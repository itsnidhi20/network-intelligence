import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)

    required_columns = ["source", "target"]

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    return df