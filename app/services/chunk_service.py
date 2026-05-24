from langchain_text_splitters import RecursiveCharacterTextSplitter

async def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=40, chunk_overlap=20
    )

    chunks = splitter.split_text(text)
    return chunks
    