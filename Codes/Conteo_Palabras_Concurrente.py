import os
import multiprocessing as mp
import time
import logging

# Configuración del logger
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger('mi-logger')

def count_words(filename, result_queue):
    """Función ejecutada por cada proceso para contar palabras."""
    inicio = time.time()
    with open(filename, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    palabras = contenido.split()
    fin = time.time()
    result_queue.put((os.path.basename(filename), len(palabras), fin - inicio))
    logger.debug(f"{os.path.basename(filename)}: count_words demoró {fin - inicio:.5f}s")



########################################################################
# Bloque de funciones similares a las originales pero sin el datalogger

def silcount_words(filename, result_queue):
    """Función ejecutada por cada proceso para contar palabras."""
    inicio = time.time()
    with open(filename, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    palabras = contenido.split()
    fin = time.time()
    result_queue.put((os.path.basename(filename), len(palabras), fin - inicio))

def procConcTime():
    directorio = os.getcwd()
    archivos = [os.path.join(directorio, f) for f in os.listdir(directorio) if f.endswith('.txt') and 'ecuaciones' not in f]

    cola = mp.Queue()
    procesos = []

    inicio_total = time.time()
    for archivo in archivos:
        proceso = mp.Process(target=silcount_words, args=(archivo, cola))
        procesos.append(proceso)
        proceso.start()

    for proceso in procesos:
        proceso.join()
    fin_total = time.time()
    total_palabras = 0
    while not cola.empty():
        nombre_archivo, cantidad, tiempo_proc = cola.get()
        total_palabras += cantidad

    return fin_total - inicio_total 


########################################################################





def procesar_concurrente():
    """Procesa los archivos usando varios procesos concurrentes."""
    directorio = os.getcwd()
    archivos = [os.path.join(directorio, f) for f in os.listdir(directorio) if f.endswith('.txt') and 'ecuaciones' not in f]

    cola = mp.Queue()
    procesos = []

    inicio_total = time.time()
    for archivo in archivos:
        proceso = mp.Process(target=count_words, args=(archivo, cola))
        procesos.append(proceso)
        proceso.start()

    for proceso in procesos:
        proceso.join()
    fin_total = time.time()

    print("\nConteo de palabras concurrente:\n")
    total_palabras = 0
    while not cola.empty():
        nombre_archivo, cantidad, tiempo_proc = cola.get()
        print(f"{nombre_archivo}: {cantidad} palabras (tardó {tiempo_proc:.5f} s)")
        total_palabras += cantidad

    print(f"\nTotal palabras: {total_palabras}")
    print(f"Tiempo total concurrente: {fin_total - inicio_total:.5f} s\n")

if __name__ == "__main__":
    procesar_concurrente()
