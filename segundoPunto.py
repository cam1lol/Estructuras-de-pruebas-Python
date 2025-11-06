"""
PREGUNTA 2 - Manejo de Recursos y Excepciones
Codigo original (lo dejo comentado):
"""
# def leer_archivo_inseguro(nombre_archivo):
#     f = open(nombre_archivo, 'r')
#     datos = f.read()
#     # Si algo falla, el archivo queda abierto y eso no es bueno
#     f.close()
#     return datos

# Instrucción: Corrija el código para asegurar que el archivo se cierre siempre, incluso si ocurre
# una excepción.
"""
Para evitar olvidarnos de cerrar el archivo, usamos 'with'.
Con 'with' el archivo se cierra solo, pase lo que pase.
"""

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        return f.read()


# Ejemplo opcional:
# print(leer_archivo("datos.txt"))
