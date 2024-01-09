import telebot
import requests
import sys
from botlib import check_service_web, check_port, check_code

# VARIABLES
token="6960071430:AAGltCpYSW5xxJA6htqe2ty8efNu0XZB8Nk"
url="https://web.telegram.org/"
port="443"
bot = telebot.TeleBot(token) 

# COMANDO TELEGRAM
@bot.message_handler(commands=["start"])

# COMPRUEBA LA PAGINA WEB
def comprobar(message):
    servicio_responde = check_service_web(url)
    puerto_responde = check_port(url, port)
    codigo_200OK = check_code(url)

    if servicio_responde and puerto_responde:
        mensaje = "El servicio web responde correctamente"
        
    elif servicio_responde:
        mensaje = "El servicio web responde pero el puerto está cerrado"
       
    elif codigo_200OK:
        mensaje = "El codigo es distinto a 200"
        
    else:
        mensaje = "El servicio web no responde"
        
    bot.send_message(message.chat.id, mensaje)

bot.polling()
