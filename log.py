import telebot

# Initialize Telegram Bot
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

# Log channel ID
LOG_CHANNEL_ID = '@your_log_channel_username'  # Replace with your log channel username or ID

# Function to log messages to the log channel
def log_message(message):
    bot.send_message(LOG_CHANNEL_ID, message)
