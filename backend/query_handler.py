# Validates User's query with the help of AI model
from .AI_Model import query_model
def is_valid_query(text):
    prompt = (
        "This is the Query From the User to a web_query_Agent. "
        "Validate the query as valid or invalid. "
        "Example of invalid query: 'walk my pet', 'add apples to grocery'. "
        "Just return 'valid' or 'invalid'.\n"
        f"Query: {text}"
    )
    response = query_model(prompt)
    if(response.strip().lower() == "valid"):
        return True
    else:
        return False

