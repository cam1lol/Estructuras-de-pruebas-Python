"""
Pregunta 15: Inmutabilidad de Datos y Tipado

En Python, el uso de Type Hinting (anotaciones de tipo) y tipos de datos inmutables 
(como tuples o frozensets) es una buena practica. Como contribuyen estas dos practicas 
a la seguridad y mantenibilidad de grandes flujos de procesamiento de datos?
"""

# RESPUESTA:

# El type hinting permite indicar el tipo de datos esperado en funciones y variables.
# Esto ayuda a evitar errores, hace el codigo mas claro y facilita el mantenimiento,
# especialmente cuando varias personas trabajan en el mismo proyecto.

# Por otro lado, el uso de tipos inmutables como tuple o frozenset asegura que los datos
# no cambien por accidente durante su procesamiento, lo cual es clave cuando se manejan
# flujos grandes o concurrencia.

# En resumen:
# Type hinting = menos errores y codigo mas claro.
# Inmutabilidad = datos mas seguros y estables.
# Ambas practicas hacen el sistema mas facil de mantener y menos propenso a fallos.


# Ejemplo simple de type hinting:
def sumar(a: int, b: int) -> int:
    return a + b

# Ejemplo de mutable vs inmutable:

# mutable (puede cambiar)
lista = [1, 2, 3]  

# inmutable (no puede cambiar)
tupla = (1, 2, 3)   

# Ejemplo combinando ambos:
from typing import Tuple

def procesar_registro(registro: Tuple[str, int]) -> str:
    nombre, edad = registro
    return f"Usuario {nombre} tiene {edad} anos"

print(procesar_registro(("Juan", 25)))
