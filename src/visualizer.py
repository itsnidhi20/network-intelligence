import matplotlib.pyplot as plt
import networkx as nx


def draw_graph(G):

    fig, ax = plt.subplots(figsize=(14, 10))

    pos = nx.spring_layout(
        G,
        seed=42,
        k=4,
        iterations=100
    )

    nx.draw(
        G,
        pos,
        ax=ax,
        with_labels=True,
        node_size=600,
        font_size=10
    )

    plt.title("Network Intelligence Graph")

    return fig


def draw_node_subgraph(G, selected_node):

    neighbors = list(G.neighbors(selected_node))

    nodes_to_keep = [selected_node] + neighbors

    subgraph = G.subgraph(nodes_to_keep)

    fig, ax = plt.subplots(figsize=(8, 6))

    pos = nx.spring_layout(
        subgraph,
        seed=42
    )

    nx.draw(
        subgraph,
        pos,
        ax=ax,
        with_labels=True,
        node_size=800,
        font_size=10
    )

    plt.title(
        f"Investigation View: {selected_node}"
    )

    return fig