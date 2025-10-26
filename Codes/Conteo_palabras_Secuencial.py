import os
import time
import logging

# Configuración del logger (para registrar tiempos)
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger('mi-logger')

def count_words(filename):
    """Cuenta las palabras de un archivo de forma secuencial."""
    inicio = time.time()
    with open(filename, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    palabras = contenido.split()
    fin = time.time()
    logger.debug(f"count_words de: {os.path.basename(filename)} demoró {fin - inicio:.5f}s")
    return os.path.basename(filename), len(palabras)



########################################################################
# Bloque de funciones similares a las originales pero sin el datalogger

def silcount_words(filename):
    """Silenciosamente cuenta las palabras, sin el logger"""
    with open(filename, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    palabras = contenido.split()
    return os.path.basename(filename), len(palabras)

def procSecTime():
    # Función interna que simplemente devuelve el tiempo de procesamiento como un float
    directorio = os.getcwd()  # Usa el directorio actual
    archivos = [os.path.join(directorio, f) for f in os.listdir(directorio) if f.endswith('.txt') and 'ecuaciones' not in f]

    total_palabras = 0
    inicio_total = time.time()

    for archivo in archivos:
        nombre_archivo, cantidad = silcount_words(archivo)
        total_palabras += cantidad

    fin_total = time.time()
    return fin_total - inicio_total
    

########################################################################




def procesar_secuencial():
    """Procesa todos los archivos del directorio de forma secuencial."""
    directorio = os.getcwd()  # Usa el directorio actual
    archivos = [os.path.join(directorio, f) for f in os.listdir(directorio) if f.endswith('.txt') and 'ecuaciones' not in f]

    total_palabras = 0
    inicio_total = time.time()
    print("\nConteo de palabras secuencial:\n")

    for archivo in archivos:
        nombre_archivo, cantidad = count_words(archivo)
        print(f"   {nombre_archivo}: {cantidad} palabras")
        total_palabras += cantidad

    fin_total = time.time()
    print(f"\nTotal de palabras en todos los archivos: {total_palabras}")
    print(f"Tiempo total secuencial: {fin_total - inicio_total:.5f} s\n")

if __name__ == "__main__":
    procesar_secuencial()
