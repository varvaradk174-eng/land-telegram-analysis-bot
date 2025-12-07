import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "8097377946:AAG5iVXaYbUm2XdZpJOekV4Podt2UqSI0E8"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer("Бот работает!")

async def main():
    await dp.start_polling(bot)
