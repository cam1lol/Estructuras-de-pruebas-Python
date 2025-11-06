"""
PREGUNTA 7 - Entornos Virtuales y Dependencias

¿Cuál es la importancia de usar entornos virtuales (venv o conda) y un archivo
requirements.txt o pyproject.toml en un proyecto de Python, especialmente en un
contexto de despliegue (DevOps)?
"""

"""
Respuesta:

Un entorno virtual basicamente sirve para que cada proyecto tenga sus propias librerías,
sin afectar o dañar otros proyectos en el mismo equipo. Es como tener una “cajita” con
solo lo necesario para ese proyecto.

Ventajas:
    Evita conflictos de versiones entre proyectos.
    Hace más facil mover el proyecto de una maquina a otra.
    Asegura que todos trabajen con las mismas dependencias.

El archivo requirements.txt guarda la lista de librerias que usa el proyecto.
En despliegue (DevOps), simplemente se instala con:

    pip install -r requirements.txt

y listo, el ambiente queda igual al del desarrollo.
"""

# Ejemplo de como crear y activar un entorno virtual en Windows:

# Crear el entorno:
#   python -m venv venv

# Activar:
#   venv\Scripts\activate

# Instalar dependencias:
#   pip install requests

# Guardar dependencias en requirements.txt:
#   pip freeze > requirements.txt
