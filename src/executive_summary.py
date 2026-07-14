from src.analytics import (
    calculate_risk_scores,
    get_communities,
    rank_communities,
    count_critical_entities,
    count_bridge_nodes
)

from src.lead_generator import (
    generate_leads
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

    leads = generate_leads(G)

    top_entities = sorted(
        risk_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    peak_day = timeline_df.loc[
        timeline_df["Interactions"].idxmax()
    ]

    critical_entities = (
        count_critical_entities(G)
    )

    bridge_nodes = (
        count_bridge_nodes(G)
    )

    highest_risk_community = ranked[0]

    summary = f"""
============================================================
                EXECUTIVE INTELLIGENCE REPORT
============================================================

MISSION OVERVIEW
------------------------------------------------------------
This report summarizes key findings identified within the
interaction network. The analysis focuses on high-risk
entities, hidden connectors, community structures, and
investigation priorities.

NETWORK OVERVIEW
------------------------------------------------------------
Total Entities        : {G.number_of_nodes()}
Total Relationships   : {G.number_of_edges()}
Communities Detected  : {len(communities)}

THREAT ASSESSMENT
------------------------------------------------------------
Critical Entities     : {critical_entities}
Bridge Entities       : {bridge_nodes}

Highest Risk Community:
Community {highest_risk_community["Community"]}

Community Risk Score:
{round(highest_risk_community["Risk Score"], 2)}

INTELLIGENCE ASSESSMENT
------------------------------------------------------------
The network contains {G.number_of_nodes()} entities linked
through {G.number_of_edges()} relationships and organized
into {len(communities)} distinct communities.

Community {highest_risk_community["Community"]}
demonstrates the highest concentration of risk indicators,
making it the primary area of interest for investigators.

Activity analysis identified a peak interaction period on
{peak_day["date"]}, during which
{peak_day["Interactions"]} interactions were recorded.
This spike may indicate increased coordination or
communication activity.

ACTIVITY ANALYSIS
------------------------------------------------------------
Peak Activity Date:
{peak_day["date"]}

Interactions Recorded:
{peak_day["Interactions"]}

HIGH-RISK ENTITIES
------------------------------------------------------------
"""

    for entity, score in top_entities:

        summary += (
            f"\n• {entity}"
            f" | Risk Score: "
            f"{round(score, 2)}"
        )

    summary += """

INVESTIGATION PRIORITIES
------------------------------------------------------------
"""

    for lead in leads[:5]:

        summary += (
            f"\n• Entity {lead['Entity']} "
            f"has been identified as a priority target "
            f"(Priority Score: "
            f"{round(lead['Priority Score'], 2)})."
        )

    summary += """

ANALYST RECOMMENDATIONS
------------------------------------------------------------
1. Prioritize investigation of the highest-risk entities.
2. Examine bridge entities for hidden communication paths.
3. Review interactions within the highest-risk community.
4. Investigate periods of unusually high activity.
5. Monitor priority targets for emerging relationships.
6. Conduct deeper analysis on suspicious relationship chains.

EXECUTIVE CONCLUSION
------------------------------------------------------------
The network exhibits identifiable clusters, key bridge
entities, and several high-priority investigation targets.
Further analysis should focus on high-risk communities and
entities demonstrating elevated connectivity or influence
within the network structure.

============================================================
                    END OF REPORT
============================================================
"""

    return summary