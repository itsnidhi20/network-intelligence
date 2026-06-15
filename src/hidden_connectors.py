import networkx as nx


def detect_hidden_connectors(G):

    betweenness = nx.betweenness_centrality(G)

    results = []

    for node in G.nodes():

        degree = G.degree(node)

        bridge_score = betweenness[node]

        if degree <= 3 and bridge_score > 0:

            results.append({

                "Entity": node,

                "Connections": degree,

                "Bridge Score": round(
                    bridge_score,
                    3
                )

            })

    results = sorted(

        results,

        key=lambda x:
        x["Bridge Score"],

        reverse=True

    )

    return results