from typing import List, AsyncGenerator
from cerebras.cloud.sdk import Cerebras

from ..types.ai_services import ChatMessage, AIService

client = Cerebras()

async def chat(messages: List[ChatMessage]) -> AsyncGenerator[str, None]:
    stream = client.chat.completions.create(
        messages=messages,
        model="gpt-oss-120b",
        stream=True,
        max_completion_tokens=32768,
        temperature=1,
        top_p=1,
        reasoning_effort="medium"
    )

    answer = ""

    for chunk in stream:
        partial = await chunk.choices[0].delta.content or ""
        answer += partial

CerebrasService: AIService = {
    "name": "Cerebras",
    "chat": chat,
}
