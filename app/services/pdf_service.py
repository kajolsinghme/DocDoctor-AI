import fitz

async def upload_pdf_service(pdf_file):
    file_content = await pdf_file.read()
    file_path = f"uploads/{pdf_file.filename}"

    with open(file_path, "wb") as file:
       file.write(file_content) 

    extracted_text = extract_text_from_pdf(file_path)

    return extracted_text

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
