import os
from docx import Document
import PyPDF2

def extract_text_from_resume(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    text = ""

    if ext == ".docx":
        try:
            doc = Document(file_path)
            for para in doc.paragraphs:
                text += para.text
        except Exception as e:
            return "Error reading DOCX file"

    elif ext == ".pdf":
        try:
            with open(file_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    text += page.extract_text() or ""
        except Exception as e:
            return "Error reading PDF file"

    else:
        return "Unsupported file format"

    return text