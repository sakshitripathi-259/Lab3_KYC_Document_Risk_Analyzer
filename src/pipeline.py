from data_ingestion import load_documents
from preprocessing import preprocess
from ner import run_ner
from risk_classifier import run_classifier

print("=" * 50)
print("KYC DOCUMENT RISK ANALYZER")
print("=" * 50)

print("\nSTEP 1 : Data Ingestion")
load_documents()

print("\nSTEP 2 : Preprocessing")
preprocess()

print("\nSTEP 3 : Named Entity Recognition")
run_ner()

print("\nSTEP 4 : Risk Classification")
run_classifier()

print("\n" + "=" * 50)
print("PIPELINE EXECUTED SUCCESSFULLY")
print("=" * 50)