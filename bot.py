from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

TOKEN = "8743209881:AAExVJWxHQc6vUtOkEHMU2c8K9YxicJidho"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я твой бот на aiogram 3.x")

# Основная функция запуска
async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())