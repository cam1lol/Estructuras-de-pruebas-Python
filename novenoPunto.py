"""
Pregunta 9: Asincronía y Concurrencia

Compare asyncio (asincronía) y multiprocessing (paralelismo) en Python. ¿Cuándo
elegiría uno sobre el otro para optimizar un flujo de datos que consiste en:
a) Hacer 1000 peticiones HTTP a APIs externas.
b) Realizar cálculos intensivos de CPU sobre un gran conjunto de datos.
"""


# 1: Tareas I/O-bound -> asyncio

# Ideal para cosas que esperan respuesta externa (API, DB, archivos)
# Permite manejar muchas tareas al mismo tiempo sin bloquear

import asyncio
import aiohttp

urls = [f"https://api.ejemplo.com/dato/{i}" for i in range(1000)]

async def obtener_dato(session, url):
    async with session.get(url) as resp:
        return await resp.json()

async def main():
    async with aiohttp.ClientSession() as session:
        resultados = await asyncio.gather(*(obtener_dato(session, url) for url in urls))
    return resultados

# para ejecutar: 
asyncio.run(main())

# 2: Tareas CPU-bound -> multiprocessing

# Esto es ideal para calculos pesados, usa todos los nucleos del CPU
from multiprocessing import Pool

def calcular(x):
     # ejemplo de calculo pesado o que requieren mucho uso de la CPU
    resultado = 0
    # con esto relizamos muchas iteraciones para simular carga
    for i in range(1000):
        resultado += x ** 2 + i
    return resultado

# conjunto grande de datos
datos = range(1000000)

if __name__ == "__main__":
    with Pool() as pool:
        resultados = pool.map(calcular, datos)


# resumen final
# I/O-bound -> asyncio -> muchas solicitudes externas sin bloquear
# CPU-bound -> multiprocessing -> calculos intensivos aprovechando CPU