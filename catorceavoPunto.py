"""
Pregunta 14: Pruebas Unitarias y TDD

Defina la diferencia entre Mocks y Stubs en el contexto de pruebas unitarias. 
Si se esta probando un componente de un flujo de datos que llama a una API externa,
cual de los dos usaria para aislar la logica durante la prueba?
"""

# RESPUESTA:

# En pruebas unitarias, la idea es probar solo la logica propia del codigo, sin depender
# de servicios externos como APIs, bases de datos o archivos reales. 
# Para eso se usan objetos falsos que reemplazan esos recursos.

# STUBS:
# Un stub es un objeto "falso" muy simple que solo devuelve un valor fijo cuando se llama.
# No simula comportamiento, solo responde algo. 
# Se usa cuando solo se necesita un dato para que la funcion continue.
#
# Ejemplo: devolver un JSON fijo como si viniera de una API.

# MOCKS:
# Un mock es mas avanzado. Puede verificar:
#   si se llamo una funcion
#   cuantas veces se llamo
#   con que argumentos
# Ademas puede simular diferentes respuestas.
#
# Esto sirve para probar que el codigo llama a la API correctamente.

# RESPUESTA A LA PREGUNTA:
# Si estoy probando un componente que llama a una API externa, uso MOCK.
# Porque necesito asegurarme de:
#   que la funcion haga la llamada
#   que se llame con la URL correcta
#   que maneje respuestas o errores

# EJEMPLO USANDO MOCK:

from unittest.mock import patch
import requests

def obtener_dato():
    response = requests.get("https://api.ejemplo.com/data")
    return response.json()

# Test aislando la API usando mock:
@patch('requests.get')
def test_obtener_dato(mock_get):
    # Configurar respuesta falsa
    mock_get.return_value.json.return_value = {"status": "ok"}

    resultado = obtener_dato()

    # Verificar que el mock fue llamado (comportamiento de la misma)
    mock_get.assert_called_once()

    # Verificar resultado esperado
    assert resultado == {"status": "ok"}

    print("Test pasado correctamente")

#test de ejemplo:
test_obtener_dato()
