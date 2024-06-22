# log.py
from telegram import Bot

BOT_TOKEN = '7198911495:AAHrRwSFiu8l6ONgDbUXiVCdCJxXPeHNYCc'
LOG_CHANNEL_ID = '-1001329275814'

def log_message(message):
    bot = Bot(token=TOKEN)
    bot.send_message(chat_id=LOG_CHANNEL_ID, text=message)

if __name__ == '__main__':
    log_message("This is a test log message.")
