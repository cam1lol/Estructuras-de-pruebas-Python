"""
PREGUNTA 3 - Integración con API y Hardcoding

Código original (lo dejo comentado):
"""
# import requests
# def obtener_datos_api():
#     url = "http://api.ejemplo.com/v1/usuarios?key=MI_CLAVE_SECRETA_12345"
#     response = requests.get(url)
#     return response.json()

# Instrucción: Corrija el código para evitar el hardcoding de la URL base y, más importante, de la
# clave secreta de la API. ¿Qué buenas prácticas de configuración se deben usar?
"""
Problema:
En el código original la URL y la clave están escritas directamente, lo cual es mala práctica.
Lo mejor es usar variables de entorno para no exponer datos sensibles.
Además, agrego un tiempo de espera y manejo de errores básico.
"""

import os
import requests

def obtener_datos_api(recurso="usuarios", params=None):
    """
    Carga la URL base y la clave desde variables de entorno.
    De esta forma la clave no queda en el código.
    """
    base_url = os.getenv("API_BASE_URL")
    api_key = os.getenv("API_KEY")

    if not base_url or not api_key:
        raise RuntimeError("Faltan las variables API_BASE_URL o API_KEY en el entorno.")

    url = f"{base_url}/v1/{recurso}"
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        resp = requests.get(url, headers=headers, params=params, timeout=10)
        resp.raise_for_status()  # Lanza error si la API responde mal
        return resp.json()
    except requests.exceptions.RequestException as e:
        # Aquí solo devuelvo el error. En un proyecto real sería mejor loguearlo.
        raise RuntimeError(f"Error al consultar la API: {e}")

# Ejemplo para probar (solo si ya se configuraron las variables de entorno):
# print(obtener_datos_api())

"""
Cómo preparar las variables de entorno:

Windows (CMD):
    set API_BASE_URL=https://api.ejemplo.com
    set API_KEY=MI_CLAVE_SECRETA_12345

PowerShell:
    $env:API_BASE_URL = "https://api.ejemplo.com"
    $env:API_KEY = "MI_CLAVE_SECRETA_12345"

Notas:
- Usé el header Authorization porque es mas seguro que mandar la clave en la URL.
- Agregar timeout evita que el programa se quede esperando indefinidamente.
"""
