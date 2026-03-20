from pathlib import Path
import uuid
import chromadb
from openai import OpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from config import EMBED_MODEL, CHROMA_PATH, CHROMA_COLLECTION

client = OpenAI()
chroma = chromadb.PersistentClient(path=CHROMA_PATH)
collection = chroma.get_or_create_collection(name=CHROMA_COLLECTION)

def load_pdf_documents(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    return loader.load()

def split_documents(documents, chunk_size=500, chunk_overlap=75):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(documents)

def embed_texts(texts: list[str]):
    resp = client.embeddings.create(
        model=EMBED_MODEL,
        input=texts
    )
    return [item.embedding for item in resp.data]

def ingest_pdf(pdf_path: str, batch_size: int = 64):
    docs = load_pdf_documents(pdf_path)
    chunks = split_documents(docs)

    texts = [c.page_content for c in chunks]
    metadatas = [
        {
            "source": c.metadata.get("source", pdf_path),
            "page": int(c.metadata.get("page", -1))
        }
        for c in chunks
    ]
    ids = [str(uuid.uuid4()) for _ in chunks]

    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i+batch_size]
        batch_meta = metadatas[i:i+batch_size]
        batch_ids = ids[i:i+batch_size]
        batch_embeds = embed_texts(batch_texts)

        collection.add(
            documents=batch_texts,
            embeddings=batch_embeds,
            metadatas=batch_meta,
            ids=batch_ids
        )

    print(f"Ingested {len(chunks)} chunks from {pdf_path}")

if __name__ == "__main__":
    pdf = Path("data/raw/docs.pdf")
    ingest_pdf(str(pdf))
