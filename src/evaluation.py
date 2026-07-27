import pandas as pd

INPUT_FILE = "data/processed/risk_results.csv"


def evaluate():

    print("Loading risk analysis results...\n")

    df = pd.read_csv(INPUT_FILE)

    total = len(df)

    print(f"Total Documents Processed: {total}\n")

    print("Risk Distribution:\n")

    print(df["Risk_Level"].value_counts())

    print("\nPercentage Distribution:\n")

    print((df["Risk_Level"].value_counts(normalize=True) * 100).round(2))


if __name__ == "__main__":
    evaluate()