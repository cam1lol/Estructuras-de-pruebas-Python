"""
PREGUNTA 6 - Principios de Diseño (SOLID)
Explique brevemente los principios SOLID y mencione al menos un ejemplo de cómo aplicar el
Principio de Inversión de Dependencia (DIP) en un proyecto de automatización con Python (por
ejemplo, al cambiar de una base de datos local a una en la nube).

Los principios SOLID son basicamente una guía para que el codigo no se vuelva un caos con el tiempo. La idea es que el proyecto sea facil de entender y de modificar sin sufrir.

S   Single Responsibility: Cada clase debe hacer una sola cosa. Si una clase empieza a encargarse de mil cosas, después es un dolor cambiar algo porque se rompe todo.
O   Open/Closed: El código debería permitir añadir cosas nuevas sin tener que estar editando lo que ya funciona. Mejor agregar que estar dañando lo que ya está.
L   Liskov Substitution: Si una clase hereda de otra, debería poder reemplazarla sin que el programa se dañe. O sea, que las clases hijas se comporten bien.
I   Interface Segregation: Es mejor tener interfaces pequeñas y específicas. Tener una interfaz gigante obliga a implementar métodos que ni se van a usar y eso es incómodo.
D   Dependency Inversion: En vez de depender directamente de algo “concreto” (como una base de datos específica), es mejor depender de una interfaz. Así, si el día de mañana cambiamos la base de datos, no tenemos que reescribir todo.

Ejemplo sencillo para DIP:

Antes teníamos una clase que se conectaba directamente a una base de datos local. Si después queremos usar una base en la nube, toca meterse a cambiar código y eso no es muy práctico.

La solución es crear una interfaz para la conexión.
Entonces nuestro código usa esa interfaz y no le importa qué base de datos esté detrás.
Si cambiamos de local a nube, simplemente cambiamos la implementación, no la lógica.
"""

from abc import ABC, abstractmethod

# "Interfaz" o abstraccion
class RepositorioUsuarios(ABC):
    @abstractmethod
    def obtener_usuarios(self):
        pass

# Repo local
class RepositorioLocal(RepositorioUsuarios):
    def obtener_usuarios(self):
        return ["Juan", "Ana"]

# Repo remoto / nube
class RepositorioRemoto(RepositorioUsuarios):
    def obtener_usuarios(self):
        return ["Carlos", "Maria"]

# El servicio depende de la abstraccion, no de una BD especifica
class ServicioUsuario:
    def __init__(self, repo: RepositorioUsuarios):
        self.repo = repo

    def listar(self):
        return self.repo.obtener_usuarios()

# Ejemplo como usar:
local = ServicioUsuario(RepositorioLocal())
remoto = ServicioUsuario(RepositorioRemoto())

print(local.listar())
print(remoto.listar())

