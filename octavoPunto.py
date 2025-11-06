"""
Pregunta 8: Diseño de Microservicios y API REST

Al diseñar una API REST con Python (usando Flask o FastAPI) que servirá datos de un flujo,
¿cuáles son los códigos de estado HTTP más apropiados para indicar una solicitud exitosa de
creación de un recurso, una solicitud exitosa de lectura de un recurso y un error de validación
de datos por parte del cliente?

Respuesta_:
En esta pregunta hablamos de los codigos de estado HTTP que deberiamos usar
al crear una API REST en Python (Flask o FastAPI). La idea es mostrar cuales
codigos usar cuando:
1. Creamos un recurso correctamente
2. Leemos un recurso correctamente
3. Hay un error de validacion de datos del cliente
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modelo de datos simple
class Item(BaseModel):
    nombre: str
    precio: float

# Lista que simula la base de datos
items = []

# 1. Crear un recurso -> 201 Created
@app.post("/items/", status_code=201)
def crear_item(item: Item):
    # se agrega el item a la lista y devuelve el recurso
    items.append(item)
    return item

# 2. Leer un recurso -> 200 OK
@app.get("/items/{item_id}", status_code=200)
def obtener_item(item_id: int):
    # si el item existe lo retorna
    try:
        return items[item_id]
    except IndexError:
        # si no existe, manda 404
        raise HTTPException(status_code=404, detail="Item no encontrado")

# 3. Validacion de datos -> 400 Bad Request
@app.post("/items/validacion/")
def crear_item_seguro(item: Item):
    # vañlidar que el precio sea mayor a cero
    if item.precio <= 0:
        raise HTTPException(status_code=400, detail="El precio debe ser mayor a cero")
    items.append(item)
    return item

# resumen de codigos HTTP:
# 201 -> recurso creado
# 200 -> lectura exitosa
# 400 -> error en la info del cliente
# 404 -> recurso no encontrado