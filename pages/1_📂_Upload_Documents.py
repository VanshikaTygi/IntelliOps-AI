import streamlit as st
from pathlib import Path
from utils.pdf_loader import load_pdf
from utils.text_chunker import chunk_text
from utils.vector_store import add_chunks_to_store

st.header("📂 Upload Industrial Documents")

uploaded_files = st.file_uploader(
    "Upload one or more PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

if uploaded_files:

    for uploaded_file in uploaded_files:

        save_path = UPLOAD_DIR / uploaded_file.name

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"✅ {uploaded_file.name} uploaded successfully!")

        pdf_text = load_pdf(save_path)
        chunks = chunk_text(pdf_text)
        add_chunks_to_store(chunks, uploaded_file.name)

        st.success(f"✅ Created {len(chunks)} text chunks")

        with st.expander("🔍 Debug: View extracted chunks & preview"):
            st.subheader("First 3 Chunks")
            for i, chunk in enumerate(chunks[:3]):
                st.markdown(f"**Chunk {i+1}**")
                st.text_area(
                    label=f"Chunk {i+1}",
                    value=chunk,
                    height=150,
                    key=f"{uploaded_file.name}_{i}"
                )

            st.subheader("PDF Preview")
            st.text_area("Extracted Text", pdf_text[:3000], height=250)

    st.subheader("Uploaded Files")
    for file in UPLOAD_DIR.iterdir():
        st.write("📄", file.name)