import telebot
import requests

# COMPRUEBA SI EL SERVICIO WEB ESTA DISPONIBLE
def check_service_web(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False

# COMPRUEBA SI EL PUERTO ESTA ABIERTO
def check_port(url, port):
    try:
        response = requests.get(f"{url}:{port}")
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False

# COMPRUEBA SI EL CODIGO DE RESPUESTA ES 200
def check_code(url):
    try:
        response = requests.get(url)
        return response.status_code != 200
    except requests.exceptions.ConnectionError:
        return False
    