import fitz
from pathlib import Path

def load_pdf(file_path: Path):
    """
    Load a PDF and return all extracted text.
    """

    pdf_document = fitz.open(file_path)

    text = ""

    for page in pdf_document:
        text += page.get_text() + "\n"

    pdf_document.close()

    return text