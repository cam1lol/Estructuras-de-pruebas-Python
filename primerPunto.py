"""
PREGUNTA 1 - Optimizacion y legibilidad
Codigo original (lo dejo comentado):
"""
# def procesar_datos_ineficiente(data):
#     resultado = []
#     for item in data:
#         if item > 10:
#             resultado.append(item * 2)
#     return resultado

# Instrucción: Optimice el código usando list comprehensions y mejore su legibilidad.
"""
Problema identificado:
Uso innecesario de un bucle explicito con append.
Puede simplificarse usando list comprehension, mejorando rendimiento y claridad.

La idea es hacer lo mismo pero más corto y fácil de leer.
Acá se puede usar una list comprehension para evitar el ciclo manual.
"""

def procesar_datos(data):
    # Retorna cada número mayor a 10 pero multiplicado por 2
    return [item * 2 for item in data if item > 10]


# Ejemplo rapido para probar
if __name__ == "__main__":
    datos = [5, 12, 3, 21]
    print(procesar_datos(datos))
    # Resultado esperado en consola: [24, 42]  
