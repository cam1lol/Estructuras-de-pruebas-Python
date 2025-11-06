"""
PREGUNTA 4 - Programación Orientada a Objetos (POO) y Responsabilidad Única

Instrucción:
Refactorice la clase para adherirse mejor al Principio de Responsabilidad Única (SRP).
Separe las responsabilidades.
"""

# Código original (lo dejo comentado):
# class ProcesadorDatos:
#     def __init__(self, datos):
#         self.datos = datos
#
#     def limpiar_y_guardar(self, nombre_archivo):
#         # Lógica de limpieza muy compleja
#         datos_limpios = [d for d in self.datos if d is not None]
#         # Lógica de guardado
#         with open(nombre_archivo, 'w') as f:
#             f.write(str(datos_limpios))
#         return "Guardado exitoso"

"""
Que se arregló:
La clase hacía dos cosas a la vez (limpiar y guardar). Separé esas responsabilidades
en clases mas pequeñas para que sea más facil cambiar o probar cada parte.
"""

class LimpiadorDatos:
    """Se encarga solo de limpiar/normalizar datos."""
    def limpiar(self, datos):
        # Aquí metes la lógica de limpieza (por ahora quitamos None)
        return [d for d in datos if d is not None]


class GuardadorDatos:
    """Se encarga solo de persistir los datos (a un archivo en este ejemplo)."""
    def guardar(self, datos, nombre_archivo):
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            f.write(str(datos))
        return "Guardado exitoso"


class ProcesadorDatos:
    """Orquesta el proceso: usa Limpiador y Guardador, pero no hace la lógica por sí mismo."""
    def __init__(self, datos):
        self.datos = datos
        self.limpiador = LimpiadorDatos()
        self.guardador = GuardadorDatos()

    def ejecutar(self, nombre_archivo):
        datos_limpios = self.limpiador.limpiar(self.datos)
        resultado = self.guardador.guardar(datos_limpios, nombre_archivo)
        return resultado


# Ejemplo para probar que funcione:
datos = [1, None, 2, None, 3]
p = ProcesadorDatos(datos)
print(p.ejecutar("resultado.txt"))
