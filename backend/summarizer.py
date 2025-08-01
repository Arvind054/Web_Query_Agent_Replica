from .AI_Model import query_model

def summarize_text(text):
    prompt = f"Summarize the follwing text: {text}"
    return query_model(prompt)
