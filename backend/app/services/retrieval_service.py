from app.services.vector_store_service import get_vector_store

def retrieve_relevant_chunks(query):
    vector_store = get_vector_store()
    results = vector_store.similarity_search(query=query, k=10)
    return results