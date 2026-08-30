import streamlit as st
from utils.pdf_loader import load_pdf
from utils.text_chunker import chunk_text
from utils.vector_store import add_chunks_to_store
from agents.supervisor import get_supervised_answer

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

        # Split extracted text into chunks
        chunks = chunk_text(pdf_text)

        add_chunks_to_store(chunks, uploaded_file.name)

        st.success(f"✅ Created {len(chunks)} text chunks")

        st.subheader("📄 First 3 Chunks")

        for i, chunk in enumerate(chunks[:3]):
            st.markdown(f"### Chunk {i+1}")
            st.text_area(
                label=f"Chunk {i+1}",
                value=chunk,
                height=150,
                key=f"{uploaded_file.name}_{i}"
            )

        st.subheader("📄 PDF Preview")

        st.text_area(
            "Extracted Text",
            pdf_text[:3000],
            height=250
        )

    st.subheader("Uploaded Files")

    for file in UPLOAD_DIR.iterdir():
        st.write("📄", file.name)


st.divider()

st.header("🤖 Ask IntelliOps")

user_question = st.text_input("Ask a question about your uploaded documents")

if user_question:

    with st.spinner("Analyzing with relevant agents..."):
        result = get_supervised_answer(user_question)

    st.subheader("🧭 Agents Involved")
    st.write(", ".join(agent.capitalize() for agent in result["agents_used"]))

    for response in result["responses"]:
        st.markdown(f"### {response['agent'].capitalize()} Agent")
        st.write(response["answer"])

        st.caption("Sources:")
        for source in response["sources"]:
            st.write(f"📄 {source}")

        st.divider()

else:
    st.warning("Please type a question first.")