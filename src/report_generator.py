from src.analytics import (
    calculate_risk_scores,
    get_communities
)

import networkx as nx


def generate_report(G, selected_node):

    risk_scores = dict(
        calculate_risk_scores(G)
    )

    report = {}

    risk_score = risk_scores.get(
        selected_node,
        0
    )

    report["Entity"] = selected_node
    report["Risk Score"] = risk_score

    connections = list(
        G.neighbors(selected_node)
    )

    report["Connections"] = connections

    communities = get_communities(G)

    community_found = []

    for community in communities:

        if selected_node in community:

            community_found = sorted(
                list(community)
            )

            break

    report["Community"] = community_found

    # Risk Level

    if risk_score >= 40:
        risk_level = "Critical"

    elif risk_score >= 25:
        risk_level = "High"

    elif risk_score >= 10:
        risk_level = "Medium"

    else:
        risk_level = "Low"

    report["Risk Level"] = risk_level

    # Investigation Reasons

    reasons = []

    if risk_score >= 40:
        reasons.append(
            "Very high risk score"
        )

    elif risk_score >= 25:
        reasons.append(
            "High risk score"
        )

    if len(connections) >= 5:
        reasons.append(
            "Highly connected entity"
        )

    betweenness = nx.betweenness_centrality(G)

    if betweenness[selected_node] > 0.20:
        reasons.append(
            "Acts as a bridge between network segments"
        )

    report["Reasons"] = reasons

    # Recommendation

    if risk_level == "Critical":

        recommendation = (
            "Immediate investigation recommended."
        )

    elif risk_level == "High":

        recommendation = (
            "Review entity activity closely."
        )

    else:

        recommendation = (
            "Monitor for future activity."
        )

    report["Recommendation"] = recommendation

    return report