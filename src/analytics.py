import networkx as nx

from networkx.algorithms.community import (
    greedy_modularity_communities
)


def get_top_connected_nodes(
    G,
    top_n=5
):
    """
    Returns nodes with highest degree
    """

    degrees = dict(
        G.degree()
    )

    sorted_nodes = sorted(
        degrees.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_nodes[:top_n]


def get_communities(G):
    """
    Detect communities using modularity optimization
    instead of connected components.
    """

    communities = list(
        greedy_modularity_communities(G)
    )

    return communities


def find_shortest_path(
    G,
    source,
    target
):
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


def get_most_influential_nodes(
    G,
    top_n=5
):
    """
    Find nodes with highest betweenness centrality
    """

    centrality = nx.betweenness_centrality(
        G
    )

    sorted_nodes = sorted(
        centrality.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_nodes[:top_n]


def calculate_risk_scores(G):
    """
    Composite intelligence risk score.

    Degree      = connectivity
    Betweenness = hidden connector behavior
    Closeness   = overall network reach
    """

    degree_scores = nx.degree_centrality(G)

    betweenness_scores = (
        nx.betweenness_centrality(G)
    )

    closeness_scores = (
        nx.closeness_centrality(G)
    )

    risk_scores = {}

    for node in G.nodes():

        score = (

            degree_scores[node] * 30 +

            betweenness_scores[node] * 50 +

            closeness_scores[node] * 20

        )

        risk_scores[node] = round(
            score,
            2
        )

    return sorted(
        risk_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )


def count_critical_entities(G):
    """
    Very high-risk entities
    """

    risk_scores = dict(
        calculate_risk_scores(G)
    )

    return sum(
        1
        for score in risk_scores.values()
        if score > 35
    )


def count_high_risk_entities(G):
    """
    Elevated-risk entities
    """

    risk_scores = dict(
        calculate_risk_scores(G)
    )

    return sum(
        1
        for score in risk_scores.values()
        if score > 25
    )


def count_bridge_nodes(G):
    """
    Entities acting as bridges between groups
    """

    betweenness = (
        nx.betweenness_centrality(G)
    )

    return sum(
        1
        for value in betweenness.values()
        if value > 0.10
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
                    (
                        node,
                        score
                    )
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
            sorted(
                high_risk_members,
                key=lambda x: x[1],
                reverse=True
            )

        })

    results = sorted(
        results,
        key=lambda x: x["Risk Score"],
        reverse=True
    )

    return results