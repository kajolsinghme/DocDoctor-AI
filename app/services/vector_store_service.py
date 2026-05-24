from app.db.chroma_client import chroma_client
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()


def store_chunks_in_chroma(chunks):
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-002",
        google_api_key= os.getenv("GEMINI_API_KEY")
    )

    vector_store = Chroma(
        collection_name="pdf_documents",
        embedding_function=embeddings,
        persist_directory="chroma_db"
    )
