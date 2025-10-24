import os
import time
import logging


logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger('mi-logger')


def count_words(filename):
    inicio = time.time()
    
    # Leer el contenido del archivo
    with open(filename, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    palabras = contenido.split()
    fin = time.time()
    
    print()
    logger.debug(f"count_words de:{os.path.basename(filename)} demoró {fin - inicio:.5f}s")
    

    return os.path.basename(filename), len(palabras)



#Procesar los archivos y contar las palabras de forma secuencial

directorio = "C:\\Users\\bsori\\OneDrive\\Escritorio\\Laboratorio 3 programación\\Directorio"
    
# Obtener la lista de archivos en el directorio
contenido = os.listdir(directorio)
archivos = [os.path.join(directorio, archivo) for archivo in contenido if os.path.isfile(os.path.join(directorio, archivo))]

total_palabras = 0
print()
    
# Procesar cada archivo uno por uno (secuencialmente)
for archivo in archivos:
    nombre_archivo, cantidad = count_words(archivo)
    print(f"{nombre_archivo}: {cantidad} palabras")
    total_palabras = total_palabras + cantidad

print()
print(f"La suma de palabras de todos los archivos es: {total_palabras}")

