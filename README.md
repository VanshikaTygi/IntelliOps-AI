# 🏭 IntelliOps AI

### Unified Industrial Knowledge Intelligence Platform

IntelliOps AI turns scattered industrial documentation — manuals, SOPs, maintenance reports, safety documents — into a searchable, queryable knowledge system using Retrieval-Augmented Generation (RAG) and multi-agent AI.

Instead of manually searching through hundreds of pages of documentation, engineers will be able to ask direct questions and get accurate, source-backed answers.

---

## How it works
Industrial PDFs → Text Extraction → Chunking → Embeddings →
Vector Database → Retrieval → AI Agents → Actionable Answers


## Current Progress

- [x] PDF upload and text extraction (PyMuPDF)
- [x] Text chunking (LangChain)
- [x] Embedding generation (`sentence-transformers`)
- [x] Vector storage and retrieval (ChromaDB) — verified working end-to-end
- [ ] LLM-powered question answering with source citations
- [ ] Multi-agent architecture (Supervisor, Maintenance, Safety, Compliance agents)
- [ ] Industrial dashboard UI (risk scores, asset timelines)

## Tech Stack

- **Language:** Python
- **UI:** Streamlit
- **Orchestration:** LangChain
- **Vector Database:** ChromaDB
- **Embeddings:** `sentence-transformers` (all-MiniLM-L6-v2)
- **Document Processing:** PyMuPDF

## Project Status

🚧 Actively in development.