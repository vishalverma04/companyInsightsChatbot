import streamlit as st
from rag.chain import build_qa_chain
from rag.memory import ChatMemory
from rag.config import settings


st.set_page_config(page_title=settings.APP_TITLE, page_icon="💼")
st.title(settings.APP_TITLE)


if "memory" not in st.session_state:
st.session_state.memory = ChatMemory()
if "chain" not in st.session_state:
st.session_state.chain = build_qa_chain()


col1, col2 = st.columns([1,1])
with col1:
if st.button("🔄 Clear chat"):
st.session_state.memory.clear()
st.toast("Chat cleared")
with col2:
st.caption(f"VectorStore: **{settings.VECTORSTORE_KIND}** | k={settings.TOP_K}")


# Render chat history
for u, a in st.session_state.memory.history:
with st.chat_message("user"):
st.markdown(u)
with st.chat_message("assistant"):
st.markdown(a)


# Chat input
user_q = st.chat_input("Ask a question about the company…")
if user_q:
with st.chat_message("user"):
st.markdown(user_q)


with st.chat_message("assistant"):
with st.spinner("Thinking…"):
result = st.session_state.chain({"question": user_q})
answer = result["answer"]
sources = result["sources"]
st.markdown(answer)
if sources:
with st.expander("Sources"):
for i, s in enumerate(sources, 1):
src = s.get("source", "unknown")
page = s.get("page")
st.markdown(f"{i}. `{src}`{f' · p.{page}' if page is not None else ''}")


st.session_state.memory.add(user_q, answer)