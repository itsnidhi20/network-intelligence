import streamlit as st
import pandas as pd

from src.graph_builder import build_graph
import matplotlib.pyplot as plt
from src.investigation_timeline import (
    get_investigation_timeline
)
from src.lead_generator import (
    generate_leads
)
from src.suspicious_relationships import (
    find_suspicious_relationships
)
from src.executive_summary import (
    generate_executive_summary
)
from src.hidden_connectors import (
    detect_hidden_connectors
)
from src.timeline import get_activity_timeline
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
    count_bridge_nodes,
    rank_communities
)
from src.interactive_visualizer import (
    create_interactive_graph
)
from src.exporter import create_text_report
from src.pdf_exporter import create_pdf_report
import tempfile
from pathlib import Path

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

    st.subheader("🏘️ Community Overview")

    community_results = rank_communities(G)

    community_table = []

    for community in community_results:

        community_table.append({

            "Community":
            community["Community"],

            "Members":
            ", ".join(
                community["Members"]
            ),

            "Member Count":
            community["Member Count"]

        })

    community_df = pd.DataFrame(
        community_table
    )

    st.dataframe(
        community_df,
        use_container_width=True
    )

    st.subheader("🏘️ Community Intelligence")

    community_results = rank_communities(G)
    for community in community_results:

        st.write(
            f"### Community {community['Community']}"
        )

        st.write(
            f"Members: {community['Member Count']}"
        )

        st.write("Member List")

        st.write(
            ", ".join(
                community["Members"]
            )
        )

        st.write(
            f"Risk Score: {community['Risk Score']}"
        )

        if community["Risk Score"] > 150:

            st.error(
                "🔴 HIGH RISK COMMUNITY"
            )

        elif community["Risk Score"] > 75:

            st.warning(
                "🟠 MEDIUM RISK COMMUNITY"
            )

        else:

            st.success(
                "🟢 LOW RISK COMMUNITY"
            )

        st.write("### High Risk Members")

        if community["High Risk Members"]:

            for node, score in community["High Risk Members"]:

                st.write(
                    f"• {node} ({score})"
                )

        else:

            st.write(
                "No high risk members."
            )

    st.subheader(
    "🕵️ Hidden Connectors"
    )

    connectors = detect_hidden_connectors(G)

    if connectors:

        connectors_df = pd.DataFrame(
            connectors
        )

        st.dataframe(
            connectors_df,
            use_container_width=True
        )

    else:

        st.info(
            "No hidden connectors detected."
        )

    st.subheader(
    "🔍 Suspicious Relationships"
)

    relationships = (
        find_suspicious_relationships(G)
    )

    relationships_df = pd.DataFrame(
        relationships
    )

    st.dataframe(
        relationships_df,
        use_container_width=True
    )

    st.subheader(
    "🎯 Investigation Leads"
)

    leads = generate_leads(G)

    if leads:

        for i, lead in enumerate(
        leads,
        start=1
        ):

            st.write(
                f"### 🎯 Priority #{i}"
            )

            st.write(
                f"Entity: "
                f"{lead['Entity']}"
            )

            st.write(
                f"Priority Score: "
                f"{lead['Priority Score']}"
            )

            st.write(
                "Reasons:"
            )

            for reason in lead["Reasons"]:

                st.write(
                    f"• {reason}"
                )

    else:

        st.info(
            "No investigation leads identified."
        )

    st.subheader(
    "🕒 Investigation Timeline"
    )

    timeline_events = (
        get_investigation_timeline(df)
    )

    for _, row in timeline_events.iterrows():

        st.write(
            f"📅 {row['date']} | "
            f"{row['source']} → "
            f"{row['target']} "
            f"({row['relationship']})"
        )

    # EXISTING CODE CONTINUES
    st.subheader("📈 Timeline Intelligence")

    col1, col2 = st.columns(2)

    with col1:

        start_date = st.date_input(
            "Start Date",
            value=pd.to_datetime(
                df["date"]
            ).min()
        )

    with col2:

        end_date = st.date_input(
            "End Date",
            value=pd.to_datetime(
                df["date"]
            ).max()
        )
        
    
    if start_date > end_date:

        st.error(
            "Start Date must be before End Date."
        )

        st.stop()

    timeline_df = get_activity_timeline(
        
        
        df,
        start_date=start_date,
        end_date=end_date
    )

    fig, ax = plt.subplots(
        figsize=(8, 4)
    )

    ax.plot(
        timeline_df["date"],
        timeline_df["Interactions"],
        marker="o"
    )

    ax.set_title(
        "Network Activity Over Time"
    )

    ax.set_xlabel(
        "Date"
    )

    ax.set_ylabel(
    "Interactions"
    )

    plt.xticks(
    
    rotation=45
    )

    st.pyplot(fig)

    if not timeline_df.empty:

        peak_day = timeline_df.loc[
            timeline_df["Interactions"].idxmax()
        ]

        st.info(
            f"📌 Peak activity occurred on "
            f"{peak_day['date']} "
            f"with {peak_day['Interactions']} interactions."
        )

    else:

        st.warning(
            "No activity found for the selected date range."
        )

    st.subheader(
    "🧠 Executive Intelligence Summary"
    )

    summary_text = (
        generate_executive_summary(
            G,
            timeline_df
        )
    )

    st.download_button(
        label="📄 Download Executive Summary",
        data=summary_text,
        file_name="executive_summary.txt",
        mime="text/plain"
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

        temp_pdf = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
        )

        temp_pdf.close()

        create_pdf_report(
        report,
        temp_pdf.name
        )

        with open(temp_pdf.name, "rb") as pdf_file:

            st.download_button(
                label="📑 Download PDF Report",
                data=pdf_file,
                file_name=f"Investigation_Report_{selected_node}.pdf",
                mime="application/pdf"
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