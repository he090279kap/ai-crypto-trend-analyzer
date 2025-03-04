import telebot
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def send_report(message):
    bot.send_message(TELEGRAM_CHAT_ID, message)
