# Retrieval-Augmented Generation (RAG) Server

This project implements a simple **Retrieval-Augmented Generation (RAG)** server using **FastAPI**. It provides an API for ingesting documents and querying them based on text input.

## Features:
- **Document Ingestion**: Ingest a document into the system and store it with embeddings.
- **Query Interface**: Retrieve relevant document content based on a query using embeddings.

## Technologies Used:
- **FastAPI**: Web framework for building the API.
- **Sentence-Transformers**: For generating embeddings.
- **ChromaDB**: For storing and querying embeddings.
- **Uvicorn**: High-performance ASGI server for running FastAPI.

## API Endpoints:
1. **POST /ingest/**: Ingests a document and generates embeddings.
2. **GET /query/**: Queries documents based on text input.

## Setup Instructions:
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/RAG_.git
    cd RAG_
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

4. Access the API documentation at `http://127.0.0.1:8000/docs`.

## License:
Include your license information here.
