import streamlit as st
from agents.supervisor import get_supervised_answer
from ui.styling import load_custom_css

load_custom_css()

st.markdown("""
    <div class="hero-banner">
        <h1>🤖 Ask IntelliOps</h1>
        <p>Ask a question and IntelliOps will automatically route it to the
        relevant specialist agent — Maintenance, Safety, or Compliance.</p>
    </div>
""", unsafe_allow_html=True)

user_question = st.text_input("Ask a question about your uploaded documents")

if user_question:

    with st.spinner("Analyzing with relevant agents..."):
        result = get_supervised_answer(user_question)

    st.markdown("#### 🧭 Agents Involved")
    tags_html = "".join(
        f'<span class="agent-tag">{agent.capitalize()}</span>'
        for agent in result["agents_used"]
    )
    st.markdown(tags_html, unsafe_allow_html=True)

    st.write("")

    for response in result["responses"]:
        st.markdown(f"### {response['agent'].capitalize()} Agent")
        st.markdown(f'<div class="status-card">{response["answer"]}</div>', unsafe_allow_html=True)

        st.caption("Sources:")
        for source in response["sources"]:
            st.write(f"📄 {source}")

        st.divider()

else:
    st.info("👆 Type a question above to get started.")