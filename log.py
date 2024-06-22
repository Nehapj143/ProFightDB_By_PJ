# log.py
from telegram import Bot

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'
LOG_CHANNEL_ID = 'YOUR_LOG_CHANNEL_ID_HERE'

def log_message(message):
    bot = Bot(token=TOKEN)
    bot.send_message(chat_id=LOG_CHANNEL_ID, text=message)

if __name__ == '__main__':
    log_message("This is a test log message.")
