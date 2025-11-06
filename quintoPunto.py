"""
PREGUNTA 5 - Seguridad y Validación de Entradas

Instrucción: Identifique la vulnerabilidad de seguridad (inyección de comandos) y proponga
una solución segura usando módulos estándar de Python, si es posible, o validando la entrada.
Codigo original (lo dejo comentado):
"""
# def ejecutar_comando_sistema(comando):
#     import os
#     # Suponemos que 'comando' viene de una entrada de usuario
#     os.system(f"echo {comando} >> log.txt")
#     return "Comando ejecutado"

"""
Problema:
    Usar os.system con texto que viene del usuario es inseguro porque se pueden inyectar comandos.
    Ej: si alguien mete 'hola; dir C:' o algo peor, el sistema lo ejecuta.
    
Solucion:
    En lugar de usar el shell, escribo directamente al archivo desde Python.
    Si necesito ejecutar comandos, solo permito algunos y los paso como lista
    para evitar shell injection.
"""

import subprocess

# Escribir en el archivo sin depender del shell
def safe_log_message(msg):
    if not isinstance(msg, str):
        raise ValueError("Mensaje inválido")
    # Con esto se evita saltos de linea para no romper la estructura del archivo
    msg = msg.replace("\r", "").replace("\n", " ")
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")

# Lista pequeña de comandos permitidos (Windows)
ALLOWED = {
    "whoami": ["whoami"],            
    "dir": ["cmd", "/c", "dir"]
}

def ejecutar_comando_simple(key, args=None):
    if key not in ALLOWED:
        raise ValueError("Comando no permitido")
    cmd = ALLOWED[key].copy()

    # Si hay argumentoss, se validan de forma basica
    if args:
        for a in args:
            if not isinstance(a, str) or len(a) > 100:
                raise ValueError("Argumento inválido")
            cmd.append(a)

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Fallo: {result.stderr.strip()}")
    return result.stdout.strip()

# Ejemplo para probar que funcione:
safe_log_message("Inicio de proceso")
print(ejecutar_comando_simple("whoami"))
