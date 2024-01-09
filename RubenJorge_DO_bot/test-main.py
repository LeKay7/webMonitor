import telebot
import bot3

# Configuración de Telegram
bot = telebot.TeleBot("6960071430:AAGltCpYSW5xxJA6htqe2ty8efNu0XZB8Nk")

# Envío de mensaje a Telegram
chatid="6647409382"
mensaje="Se ha hecho un push"
bot.send_message(chatid, mensaje)