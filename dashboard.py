import streamlit as st
import pandas as pd

from src.graph_builder import build_graph
from src.visualizer import (
    draw_graph,
    draw_node_subgraph
)
from src.analytics import (
    get_top_connected_nodes,
    calculate_risk_scores,
    get_communities,
    find_shortest_path
)

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