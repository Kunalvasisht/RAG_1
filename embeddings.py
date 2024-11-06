from sentence_transformers import SentenceTransformer

# Load the pre-trained SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text: str):
    """
    Function to get the embedding of a text using the SentenceTransformer model.
    """
    embedding = model.encode(text)
    return embedding
