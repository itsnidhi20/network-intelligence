import networkx as nx

from src.analytics import (
    calculate_risk_scores
)


def generate_leads(G):

    risk_scores = dict(
        calculate_risk_scores(G)
    )

    betweenness = nx.betweenness_centrality(G)

    relationship_count = {}

    for node in G.nodes():

        relationship_count[node] = 0

    for source, target in G.edges():

        relationship_count[source] += 1
        relationship_count[target] += 1

    leads = []

    for node in G.nodes():

        score = risk_scores[node]

        bridge_score = betweenness[node]

        reasons = []

        priority_score = 0

        if score > 5:

            reasons.append(
                "High risk entity"
            )

            priority_score += score

        if bridge_score > 0:

            reasons.append(
                "Hidden connector"
            )

            priority_score += (
                bridge_score * 100
            )

        if relationship_count[node] >= 2:

            reasons.append(
                "Multiple relationships"
            )

            priority_score += (
                relationship_count[node]
            )

        leads.append({

            "Entity": node,

            "Priority Score":
            round(
                priority_score,
                2
            ),

            "Reasons":
            reasons

        })

    leads = sorted(

        leads,

        key=lambda x:
        x["Priority Score"],

        reverse=True

    )

    return leads[:5]