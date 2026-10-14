import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key  = os.getenv("GOOGLE_API_KEY")

if not api_key :
    raise ValueError("GOOGLE_API_KEY is missing. Check your .env file.")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=api_key
)