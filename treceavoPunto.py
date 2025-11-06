"""
Pregunta 13: Manejo Seguro de Credenciales

Ademas de usar variables de entorno, que otras tecnicas o herramientas (ej. Vaults o
Servicios de Secreto) se deben emplear para manejar credenciales sensibles (claves de API,
contraseñas de DB) en un entorno de produccion con Python, y por que las variables de
entorno por si solas podrian no ser suficientes?
"""

# RESPUESTA:

# Usar variables de entorno es una buena practica, pero no siempre es suficiente.
# En produccion, las variables de entorno pueden filtrarse:
#   En logs
#   En historiales de despliegue
#   En archivos docker-compose o scripts
#   O si alguien tiene acceso al servidor

# Por eso, en sistemas reales se usan servicios especializados para guardar secretos.
# Estos servicios permiten:
#   Guardar credenciales cifradas
#   Rotar claves automaticamente
#   Controlar quien puede leerlas
#   Registrar accesos (auditoria)

# Ejemplos de herramientas recomendadas:
# 1. HashiCorp Vault -> Manejo centralizado de secretos, muy usado en entornos grandes.
# 2. AWS Secrets Manager -> Guarda claves y las rota automaticamente.
# 3. Azure Key Vault -> Manejo de secretos en aplicaciones desplegadas en Azure.
# 4. Google Secret Manager -> Similar al de AWS pero en GCP.

# En Python, se pueden leer estos secretos usando sus SDK oficiales.

# EJEMPLO BASICO DE AWS SECRETS MANAGER:

import boto3
import json

cliente = boto3.client('secretsmanager', region_name='us-east-1')

nombre_secreto = "mi/base_de_datos"

respuesta = cliente.get_secret_value(SecretId=nombre_secreto)

secret_data = json.loads(respuesta['SecretString'])

usuario = secret_data["username"]
password = secret_data["password"]

print("Usuario:", usuario)
print("Password:", password)

# Ventaja: La credencial no esta en el codigo, no esta en variables de entorno, ni en texto plano.

