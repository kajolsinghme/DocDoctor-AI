from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(pages):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200
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