import os
from dotenv import load_dotenv
from groq import Groq
from utils.vector_store import collection

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def get_answer(question, source_filter=None):
    query_kwargs = {
        "query_texts": [question],
        "n_results": 3
    }

    if source_filter:
        query_kwargs["where"] = {"source": {"$in": source_filter}}

    results = collection.query(**query_kwargs)

    retrieved_chunks = results["documents"][0]
    retrieved_metadata = results["metadatas"][0]

    context_text = "\n\n".join(retrieved_chunks)

    system_prompt = (
        """
        You are an industrial knowledge assistant. Answer the user's 
        question using ONLY the context provided below. If the answer 
        is not present in the context, say you don't have enough 
        information from the uploaded documents to answer that.
        """
    )

    user_prompt = f"Context:\n{context_text}\n\nQuestion: {question}"

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3
    )

    answer = response.choices[0].message.content
    sources = list(set(m["source"] for m in retrieved_metadata))

    return {"answer": answer, "sources": sources}


if __name__ == "__main__":
    result = get_answer("What safety measures are required for machine guarding?")
    print("ANSWER:", result["answer"])
    print("SOURCES:", result["sources"])