import os;

from typing import List, AsyncGenerator
from openai import OpenAI

from ..types.ai_services import ChatMessage, AIService

OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY", "")
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=OPEN_ROUTER_API_KEY,
)

async def chat(messages: List[ChatMessage]) -> AsyncGenerator[str, None]:
    completion = client.chat.completions.create(
      model="openai/gpt-4o",
      messages=messages
    )

    answer = ""

    for chunk in completion:
        partial = await chunk.choices[0].delta.content or ""
        answer += partial

OpenAIService: AIService = {
    "name": "OpenAI",
    "chat": chat,
}