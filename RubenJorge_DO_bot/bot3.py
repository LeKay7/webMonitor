import telebot
import requests
from botlib import check_service_web, check_port, check_code


# VARIABLES
token=input("Token del bot: ")
url=input("URL: ")
port=input("Puerto: ")
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

chatid="6647409382"
bot.send_message(chatid, mensaje)
bot.stop_polling()
