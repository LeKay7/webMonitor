import telebot
import requests
import os
from botlib import check_service_web, check_port, check_code


# VARIABLES
token=os.environ.get("TELEGRAM_TOKEN")
url="https://web.telegram.org/"
port="443"
chatid=os.environ.get("CHAT_ID")
bot = telebot.TeleBot(token) 

# COMPRUEBA LA PAGINA WEB
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


bot.send_message(chatid, mensaje)
bot.stop_polling()
