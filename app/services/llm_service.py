from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

genai_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = genai_client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)