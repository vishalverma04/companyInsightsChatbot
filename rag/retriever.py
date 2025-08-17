from __future__ import annotations
from langchain.schema import BaseRetriever
from rag.config import settings
from rag.vectorstore import load_chroma, load_faiss




def get_retriever() -> BaseRetriever:
kind = settings.VECTORSTORE_KIND.lower()
if kind == "chroma":
vs = load_chroma(settings.CHROMA_DIR)
elif kind == "faiss":
vs = load_faiss(settings.FAISS_DIR)
else:
raise ValueError(f"Unsupported VECTORSTORE_KIND: {settings.VECTORSTORE_KIND}")


retriever = vs.as_retriever(search_kwargs={
"k": settings.TOP_K,
})
return retriever