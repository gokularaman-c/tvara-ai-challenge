import numpy as np
from sentence_transformers import SentenceTransformer

def main():
    # Load embedding model
    model = SentenceTransformer("intfloat/e5-small-v2")

    # Example sentences (documents)
    sentences = [
        "Retrieval-Augmented Generation combines retrieval with generation.",
        "Embeddings convert text into numerical vectors.",
        "FAISS enables fast similarity search over vectors.",
        "Transformers are widely used for NLP tasks.",
        "Chunking splits large documents into smaller parts."
    ]

    # E5 model expects prefixes
    documents = [f"passage: {s}" for s in sentences]
    query = "query: What is RAG?"

    # Generate embeddings
    doc_embeddings = model.encode(documents, normalize_embeddings=True)
    query_embedding = model.encode(query, normalize_embeddings=True)

    # Similarity search (cosine similarity via dot product)
    scores = doc_embeddings @ query_embedding

    best_index = scores.argmax()

    print("Query:", query.replace("query: ", ""))
    print("Most relevant sentence:")
    print(sentences[best_index])
    print("Similarity score:", float(scores[best_index]))

if __name__ == "__main__":
    main()
