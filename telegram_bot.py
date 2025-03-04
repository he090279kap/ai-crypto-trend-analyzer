import telebot
import matplotlib.pyplot as plt
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def send_report(message):
    """Отправляет отчёт в Telegram."""
    bot.send_message(TELEGRAM_CHAT_ID, message)
