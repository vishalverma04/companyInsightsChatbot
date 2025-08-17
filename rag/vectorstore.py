from __future__ import annotations
from typing import Literal
from langchain_community.vectorstores import Chroma, FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings as OpenAIEmbeddingsNew


# You can swap in a different embedding model here if needed (e.g., SentenceTransformers)


def load_embeddings(provider: Literal["openai"] = "openai"):
# langchain-openai package provides OpenAIEmbeddingsNew (new shim)
# fallback to community if needed
try:
return OpenAIEmbeddingsNew()
except Exception:
return OpenAIEmbeddings()




def load_chroma(persist_dir: str):
embeddings = load_embeddings()
vs = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
return vs




def load_faiss(index_dir: str):
embeddings = load_embeddings()
vs = FAISS.load_local(index_dir, embeddings, allow_dangerous_deserialization=True)
return vs