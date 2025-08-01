# Vectore Database Chroma DB and its related Functions
import chromadb
import numpy as np
from .embeddings import get_embedding

# Initialize Chroma client
client = chromadb.Client()
collection = client.get_or_create_collection("queries")

# To find Similar Query
def find_similar(query_text):
    """
    Find the most similar query to the given query_text using vector similarity.
    """
    try:
        query_vector = get_embedding(query_text)
        # Convert numpy array to list if needed
        if isinstance(query_vector, np.ndarray):
            query_vector = query_vector.tolist()
        
        results = collection.query(
            query_embeddings=[query_vector],
            n_results=1,
            include=["documents", "metadatas", "distances"]
        )
        
        if results['ids'][0]:
            return results
        else:
            return {'ids': [[]], 'documents': [[]], 'metadatas': [[]], 'distances': [[]]}
    
    except Exception as e:
        print(f"Error in find_similar: {e}")
        return {'ids': [[]], 'documents': [[]], 'metadatas': [[]], 'distances': [[]]}

# To save the Query and it's summary
def save_query(query, vector, summary):
    """
    Save a new query, its embedding vector, and its summary.
    """
    try:
        import uuid
        if isinstance(vector, np.ndarray):
            vector = vector.tolist()
        
        collection.add(
            ids=[str(uuid.uuid4())],  
            documents=[summary],      
            embeddings=[vector],      
            metadatas=[{"query": query}]
        )
        print(f"Successfully saved query: {query[:50]}...")
        
    except Exception as e:
        print(f"Error saving query: {e}")
        raise
