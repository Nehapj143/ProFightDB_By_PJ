import telebot
import wikipediaapi

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
    else:
        bot.reply_to(message, "Sorry, I couldn't find any information on that.")

# Polling mechanism to start listening for messages
bot.polling()
