import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Здравствуйте! Я ваш помощник магазина. Задайте вопрос 😊")

@bot.message_handler(func=lambda x: True)
def answer(message):
    bot.reply_to(message, "Спасибо за вопрос! Я пока тестовый бот и скоро научусь анализировать ваш шоп ❤️")

def run_bot():
    bot.polling(none_stop=True)
