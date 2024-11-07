from fastapi import FastAPI, HTTPException
from db_manager import ingest_document, query_document
from embeddings import get_embedding

app = FastAPI()

@app.post("/ingest/")
async def ingest(document: str):
    try:
        embedding = get_embedding(document)
        ingest_document(document, embedding)
        return {"message": "Document ingested successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to query documents
@app.get("/query/")
async def query(query_text: str):
    try:
        embedding = get_embedding(query_text)
        result = query_document(embedding)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
