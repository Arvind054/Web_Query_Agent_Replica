#Imports
from backend.query_handler import is_valid_query
from backend.vector_db import find_similar, save_query
from backend.embeddings import get_embedding
from backend.DuckDuckSearch import scrape_top_sites
from backend.summarizer import summarize_text

# To Handle the User Query
def handle_query(query):
    #Validate the Query
    if not is_valid_query(query):
        return "This is not a valid query."
    
    # Check for Similarity in the DB
    similar_results = find_similar(query)
    if similar_results['ids'][0] and len(similar_results['ids'][0]) > 0:
        print("Found similar query in database")
        return similar_results['documents'][0][0]  # Return the first document
    
    #Scrape the Web using DuckDuckGo search
    data = scrape_top_sites(query)
    #Summarise the Data using AI Model
    summary = summarize_text(data)
    #Save the Query to the DB
    save_query(query, get_embedding(query), summary)
    return summary
if __name__ == "__main__":
    query = input("Enter your query: ")
    result = handle_query(query)
    print("\nAnswer:\n", result)
