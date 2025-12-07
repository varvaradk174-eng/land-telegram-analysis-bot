import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "ТВОЙ_ТОКЕН"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer("Бот работает!")

async def run_bot():
    await dp.start_polling(bot)
