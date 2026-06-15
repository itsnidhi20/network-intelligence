import pandas as pd


def get_activity_timeline(
    df,
    start_date=None,
    end_date=None
):

    filtered_df = df.copy()

    if start_date:

        filtered_df = filtered_df[
            filtered_df["date"] >= str(start_date)
        ]

    if end_date:

        filtered_df = filtered_df[
            filtered_df["date"] <= str(end_date)
        ]

    timeline = (
        filtered_df
        .groupby("date")
        .size()
        .reset_index(name="Interactions")
    )

    timeline = timeline.sort_values(
        "date"
    )

    return timeline