from typing import List, AsyncGenerator
from groq import Groq

from ..types.ai_services import ChatMessage, AIService

client = Groq()

async def chat(messages: List[ChatMessage]) -> AsyncGenerator[str, None]:
    completion = client.chat.completions.create(
        model="moonshotai/kimi-k2-instruct-0905",
        messages=messages,
        temperature=0.6,
        max_completion_tokens=4096,
        top_p=1,
        stream=True,
        stop=None,
    )

    answer = ""

    for chunk in completion:
        partial = await chunk.choices[0].delta.content or ""
        answer += partial

GroqService: AIService = {
    "name": "Groq",
    "chat": chat,
}
