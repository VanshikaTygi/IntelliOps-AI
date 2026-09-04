import streamlit as st
from ui.styling import load_custom_css

st.set_page_config(page_title="IntelliOps AI", page_icon="🏭", layout="wide")
load_custom_css()

st.markdown("""
    <div class="hero-banner">
        <h1>🏭 IntelliOps AI</h1>
        <p>Unified Industrial Knowledge Intelligence Platform — transforming
        scattered documentation into actionable, source-backed answers
        through Retrieval-Augmented Generation and multi-agent AI.</p>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="metric-box"><h2>3</h2><p>AI Agents Active</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-box"><h2>RAG</h2><p>Retrieval Engine</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-box"><h2>Groq</h2><p>LLM Provider</p></div>', unsafe_allow_html=True)

st.divider()
st.markdown("""
**Use the sidebar to navigate:**
- 📂 **Upload Documents** — add manuals, SOPs, safety and maintenance reports
- 🤖 **Ask IntelliOps** — query your documents through specialized AI agents
""")