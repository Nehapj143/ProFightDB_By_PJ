import telebot
import wikipediaapi
from log import log_message  # Import the log_message function from log.py

# Initialize Telegram Bot
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

# Initialize Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia('en')  # Adjust language as needed

# Command handler for '/wiki' command
@bot.message_handler(commands=['wiki'])
def send_wikipedia_summary(message):
    query = message.text.split('/wiki ', 1)[1]  # Extract query from message
    page = wiki_wiki.page(query)
    if page.exists():
        summary = page.summary[:1000]  # Limit summary to 1000 characters
        bot.reply_to(message, summary)
        log_message(f"User {message.chat.username} queried '{query}'")  # Log the query
    else:
        bot.reply_to(message, "Sorry, I couldn't find any information on that.")
        log_message(f"User {message.chat.username} queried '{query}', but no information found")

# Polling mechanism to start listening for messages
bot.polling()
