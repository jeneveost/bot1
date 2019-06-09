from typing import List

import telebot
from telebot.types import Message
import random

TOKEN = '812682071:AAEdrHVoch6Y0rUgA-zMrPAg7pjXfB2hCEM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Privet')


@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    bot.reply_to(message, message.text.upper())





bot.polling()
 