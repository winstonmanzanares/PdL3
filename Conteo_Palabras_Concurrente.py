import os
import multiprocessing as mp
import time
import logging

# Configuración medir tiempo ejecución
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger('mi-logger')



def count_words(filename, result_queue):
    inicio = time.time()
    with open(filename, 'r', encoding='utf-8') as archivos:
        contenido = archivos.read()

    palabras = contenido.split()
    result_queue.put((os.path.basename(filename), len(palabras)))
    fin = time.time()
    logger.debug(f"{os.path.basename(filename)}: count_words demoró {fin - inicio:.5f}s")

def procesar_archivos_count_words():
    directorio = "C:\\Users\\bsori\\OneDrive\\Escritorio\\Laboratorio 3 programación\\Directorio"
    
    contenido = os.listdir(directorio)
    archivos = [os.path.join(directorio, archivo) for archivo in contenido if os.path.isfile(os.path.join(directorio, archivo))]
    
    cola = mp.Queue()
    procesos = []

    for archivo in archivos:
        proceso = mp.Process(target=count_words, args=(archivo, cola))
        procesos.append(proceso)
        proceso.start()

    for proceso in procesos:
        proceso.join()

    total_palabras = 0
    print()
    while not cola.empty():
        nombre_archivo, cantidad = cola.get()
        print(f"{nombre_archivo}: {cantidad} palabras")
        total_palabras = total_palabras + cantidad
    print()
    print(f"Suma de palabras en todos los archivos es: {total_palabras}")



if __name__ == "__main__":
    procesar_archivos_count_words()
