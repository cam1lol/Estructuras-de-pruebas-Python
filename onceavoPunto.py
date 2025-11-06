"""
Pregunta 11: Patrones de Flujo de Datos

Describa la diferencia entre los patrones Push y Pull en el diseño de flujos de datos y
automatizaciones. Proporcione un ejemplo de un caso de uso en Python para cada uno (ej.
integración con Message Queues vs. Polling a una API).
"""

# RESPUESTA:

# Push:
# Los datos se envIan automAticamente desde el origen hacia el consumidor.
# El consumidor no tiene que preguntar, solo recibe los datos cuando llegan.
# Es muy usado en Message Queues, Webhooks o sistemas de streaming.

# Pull
# El consumidor pregunta activamente al origen si hay datos nuevos.
# El flujo depende de consultas periodicas o “polling”.
# Es muy usado cuando no hay notificaciones automaticas o el origen no puede enviar datos.

# EJEMPLOS: 

# 1: Patrón Push (Message Queue con RabbitMQ como ejemplo)

# Simulacion usando un push usando pika (RabbitMQ)

import pika

# Conexion al broker
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='tareas')

# Publicar mensaje (push)
channel.basic_publish(exchange='',
                      routing_key='tareas',
                      body='Procesar dato importante')
print(" [x] Mensaje enviado")
connection.close()

# 2: Patron Pull (Polling a una API externa)
import requests
import time

url = "https://api.ejemplo.com/datos"

while True:
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        data = respuesta.json()
        print("Datos obtenidos:", data)
    else:
        print("Error en la solicitud:", respuesta.status_code)

    # esto consulta cada 60 segundos
    time.sleep(60)  