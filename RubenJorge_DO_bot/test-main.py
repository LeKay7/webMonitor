import telebot
import os
import bot3

# Configuración de Telegram
bot = telebot.TeleBot(os.environ.get("TELEGRAM_TOKEN"))

# Envío de mensaje a Telegram
chatid=os.environ.get("CHAT_ID")
mensaje="Se ha hecho un push"
bot.send_message(chatid, mensaje)
