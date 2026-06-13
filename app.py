from src.data_loader import load_data
from src.graph_builder import build_graph
from src.analytics import get_top_connected_nodes
from src.analytics import get_communities
from src.analytics import (
    get_top_connected_nodes,
    get_communities,
    find_shortest_path
)
from src.analytics import (
    get_top_connected_nodes,
    get_communities,
    find_shortest_path,
    get_most_influential_nodes
)
from src.visualizer import draw_graph
from src.analytics import calculate_risk_scores

# Load Data
df = load_data("data/interactions.csv")

# Build Graph
G = build_graph(df)

# Network Summary
print("\n===== NETWORK SUMMARY =====")

print(f"Nodes: {G.number_of_nodes()}")
print(f"Edges: {G.number_of_edges()}")

# Nodes
print("\nNodes:")
print(list(G.nodes()))

# Edges
print("\nEdges:")
print(list(G.edges(data=True)))

# Top Connected Nodes
print("\n===== TOP CONNECTED NODES =====")

top_nodes = get_top_connected_nodes(G)

for node, degree in top_nodes:
    print(f"{node}: {degree}")

print("\n===== COMMUNITIES =====")

communities = get_communities(G)

for idx, community in enumerate(communities, start=1):
    print(f"\nCommunity {idx}:")
    print(sorted(community))


print("\n===== SHORTEST PATH =====")

source = "A"
target = "F"

path = find_shortest_path(
    G,
    source,
    target
)

if path:
    print(" -> ".join(path))
else:
    print("No path found")


print("\n===== MOST INFLUENTIAL NODES =====")

influential_nodes = get_most_influential_nodes(G)

for node, score in influential_nodes:
    print(f"{node}: {score:.4f}")



print("\n===== RISK SCORES =====")

risk_scores = calculate_risk_scores(G)

for node, score in risk_scores:
    print(f"{node}: {score}")

draw_graph(G)