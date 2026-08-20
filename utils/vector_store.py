from sentence_transformers import SentenceTransformer
import chromadb

# Load the embedding model once (not every time we call a function)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Create a persistent ChromaDB client - "persistent" means data is saved
# to disk in data/vector_db, so it survives even after you close the app
chroma_client = chromadb.PersistentClient(path="data/vector_db")

# Get (or create, if it doesn't exist yet) a collection named "industrial_docs"
# Think of a "collection" like a table in a database, purpose-built for vectors
collection = chroma_client.get_or_create_collection(name="industrial_docs")


def add_chunks_to_store(chunks, source_filename):
    """
    Takes a list of text chunks from one PDF, converts each into an
    embedding, and stores it in ChromaDB along with the original text
    and metadata (so we know which file/chunk it came from later).
    """

    # Convert all chunks into embeddings in one batch call (efficient)
    embeddings = embedding_model.encode(chunks).tolist()

    # ChromaDB needs a unique ID for every entry we store
    ids = [f"{source_filename}_chunk_{i}" for i in range(len(chunks))]

    # Metadata helps us trace an answer back to its source later
    metadatas = [{"source": source_filename, "chunk_index": i} for i in range(len(chunks))]

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=chunks,
        metadatas=metadatas
    )