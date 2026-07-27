import os
import pdfplumber
import pandas as pd

INPUT_FOLDER = "data/raw/kyc_documents"
OUTPUT_FILE = "data/processed/extracted_documents.csv"


def extract_text(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text.strip()


def load_documents():
    records = []

    print("Reading KYC documents...\n")

    for file in os.listdir(INPUT_FOLDER):
        if file.endswith(".pdf"):
            path = os.path.join(INPUT_FOLDER, file)

            print(f"Processing: {file}")

            text = extract_text(path)

            records.append({
                "filename": file,
                "text": text
            })

    df = pd.DataFrame(records)

    os.makedirs("data/processed", exist_ok=True)

    df.to_csv(OUTPUT_FILE, index=False)

    print("\nExtraction completed successfully!")
    print(f"\nDocuments Processed: {len(df)}")
    print(df.head())


if __name__ == "__main__":
    load_documents()