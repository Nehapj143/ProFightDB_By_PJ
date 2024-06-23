import telebot

# Initialize Telegram Bot
bot = telebot.TeleBot('7198911495:AAHrRwSFiu8l6ONgDbUXiVCdCJxXPeHNYCc')

# Log channel ID
LOG_CHANNEL_ID = '-1001329275814'  # Replace with your log channel username or ID

# Function to log messages to the log channel
def log_message(message):
    bot.send_message(LOG_CHANNEL_ID, message)
    
