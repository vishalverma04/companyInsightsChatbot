from langchain.prompts import ChatPromptTemplate


SYSTEM_PROMPT = (
"You are a helpful company insights assistant. Answer strictly based on the provided context.\n"
"- If the answer is not in the context, say: 'I could not find information about that in the company documents.'\n"
"- Be concise and cite sources at the end as [source-name or file][page if available]."
)


USER_PROMPT = (
"Question: {question}\n\n"
"Context:\n{context}\n\n"
"Return a clear answer followed by a short bullet list of sources."
)


prompt = ChatPromptTemplate.from_messages([
("system", SYSTEM_PROMPT),
("human", USER_PROMPT),
])