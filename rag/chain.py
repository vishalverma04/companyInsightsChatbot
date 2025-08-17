from __future__ import annotations
from typing import Dict
from rag.prompts import prompt
from rag.retriever import get_retriever
from rag.config import settings


# LLMs
from langchain_openai import ChatOpenAI
# If using Ollama locally, uncomment the next line and the code inside build_qa_chain
# from langchain_ollama import ChatOllama


from langchain.schema import Document




def format_docs(docs: list[Document]) -> str:
blocks = []
for d in docs:
source = d.metadata.get("source") or d.metadata.get("file_path") or "unknown"
page = d.metadata.get("page")
src_str = f"[source: {source}{f' p.{page}' if page is not None else ''}]"
blocks.append(f"{d.page_content}\n{src_str}")
return "\n\n---\n\n".join(blocks)




def build_llm():
provider = settings.LLM_PROVIDER.lower()
if provider == "openai":
return ChatOpenAI(model=settings.OPENAI_MODEL, temperature=0)
elif provider == "ollama":
# return ChatOllama(model=settings.OLLAMA_MODEL, temperature=0)
raise ValueError("Ollama path commented out; enable ChatOllama import and return above.")
else:
raise ValueError(f"Unsupported LLM_PROVIDER: {settings.LLM_PROVIDER}")




def build_qa_chain():
retriever = get_retriever()
llm = build_llm()


# LCEL runnable: {"question"} -> retrieve -> prompt -> llm
def run(payload: Dict[str, str]):
question = payload["question"]
docs = retriever.get_relevant_documents(question)
context = format_docs(docs)
# Build prompt
messages = prompt.format_messages(question=question, context=context)
result = llm.invoke(messages)
# Package response and sources
sources = []
for d in docs:
src = d.metadata.get("source") or d.metadata.get("file_path") or "unknown"
page = d.metadata.get("page")
sources.append({"source": src, "page": page})
return {
"answer": result.content,
"sources": sources,
}


return run