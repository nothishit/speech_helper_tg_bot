import asyncio, os
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from app.handlers import router
from app.callbacks import call_router
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()

async def main():
    dp.include_router(router)
    dp.include_router(call_router)
    dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("info", "Информация о методах перевода речи в текст"),
        types.BotCommand("change", "Изменить метод перевода речи в текст"),
    ])
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")