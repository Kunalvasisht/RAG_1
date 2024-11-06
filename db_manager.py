import chromadb
from chromadb import Client


# Initialize the ChromaDB client
client = Client()

# Chroma collection to store the documents
collection = client.create_collection("documents")

def ingest_document(document: str, embedding: list):
    """
    Function to ingest a document with its corresponding embedding into the database.
    """
    collection.add(
        documents=[document],
        embeddings=[embedding],
        metadatas=[{"source": "example"}],
        ids=["doc1"]
    )

def query_document(query_embedding: list):
    """
    Function to query the database using the document's embedding.
    """
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=1
    )
    return results['documents']
