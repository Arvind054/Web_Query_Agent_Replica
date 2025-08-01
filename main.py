from backend.query_handler import is_valid_query
from backend.vector_db import find_similar, save_query
from backend.embeddings import get_embedding
from backend.DuckDuckSearch import scrape_top_sites
from backend.summarizer import summarize_text
def handle_query(query):
    if not is_valid_query(query):
        return "This is not a valid query."
    print("Till Valid Query")
    
    similar_results = find_similar(query)
    print("Similar results:", similar_results)
    
    # Check if we have any results (ids[0] should be a list, if it has items, we have results)
    if similar_results['ids'][0] and len(similar_results['ids'][0]) > 0:
        print("Found similar query in database")
        return similar_results['documents'][0][0]  # Return the first document
    
    print("No similar queries found")
    data = scrape_top_sites(query)
    summary = summarize_text(data)
    save_query(query, get_embedding(query), summary)
    return summary
if __name__ == "__main__":
    query = input("Enter your query: ")
    result = handle_query(query)
    print("\nAnswer:\n", result)
