from openai import AsyncOpenAI
from config.config import settings


client = AsyncOpenAI(api_key=settings.OPEN_AI_KEY.get_secret_value())


async def transcribe_audio(file_path: str) -> str:
    with open(file_path, "rb") as f:
        transcript = await client.audio.transcriptions.create(model="whisper-1", file=f)
    return transcript.text
