# 📄 KYC Document Risk Analyzer

An AI-powered KYC Document Risk Analyzer that extracts important information from PDF-based KYC documents, identifies key entities, performs document risk assessment, and provides an interactive Streamlit dashboard.

---

## 🚀 Features

- 📄 Upload KYC PDF documents
- 🔍 Automatic text extraction using PDFPlumber
- 🧹 Text preprocessing
- 📝 Entity extraction
  - Name
  - DOB
  - Gender
  - Aadhaar Number
  - PAN Number
  - Passport Number
  - Driving Licence
  - Address
  - PIN Code
- ⚠ Intelligent document risk assessment
- 📊 Interactive Streamlit web application

---

## 🛠 Technologies Used

- Python
- Streamlit
- PDFPlumber
- spaCy
- Pandas
- Regular Expressions (Regex)

---

## 📂 Project Structure

```
Lab3_KYC_Document_Risk_Analyzer/
│
├── app/
│   └── main.py
│
├── data/
│   ├── raw/
│   │   └── kyc_documents/
│   └── processed/
│
├── src/
│   ├── data_ingestion.py
│   ├── preprocessing.py
│   ├── ner.py
│   ├── risk_classifier.py
│   ├── pipeline.py
│   └── evaluation.py
│
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/sakshitripathi-259/Lab3_KYC_Document_Risk_Analyzer.git
```

Go into the project folder

```bash
cd Lab3_KYC_Document_Risk_Analyzer
```

Create a virtual environment

```bash
python -m venv kyc_env
```

Activate it

Linux / WSL

```bash
source kyc_env/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Project

Run the complete pipeline

```bash
python src/pipeline.py
```

Launch the Streamlit application

```bash
python -m streamlit run app/main.py
```

---


## 📊 Sample Output

| Field | Value |
|------|------|
| Name | Rahul Sharma |
| DOB | 15/08/1996 |
| Gender | Male |
| Aadhaar Number | 1234 5678 9012 |
| Address | 12 MG Road, Bhopal |
| PIN Code | 462001 |

Risk Level

🟡 Medium Risk

---

## 🔮 Future Improvements

- OCR support for scanned documents
- Deep Learning based NER
- Face verification
- Signature verification
- Fake document detection
- Multi-language support

---

## 👩‍💻 Author

**Sakshi Tripathi**

Biotechnology Graduate | AI & Machine Learning Enthusiast

GitHub

https://github.com/sakshitripathi-259
