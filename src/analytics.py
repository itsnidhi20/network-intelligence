import networkx as nx


def get_top_connected_nodes(G, top_n=5):
    """
    Returns nodes with highest degree
    """

    degrees = dict(G.degree())

    sorted_nodes = sorted(
        degrees.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_nodes[:top_n]

def get_communities(G):
    """
    Detect connected communities
    """

    communities = list(nx.connected_components(G))

    return communities

def find_shortest_path(G, source, target):
    """
    Find shortest path between two nodes
    """

    try:
        path = nx.shortest_path(
            G,
            source=source,
            target=target
        )

        return path

    except nx.NetworkXNoPath:
        return None
    

def get_most_influential_nodes(G, top_n=5):
    """
    Find nodes with highest betweenness centrality
    """

    centrality = nx.betweenness_centrality(G)

    sorted_nodes = sorted(
        centrality.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_nodes[:top_n]

def calculate_risk_scores(G):

    degree_scores = nx.degree_centrality(G)
    betweenness_scores = nx.betweenness_centrality(G)

    risk_scores = {}

    for node in G.nodes():

        score = (
            degree_scores[node] * 40 +
            betweenness_scores[node] * 60
        )

        risk_scores[node] = round(score, 2)

    return sorted(
        risk_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

def count_critical_entities(G):

    risk_scores = dict(
        calculate_risk_scores(G)
    )

    return sum(
        1
        for score in risk_scores.values()
        if score > 40
    )


def count_high_risk_entities(G):

    risk_scores = dict(
        calculate_risk_scores(G)
    )

    return sum(
        1
        for score in risk_scores.values()
        if score > 25
    )


def count_bridge_nodes(G):

    betweenness = nx.betweenness_centrality(G)

    return sum(
        1
        for value in betweenness.values()
        if value > 0.20
    )

def rank_communities(G):

    communities = get_communities(G)

    risk_scores = dict(
        calculate_risk_scores(G)
    )

    results = []

    for i, community in enumerate(
        communities,
        start=1
    ):

        community_risk = 0

        high_risk_members = []

        for node in community:

            score = risk_scores.get(
                node,
                0
            )

            community_risk += score

            if score > 25:

                high_risk_members.append(
                    (node, score)
                )

        results.append({

        "Community": i,

        "Members": sorted(
            list(community)
        ),

        "Member Count": len(
            community
        ),

        "Risk Score": round(
            community_risk,
            2
        ),

        "High Risk Members":
        high_risk_members

        })

    results = sorted(
        results,
        key=lambda x: x["Risk Score"],
        reverse=True
    )

    return results