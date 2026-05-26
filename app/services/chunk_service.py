from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(pages):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=40, chunk_overlap=20
    )

    chunk_list = []

    for page in pages:
        chunks = splitter.split_text(page["text"])

        for chunk in chunks:
            chunk_list.append(
            {
                "chunk": chunk,
                "page": page["page"]
            }
        )
    return chunk_list