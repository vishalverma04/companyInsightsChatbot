from typing import List, Tuple


# Simple in-memory chat history container for Streamlit session state


class ChatMemory:
def __init__(self):
self.history: List[Tuple[str, str]] = [] # list of (user, assistant)


def add(self, user: str, assistant: str):
self.history.append((user, assistant))


def as_langchain(self) -> List[Tuple[str, str]]:
return self.history


def clear(self):
self.history.clear()