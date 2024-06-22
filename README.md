# ProFightDB Telegram Bot

A Telegram bot that provides wrestler information from ProFightDB directly in your group chat.

## Features

- Search for wrestler information using their name.
- Retrieves wrestler biographies from ProFightDB.
- Logs user queries and bot responses to a dedicated channel.

## Requirements

- Python 3.6+
- `python-telegram-bot` library
- `requests` library
- `beautifulsoup4` library

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/ProFightDBTelegramBot.git
   cd ProFightDBTelegramBot
Install dependencies

bash
Copy code
pip install -r requirements.txt
Configure your Telegram Bot Token

Replace YOUR_TELEGRAM_BOT_TOKEN_HERE in bot.py and log.py with your actual Telegram bot token obtained from BotFather
Run the bot

bash
Copy code
python bot.py
Interact with the bot

Start your Telegram bot and use commands /start, /help, and /search wrestler_name in your group chat to interact with the bot.
Compliance

Respect ProFightDB's terms of service when scraping data. Ensure your bot's usage complies with legal and ethical standards
