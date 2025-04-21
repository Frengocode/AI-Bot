from openai import AsyncOpenAI
import tempfile
from config.config import settings
import aiofiles

client = AsyncOpenAI(api_key=settings.OPEN_AI_KEY.get_secret_value())


async def speak_text(text: str) -> str:
    response = await client.audio.speech.create(
        model="tts-1", voice="nova", input=text, response_format="mp3"
    )
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    audio_data = await response.aread()
    async with aiofiles.open(temp_file.name, "wb") as out_file:
        await out_file.write(audio_data)
    return temp_file.name
