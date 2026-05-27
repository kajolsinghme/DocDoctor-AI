from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

genai_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_ai_response(prompt):
    response = genai_client.models.generate_content(
        model="gemini-3.5-flash", contents=prompt
        )
    return response.text