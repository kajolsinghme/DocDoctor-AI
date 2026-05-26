import fitz
from app.services.chunk_service import chunk_text
from app.services.vector_store_service import store_chunks_in_chroma

async def upload_pdf_service(pdf_file):
    file_content = await pdf_file.read()
    file_path = f"uploads/{pdf_file.filename}"

    with open(file_path, "wb") as file:
       file.write(file_content) 

    extracted_text = extract_text_from_pdf(file_path)

    chunks = chunk_text(extracted_text)
    store_chunks_in_chroma(chunks, pdf_file.filename)
    return 0

def extract_text_from_pdf(file_path):
    pages = []
    
    with fitz.open(file_path) as pdf:
        for index, page in enumerate(pdf):
            page_text = {
                "page": index + 1,
                "text": page.get_text()
            }
            pages.append(page_text)

    return pages
