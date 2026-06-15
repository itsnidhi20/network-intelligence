from src.analytics import (
    calculate_risk_scores
)


def find_suspicious_relationships(G):

    risk_scores = dict(
        calculate_risk_scores(G)
    )

    results = []

    for source, target, data in G.edges(data=True):

        combined_risk = (

            risk_scores.get(source, 0)
            +

            risk_scores.get(target, 0)

        )

        results.append({

            "Source": source,

            "Target": target,

            "Relationship":
            data["relationship"],

            "Combined Risk":
            round(
                combined_risk,
                2
            )

        })

    results = sorted(

        results,

        key=lambda x:
        x["Combined Risk"],

        reverse=True

    )

    return results[:10]