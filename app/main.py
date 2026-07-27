import streamlit as st
import pdfplumber
import pandas as pd
import re

st.set_page_config(
    page_title="KYC Document Risk Analyzer",
    page_icon="📄",
    layout="wide"
)


# -------------------------------
# PDF TEXT EXTRACTION
# -------------------------------
def extract_text(uploaded_file):

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


# -------------------------------
# CLEAN TEXT
# -------------------------------
def clean_text(text):

    text = re.sub(r"\s+", " ", text)

    return text.strip()


# -------------------------------
# EXTRACT KYC INFORMATION
# -------------------------------
def extract_entities(text):

    entities = {}

    lines = text.split("\n")

    address_started = False
    address = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.startswith("Name:"):
            entities["Name"] = line.replace("Name:", "").strip()

        elif line.startswith("DOB:"):
            entities["DOB"] = line.replace("DOB:", "").strip()

        elif line.startswith("Gender:"):
            entities["Gender"] = line.replace("Gender:", "").strip()

        elif line.startswith("Father's Name:"):
            entities["Father's Name"] = line.replace("Father's Name:", "").strip()

        elif line.startswith("Aadhaar Number:"):
            entities["Aadhaar Number"] = line.replace("Aadhaar Number:", "").strip()

        elif line.startswith("PAN No:"):
            entities["PAN Number"] = line.replace("PAN No:", "").strip()

        elif line.startswith("Passport No:"):
            entities["Passport Number"] = line.replace("Passport No:", "").strip()

        elif line.startswith("Licence No:"):
            entities["Driving Licence"] = line.replace("Licence No:", "").strip()

        elif line.startswith("Consumer Name:"):
            entities["Consumer Name"] = line.replace("Consumer Name:", "").strip()

        elif line.startswith("Address:"):
            address_started = True
            continue

        elif address_started:

            if ":" in line:
                address_started = False
            else:
                address.append(line)

    if address:
        entities["Address"] = ", ".join(address)

    pin = re.search(r"\b\d{6}\b", text)

    if pin:
        entities["PIN Code"] = pin.group()

    return entities


# -------------------------------
# RISK CLASSIFICATION
# -------------------------------
def classify_risk(entities):

    score = 0

    important_fields = [

        "Name",
        "DOB",
        "Aadhaar Number",
        "PAN Number",
        "Passport Number",
        "Driving Licence"

    ]

    for field in important_fields:

        if field in entities:
            score += 1

    if score >= 4:
        return "🟢 LOW RISK"

    elif score >= 2:
        return "🟡 MEDIUM RISK"

    else:
        return "🔴 HIGH RISK"


# -------------------------------
# STREAMLIT UI
# -------------------------------
st.title("📄 KYC Document Risk Analyzer")

uploaded_file = st.file_uploader(
    "Upload a KYC PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Document uploaded successfully!")

    raw_text = extract_text(uploaded_file)

    cleaned_text = clean_text(raw_text)

    entities = extract_entities(raw_text)

    risk = classify_risk(entities)

    st.subheader("📄 Extracted Text")

    st.text_area(
        "",
        raw_text,
        height=250
    )

    st.subheader("📝 Extracted KYC Information")

    if len(entities) == 0:

        st.warning("No information detected.")

    else:

        entity_df = pd.DataFrame(
            list(entities.items()),
            columns=["Field", "Value"]
        )

        st.table(entity_df)

    st.subheader("⚠ Risk Assessment")

    if "LOW" in risk:
        st.success(risk)

    elif "MEDIUM" in risk:
        st.warning(risk)

    else:
        st.error(risk)