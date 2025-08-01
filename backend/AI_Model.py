# Create an Instance of Gemini AI model using Lanchain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
def query_model(query):
    response = model.invoke(query)
    return response.content
