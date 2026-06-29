import os
from groq import AsyncGroq

_client: AsyncGroq | None = None


def _get_client() -> AsyncGroq:
    global _client
    if _client is None:
        _client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))
    return _client

_SYSTEM_PROMPT = (
    "Ты умный и дружелюбный ассистент. "
    "Отвечай на том языке на котором задан вопрос. "
    "Будь краток и по делу."
)

_MODEL = "llama-3.1-8b-instant"


async def ask(messages: list[dict]) -> str:
    response = await _get_client().chat.completions.create(
        model=_MODEL,
        messages=[{"role": "system", "content": _SYSTEM_PROMPT}] + messages,
        max_tokens=1024,
        temperature=0.7,
    )
    return response.choices[0].message.content
