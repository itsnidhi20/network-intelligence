import networkx as nx


def build_graph(df):
    G = nx.Graph()

    for _, row in df.iterrows():
        source = row["source"]
        target = row["target"]

        relationship = row.get("relationship", "unknown")

        G.add_edge(
            source,
            target,
            relationship=relationship
        )

    return G