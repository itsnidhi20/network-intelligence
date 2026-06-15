from src.analytics import (
    calculate_risk_scores,
    get_communities,
    rank_communities
)


def generate_executive_summary(
    G,
    timeline_df
):

    risk_scores = dict(
        calculate_risk_scores(G)
    )

    communities = get_communities(G)

    ranked = rank_communities(G)

    top_entities = sorted(
        risk_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )[:3]

    peak_day = timeline_df.loc[
        timeline_df["Interactions"].idxmax()
    ]

    summary = f"""
EXECUTIVE INTELLIGENCE SUMMARY

Entities: {G.number_of_nodes()}
Communities: {len(communities)}

Highest Risk Community:
Community {ranked[0]["Community"]}
Risk Score: {ranked[0]["Risk Score"]}

Peak Activity:
{peak_day["date"]}
({peak_day["Interactions"]} interactions)

Top Entities:
"""

    for entity, score in top_entities:

        summary += (
            f"\n- {entity} "
            f"(Risk Score: {round(score,2)})"
        )

    return summary