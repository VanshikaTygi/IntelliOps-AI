import os
from dotenv import load_dotenv
from groq import Groq
from utils.vector_store import collection

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def get_answer(question):
    """
    Takes a user's question, retrieves relevant chunks from ChromaDB,
    and asks the LLM to answer using only that retrieved context.
    Returns the answer text along with the sources it was based on.
    """

    # Step 1: Retrieve the most relevant chunks for this question
    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    retrieved_chunks = results["documents"][0]
    retrieved_metadata = results["metadatas"][0]

    # Step 2: Build the context block from retrieved chunks
    context_text = "\n\n".join(retrieved_chunks)

    # Step 3: Build the full prompt with clear instructions
    system_prompt = (
        """
        You are an industrial knowledge assistant. Answer the user's 
        question using ONLY the context provided below. If the answer 
        is not present in the context, say you don't have enough 
        information from the uploaded documents to answer that.
        """
    )

    user_prompt = f"Context:\n{context_text}\n\nQuestion: {question}"

    # Step 4: Call the LLM
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3
    )

    answer = response.choices[0].message.content

    # Step 5: Collect unique sources for citation
    sources = list(set(m["source"] for m in retrieved_metadata))

    return {
        "answer": answer,
        "sources": sources
    }


if __name__ == "__main__":
    result = get_answer("What safety measures are required for machine guarding?")
    print("ANSWER:", result["answer"])
    print("SOURCES:", result["sources"])