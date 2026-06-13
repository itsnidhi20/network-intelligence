import networkx as nx

from src.analytics import calculate_risk_scores


def generate_alerts(G):

    alerts = []

    risk_scores = dict(
        calculate_risk_scores(G)
    )

    degrees = dict(G.degree())

    betweenness = nx.betweenness_centrality(G)

    for node in G.nodes():

        score = risk_scores.get(node, 0)

        alert_types = []

        if score > 40:
            alert_types.append("Critical Risk")

        elif score > 25:
            alert_types.append("High Risk")

        if degrees[node] >= 5:
            alert_types.append("Highly Connected")

        if betweenness[node] > 0.20:
            alert_types.append("Bridge Node")

        if alert_types:

            alerts.append({
                "Entity": node,
                "Risk Score": score,
                "Alert Type": ", ".join(alert_types)
            })

    alerts = sorted(
        alerts,
        key=lambda x: x["Risk Score"],
        reverse=True
    )

    return alerts