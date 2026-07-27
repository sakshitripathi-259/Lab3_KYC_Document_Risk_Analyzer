from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

OUTPUT_DIR = "data/raw/kyc_documents"
os.makedirs(OUTPUT_DIR, exist_ok=True)

documents = [
    (
        "aadhaar_sample.pdf",
        [
            "AADHAAR CARD",
            "",
            "Name: Rahul Sharma",
            "DOB: 15/08/1996",
            "Gender: Male",
            "Aadhaar Number: 1234 5678 9012",
            "Address:",
            "12 MG Road",
            "Bhopal, Madhya Pradesh - 462001"
        ]
    ),
    (
        "pan_sample.pdf",
        [
            "PAN CARD",
            "",
            "Name: Rahul Sharma",
            "Father's Name: Mohan Sharma",
            "PAN: ABCDE1234F",
            "DOB: 15/08/1996"
        ]
    ),
    (
        "passport_sample.pdf",
        [
            "PASSPORT",
            "",
            "Passport No: P1234567",
            "Name: Rahul Sharma",
            "Nationality: Indian",
            "Date of Birth: 15/08/1996",
            "Place of Birth: Bhopal"
        ]
    ),
    (
        "driving_license_sample.pdf",
        [
            "DRIVING LICENCE",
            "",
            "Licence No: MP0420210001234",
            "Name: Rahul Sharma",
            "DOB: 15/08/1996",
            "Valid Till: 15/08/2036"
        ]
    ),
    (
        "utility_bill_sample.pdf",
        [
            "ELECTRICITY BILL",
            "",
            "Consumer Name: Rahul Sharma",
            "Consumer No: 9988776655",
            "Address:",
            "12 MG Road",
            "Bhopal",
            "Amount Due: Rs. 1450"
        ]
    )
]

for filename, lines in documents:
    c = canvas.Canvas(os.path.join(OUTPUT_DIR, filename), pagesize=A4)

    y = 800

    for line in lines:
        c.drawString(80, y, line)
        y -= 25

    c.save()

print("Sample KYC PDFs created successfully!")