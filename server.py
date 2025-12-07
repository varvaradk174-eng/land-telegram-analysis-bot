from flask import Flask
import os
import threading
import asyncio

# Импорт запуска бота
from bot import main as bot_main

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running!"

def start_bot():
    asyncio.run(bot_main())

if __name__ == "__main__":
    bot_thread = threading.Thread(target=start_bot)
    bot_thread.start()

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
