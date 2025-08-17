import os
from pydantic import BaseModel
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseModel):
# LLM
LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "openai")
OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama3:8b")


# Vector store
VECTORSTORE_KIND: str = os.getenv("VECTORSTORE_KIND", "chroma") # chroma | faiss
CHROMA_DIR: str = os.getenv("CHROMA_DIR", "./data/chroma")
FAISS_DIR: str = os.getenv("FAISS_DIR", "./data/faiss")


# Retrieval
TOP_K: int = int(os.getenv("TOP_K", "4"))
SCORE_THRESHOLD: float = float(os.getenv("SCORE_THRESHOLD", "0.0"))


# UI
APP_TITLE: str = os.getenv("APP_TITLE", "Company Insights Chatbot")


settings = Settings()