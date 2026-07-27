import re
import pandas as pd
import os

INPUT_FILE = "data/processed/extracted_documents.csv"
OUTPUT_FILE = "data/processed/cleaned_documents.csv"


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s:/.-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def preprocess():
    print("Loading extracted documents...")

    df = pd.read_csv(INPUT_FILE)

    print("Cleaning text...")

    df["clean_text"] = df["text"].apply(clean_text)

    os.makedirs("data/processed", exist_ok=True)

    df.to_csv(OUTPUT_FILE, index=False)

    print("\nPreprocessing completed!")

    print(df[["filename", "clean_text"]].head())


if __name__ == "__main__":
    preprocess()