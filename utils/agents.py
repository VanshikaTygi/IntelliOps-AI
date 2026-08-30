import os
from dotenv import load_dotenv
from groq import Groq
from utils.vector_store import collection

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def run_agent(role_prompt, question, n_results=3):
    """
    Generic agent runner. Takes a role-specific system prompt and a
    question, retrieves relevant context, and returns an answer
    grounded in that context, scoped to the given role's concern.
    """

    results = collection.query(
        query_texts=[question],
        n_results=n_results
    )

    retrieved_chunks = results["documents"][0]
    retrieved_metadata = results["metadatas"][0]

    context_text = "\n\n".join(retrieved_chunks)

    user_prompt = f"Context:\n{context_text}\n\nQuestion: {question}"

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": role_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3
    )

    answer = response.choices[0].message.content
    sources = list(set(m["source"] for m in retrieved_metadata))

    return {
        "answer": answer,
        "sources": sources
    }

if __name__ == "__main__":
    test_role = "You are a helpful assistant. Answer using only the provided context."
    result = run_agent(test_role, "What safety measures are required for machine guarding?")
    print("ANSWER:", result["answer"])
    print("SOURCES:", result["sources"])