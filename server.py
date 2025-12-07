from flask import Flask
import threading
from bot import run_bot

app = Flask(__name__)

@app.get("/")
def home():
    return "Bot is running!"

# Запускаем бота в отдельном потоке
def start_bot():
    run_bot()

bot_thread = threading.Thread(target=start_bot)
bot_thread.daemon = True
bot_thread.start()
