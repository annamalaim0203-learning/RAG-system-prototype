import chromadb
from openai import OpenAI
from config import EMBED_MODEL, CHROMA_PATH, CHROMA_COLLECTION

client = OpenAI()
chroma = chromadb.PersistentClient(path=CHROMA_PATH)
collection = chroma.get_or_create_collection(name=CHROMA_COLLECTION)

def embed_query(query: str):
    resp = client.embeddings.create(model=EMBED_MODEL, input=query)
    return resp.data[0].embedding

def retrieve(query: str, candidate_k: int = 20, top_k: int = 5):
    q_emb = embed_query(query)
    results = collection.query(
        query_embeddings=[q_emb],
        n_results=candidate_k
    )

    docs = results.get("documents", [[]])[0][:top_k]
    metas = results.get("metadatas", [[]])[0][:top_k]
    dists = results.get("distances", [[]])[0][:top_k]
    return docs, metas, dists
