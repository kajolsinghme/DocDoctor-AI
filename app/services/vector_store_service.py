from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
import os
from dotenv import load_dotenv

load_dotenv()

def store_chunks_in_chroma(chunks, filename):
    
    documents = create_documents(chunks, filename)
    vector_store = get_vector_store()
    vector_store.add_documents(documents)

def create_documents(chunks, filename):
    documents = []
    for chunk in chunks:
        document = Document(
            page_content=chunk["chunk"],
            metadata={
                "page": chunk["page"],
                "source": filename
            }
        )
        documents.append(document)
    return documents

def get_vector_store():
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-002",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    vector_store = Chroma(
        collection_name="pdf_documents",
        embedding_function=embeddings,
        persist_directory="chroma_db"
    )
    return vector_store