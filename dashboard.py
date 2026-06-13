import streamlit as st
import pandas as pd

from src.graph_builder import build_graph
from src.visualizer import (
    draw_graph,
    draw_node_subgraph
)
from src.alerts import generate_alerts
from src.report_generator import generate_report
from src.analytics import (
    get_top_connected_nodes,
    calculate_risk_scores,
    get_communities,
    find_shortest_path,
    count_critical_entities,
    count_high_risk_entities,
    count_bridge_nodes
)
from src.interactive_visualizer import (
    create_interactive_graph
)
from src.exporter import create_text_report

import streamlit.components.v1 as components

st.title("🕸️ Network Intelligence Platform")

uploaded_file = st.file_uploader(
    "Upload Interaction CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(df)

    G = build_graph(df)

    st.subheader("📊 Intelligence Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🚨 Critical",
            count_critical_entities(G)
        )

    with col2:
        st.metric(
            "⚠️ High Risk",
            count_high_risk_entities(G)
        )

    with col3:
        st.metric(
            "🌉 Bridges",
            count_bridge_nodes(G)
        )

    with col4:
        st.metric(
            "👥 Communities",
            len(get_communities(G))
        )

    st.subheader("🚨 Intelligence Alerts")

    alerts = generate_alerts(G)

    if alerts:

        alerts_df = pd.DataFrame(alerts)

        st.dataframe(
            alerts_df,
            use_container_width=True
        )

    else:

        st.success(
            "No alerts detected."
        )

    st.subheader("Network Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Nodes", G.number_of_nodes())

    with col2:
        st.metric("Edges", G.number_of_edges())

    st.subheader("Top Connected Nodes")

    top_nodes = get_top_connected_nodes(G)

    top_df = pd.DataFrame(
        top_nodes,
        columns=["Node", "Connections"]
    )

    st.dataframe(top_df)

    st.subheader("Risk Scores")

    risk_scores = calculate_risk_scores(G)

    risk_df = pd.DataFrame(
    risk_scores,
    columns=["Node", "Risk Score"]
    )

    st.dataframe(risk_df)

    st.subheader("Investigate a Node")

    selected_node = st.selectbox(
    "Choose a node",
    sorted(list(G.nodes()))
    )   
    risk_dict = dict(risk_scores)

    st.write("### Risk Score")

    st.metric(
    "Risk Score",
    risk_dict[selected_node]
    )
    connections = list(G.neighbors(selected_node))

    st.write("### Direct Connections")

    for node in connections:

        relationship = G[selected_node][node]["relationship"]

        st.write(
            f"• {node} ({relationship})"
        )

    st.write("### Community")

    communities = get_communities(G)

    for community in communities:

        if selected_node in community:

            for member in sorted(list(community)):
                st.write(f"• {member}")

            break

    st.subheader("📄 Investigation Report")

    if st.button("Generate Report"):

        report = generate_report(
            G,
            selected_node
        )

        st.write("### Entity")
        st.write(report["Entity"])

        st.write("### Risk Score")
        st.write(report["Risk Score"])

        st.write("### Risk Level")
        st.write(report["Risk Level"])
        st.write("### Connections")

        for connection in report["Connections"]:
            st.write(f"• {connection}")

        st.write("### Community")

        for member in report["Community"]:
            st.write(f"• {member}")

        st.write("### Reasons")

        if report["Reasons"]:

            for reason in report["Reasons"]:
                st.write(f"• {reason}")

        else:

            st.write("No significant findings.")
        st.write("### Recommendation")
        st.write(report["Recommendation"])

        report_text = create_text_report(
        report
    )

        st.download_button(
            label="📄 Download Report",
            data=report_text,
            file_name=f"{selected_node}_report.txt",
            mime="text/plain"
        )

    st.write("### Investigation Graph")

    subgraph_fig = draw_node_subgraph(
    G,
    selected_node
    )

    st.pyplot(subgraph_fig)

    st.subheader("Trace Relationship")

    source_node = st.selectbox(
    "Start Node",
    sorted(list(G.nodes())),
    key="source"
    )

    target_node = st.selectbox(
    "End Node",
    sorted(list(G.nodes())),
    key="target"
    )

    if st.button("Trace Connection"):

        path = find_shortest_path(
            G,
            source_node,
            target_node
     )

        if path:
            st.success(" → ".join(path))
        else:
            st.error("No connection found")

    st.subheader("Network Visualization")

    fig = draw_graph(G)

    st.pyplot(fig)
    st.subheader("🌐 Interactive Network")

    html_file = create_interactive_graph(G)

    with open(html_file, "r", encoding="utf-8") as f:

        source_code = f.read()

    components.html(
        source_code,
        height=750
    )