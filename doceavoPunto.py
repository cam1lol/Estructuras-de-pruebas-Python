"""
Pregunta 12: Integracion de Microservicios - Circuit Breaker

Explique que es el patron de diseño Circuit Breaker en el contexto de la integracion de
microservicios. Por que es crucial para la robustez de un flujo de datos que dependa de
servicios externos? Mencione si hay librerias en Python que faciliten su implementacion.
"""

# RESPUESTA:

# El patron Circuit Breaker se usa para evitar que un servicio siga intentando llamar
# a otro servicio externo que esta fallando constantemente. 
# La idea es como un interruptor electrico:
#   Si el servicio externo responde bien -> el circuito esta "cerrado" (todo funciona).
#   Si empieza a fallar muchas veces seguidas -> el circuito se "abre" y se corta la llamada.
#   Despues de un tiempo -> se prueba de nuevo (estado "half-open") para ver si ya se recupero.

# Este patron es clave para proteger el sistema, porque:
#   Evita que el flujo de datos se bloquee esperando respuestas que nunca llegan.
#   Reduce tiempos de espera innecesarios.
#   Evita sobrecargar servicios que ya estan fallando.
#   Mejora la resiliencia y la estabilidad general de la aplicacion.

# EJEMPLO SENCILLO DE USO EN PYTHON CON "pybreaker"
# (pybreaker es una libreria que implementa el patron Circuit Breaker)

import requests
import pybreaker

# Se define el Circuit Breaker
breaker = pybreaker.CircuitBreaker(
    # numero de fallos antes de "abrir" el circuito
    fail_max=3,  
    # tiempo para intentar reconectar        
    reset_timeout=10     
)

# Funcion que hace la llamada externa, protegida por el Circuit Breaker
@breaker
def llamar_servicio():
    r = requests.get("https://api.ejemplo.com/datos")
    return r.json()

try:
    data = llamar_servicio()
    print("Respuesta del servicio:", data)
except pybreaker.CircuitBreakerError:
    print("Circuito abierto: el servicio fallo demasiadas veces")
except Exception:
    print("Error inesperado en la llamada")
