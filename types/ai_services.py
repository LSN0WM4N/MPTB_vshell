from typing import Any, TypedDict

class ChatMessage(TypedDict):
    role: str
    content: str


class AIService(TypedDict):
    name: str
    chat: Any