import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
EMBED_MODEL = os.getenv("RAG_EMBED_MODEL", "text-embedding-3-small")
CHAT_MODEL = os.getenv("RAG_CHAT_MODEL", "gpt-4o-mini")
CHROMA_PATH = os.getenv("CHROMA_PATH", "./data/chroma")
CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION", "rag_docs")

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is missing. Set it in environment or .env file.")
