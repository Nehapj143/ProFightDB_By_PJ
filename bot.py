import logging
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
import requests
from bs4 import BeautifulSoup

# Telegram Bot Token
BOT_TOKEN = '7198911495:AAHrRwSFiu8l6ONgDbUXiVCdCJxXPeHNYCc'

# ProFightDB URL
PROFIGHTDB_URL = 'http://www.profightdb.com/'

# Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Function to scrape wrestler information from ProFightDB
def scrape_wrestler_info(name):
    url = f'{PROFIGHTDB_URL}wrestlers/{name.replace(" ", "-").lower()}.html'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        bio = soup.find('div', class_='bio').get_text(strip=True)  # Example: Scraping wrestler bio
        return bio
    else:
        return None

# Command handlers
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to ProFightDB Bot! Send /help for instructions.')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('You can search for wrestler information by sending their name.')

def search_wrestler(update: Update, context: CallbackContext) -> None:
    query = update.message.text.replace('/search ', '').strip()
    info = scrape_wrestler_info(query)
    if info:
        update.message.reply_text(info, parse_mode=ParseMode.HTML)
        # Log search query and result to a dedicated log channel
        log_channel_id = 'YOUR_LOG_CHANNEL_ID_HERE'
        context.bot.send_message(log_channel_id, f"User searched for wrestler: {query}\nResult: {info}")
    else:
        update.message.reply_text(f"Sorry, no information found for wrestler: {query}")

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.command & Filters.regex('^/search'), search_wrestler))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
