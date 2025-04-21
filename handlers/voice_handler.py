from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart
from services.whisper import transcribe_audio
from services.assistant import get_assistant_response
from services.tts import speak_text
import tempfile

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("🎤 Отправь голосовое сообщение — я отвечу голосом!")


@router.message(F.voice)
async def handle_voice(message: Message):

    file = await message.bot.get_file(message.voice.file_id)
    voice_bytes = await message.bot.download_file(file.file_path)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".ogg") as tmp:
        tmp.write(voice_bytes.read())
        tmp_path = tmp.name

    text = await transcribe_audio(tmp_path)

    reply = await get_assistant_response(text)

    audio_path = await speak_text(reply)

    audio = FSInputFile(audio_path)

    await message.answer_voice(voice=audio, caption="Ответ")
