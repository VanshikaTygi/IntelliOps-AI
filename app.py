import streamlit as st
from utils.pdf_loader import load_pdf

st.set_page_config(
    page_title="IntelliOps AI",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 IntelliOps AI")

st.markdown("""
### Unified Industrial Knowledge Intelligence Platform

Welcome to IntelliOps AI.

This platform helps engineers and industries analyze manuals,
SOPs, maintenance reports, safety documents, and technical PDFs
using AI-powered Industrial Knowledge Intelligence.
""")

st.divider()

st.header("📂 Upload Industrial Documents")

uploaded_files = st.file_uploader(
    "Upload one or more PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

from pathlib import Path

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

if uploaded_files:

    for uploaded_file in uploaded_files:

        save_path = UPLOAD_DIR / uploaded_file.name

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"✅ {uploaded_file.name} uploaded successfully!")

        # Extract text from uploaded PDF
        pdf_text = load_pdf(save_path)

        st.subheader("📄 PDF Preview")

        st.text_area(
            "Extracted Text",
            pdf_text[:3000],
            height=250
        )

    st.subheader("Uploaded Files")

    for file in UPLOAD_DIR.iterdir():
        st.write("📄", file.name)