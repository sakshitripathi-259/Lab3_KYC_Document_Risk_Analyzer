import pandas as pd
import os

INPUT_FILE = "data/processed/ner_results.csv"
OUTPUT_FILE = "data/processed/risk_results.csv"


def classify_risk(entities):

    entities = str(entities).lower()

    score = 0

    if "person" in entities:
        score += 1

    if "date" in entities:
        score += 1

    if "org" in entities:
        score += 1

    if "gpe" in entities or "loc" in entities:
        score += 1

    if score >= 4:
        return "Low Risk"
    elif score >= 2:
        return "Medium Risk"
    else:
        return "High Risk"


def run_classifier():

    print("Loading NER results...")

    df = pd.read_csv(INPUT_FILE)

    print("Calculating risk levels...")

    df["Risk_Level"] = df["entities"].apply(classify_risk)

    os.makedirs("data/processed", exist_ok=True)

    df.to_csv(OUTPUT_FILE, index=False)

    print("\nRisk classification completed!")

    print(df[["filename", "Risk_Level"]])


if __name__ == "__main__":
    run_classifier()