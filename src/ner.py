import pandas as pd
import spacy
import os

INPUT_FILE = "data/processed/cleaned_documents.csv"
OUTPUT_FILE = "data/processed/ner_results.csv"

print("Loading spaCy model...")
nlp = spacy.load("en_core_web_sm")


def extract_entities(text):
    doc = nlp(str(text))

    entities = []

    for ent in doc.ents:
        entities.append(f"{ent.text} ({ent.label_})")

    return ", ".join(entities)


def run_ner():
    print("Loading cleaned documents...")

    df = pd.read_csv(INPUT_FILE)

    print("Extracting entities...")

    df["entities"] = df["clean_text"].apply(extract_entities)

    os.makedirs("data/processed", exist_ok=True)

    df.to_csv(OUTPUT_FILE, index=False)

    print("\nNER completed successfully!")

    print(df[["filename", "entities"]])


if __name__ == "__main__":
    run_ner()