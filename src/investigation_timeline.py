def get_investigation_timeline(df):

    timeline = df.sort_values(
        "date"
    )

    return timeline