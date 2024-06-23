import telebot
import wikipediaapi
from log import log_message  # Import the log_message function from log.py
import requests

# Initialize Telegram Bot
bot = telebot.TeleBot('7198911495:AAHrRwSFiu8l6ONgDbUXiVCdCJxXPeHNYCc')

# Initialize Wikipedia API with user agent
wiki_wiki = wikipediaapi.Wikipedia(
    language='en',  # Adjust language as needed
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent="YourTelegramBot/1.0 (https://github.com/Nehapj143/ProFightDB_By_PJ)"
)

# Log channel ID
LOG_CHANNEL_ID = '@-1001329275814'  # Replace with your log channel username or ID

# Function to log messages to the log channel
def log_message(message):
    bot.send_message(LOG_CHANNEL_ID, message)

# Command handler for '/wiki' command
@bot.message_handler(commands=['wiki'])
def send_wikipedia_summary(message):
    query = message.text.split('/wiki ', 1)[1]  # Extract query from message
    try:
        page = wiki_wiki.page(query)
        if page.exists():
            summary = page.summary[:1000]  # Limit summary to 1000 characters
            bot.reply_to(message, summary)
            log_message(f"User {message.chat.username} queried '{query}'")  # Log the query
        else:
            bot.reply_to(message, "Sorry, I couldn't find any information on that.")
            log_message(f"User {message.chat.username} queried '{query}', but no information found")
    except requests.exceptions.HTTPError as e:
        bot.reply_to(message, f"Error: {str(e)}")
        log_message(f"HTTPError occurred: {str(e)}")

# Polling mechanism to start listening for messages
bot.polling()
