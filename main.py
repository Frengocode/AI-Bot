import asyncio
from aiogram import Bot, Dispatcher
from config.config import settings
from handlers.voice_handler import router


async def main():
    bot = Bot(token=settings.BOT_TOKEN.get_secret_value())
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
