import chromadb
from chromadb import Client


client = Client()

collection = client.create_collection("documents")

def ingest_document(document: str, embedding: list):
    collection.add(
        documents=[document],
        embeddings=[embedding],
        metadatas=[{"source": "example"}],
        ids=["doc1"]
    )

def query_document(query_embedding: list):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=1
    )
    return results['documents']
