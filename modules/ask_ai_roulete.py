from typing import List

from ..services.groq import GroqService
from ..services.open_ai import OpenAIService
from ..services.cerebras import CerebrasService

from ..types.ai_services import AIService

services: List[AIService] = [
  GroqService,
  CerebrasService,
  OpenAIService,
]

actual_service = 0

def getService() -> AIService: 
  service = services[actual_service]
  actual_service = (actual_service + 1) % len(services)
  return service;

async def Ask_AI(message: str): 
  service = getService()
  print(f"[DEBUG] Answering with { service.name }")

  answer = await service.chat([{
    "role": "user",
    "content": message
  }])

  return answer