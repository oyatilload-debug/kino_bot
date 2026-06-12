import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import os

# Render'dagi Environment dan tokenni oladi
TOKEN = os.environ.get("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Assalomu alaykum! Bot muvaffaqiyatli ishga tushdi.")

async def main():
    print("Bot ishga tushmoqda...")
    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())
