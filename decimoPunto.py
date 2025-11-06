"""
Pregunta 10: Logging y Trazabilidad

Describa las buenas prácticas para implementar logging en una solución de automatización.
Mencione al menos tres niveles de log que se deben usar y un ejemplo de cuándo usaría cada
uno.
"""
# RESPUESTA:
# En Python, el modulo logging es el estandar para registrar eventos en los programas. 
# Implementar logging correctamente ayuda a: depurar errores, monitorear procesos de produccion y mantener trazabilidad
# de lo que sucede en el sistema

# Ejemplos de buenas practicas:
# No usar print para logging en produccion: Solo para pruebas rápidas.
# Configurar niveles de log: Para diferenciar severidad (INFO, WARNING, ERROR, etc.)
# Usar archivos de log rotativos: Evita que los logs crezcan demasiado
# Incluir timestamps y contexto: Fecha, hora, módulo o función donde ocurre el evento
# No loggear información sensible: Como contraseñas o claves

# Niveles de Log recomendados:
# INFO: para confirmar que todo funciona correctamente
# WARNING: para problemas potenciales
# ERROR: para funciones que fallaron 
# CRITICAL: para errores graves que pueden detener la aplicacion

# Ejemplo en codigo>:
import logging

# configuracion basica del logger
logging.basicConfig(
    filename='mi_app.log',
    level=logging.INFO,  # nivel minimo que se registrara
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ejemplo de logs
logging.info("La aplicacion inicio correctamente")
logging.warning("No se encontro el archivo de configuracion, usando valores por defecto")
logging.error("Error al conectar con la base de datos")
logging.critical("Error con el programa, puede hacer que el programa se detenga ")
