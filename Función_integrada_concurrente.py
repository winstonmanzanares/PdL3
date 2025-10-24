import multiprocessing as mp
from sympy import symbols, integrate, sin, exp, log, sec 
import threading as th
import os
import time
import logging
from Conteo_Palabras_Concurrente import count_words
from ecuaciones_matematicas_concurrente import solve_equation


# Configuración para medir los tiempos de ejecución
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger('mi-logger')

    
# Función para resolver ecuaciones usando hilos
def thread_solve_equations(equations, result_pipe):
    threads = []
    for equation in equations:
        thread = th.Thread(target=solve_equation, args=(equation, result_pipe))
        threads.append(thread)
        thread.start()

    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()


if __name__ == "__main__":

    # Leer los archivos de texto del directorio de entrada y almacenar sus rutas en una lista.
    directorio = "C:\\Users\\bsori\\OneDrive\\Escritorio\\PdL3 Grupo_PdL3_F\\Directorio"
    
    contenido = os.listdir(directorio)
    archivos = [os.path.join(directorio, archivo) for archivo in contenido if os.path.isfile(os.path.join(directorio, archivo))]

    result_queue = mp.Queue()
    procesos = []
    
    # Parte 1: Iniciar el proceso process_count_words 
    # Iniciar procesos para cada archivo 
    for archivo in archivos:
        proceso = mp.Process(target=count_words, args=(archivo, result_queue))
        procesos.append(proceso)
        proceso.start()

    # Esperar a que todos los procesos terminen
    for proceso in procesos:
        proceso.join()

    # Recoger los resultados de la cola result_queue
    resultados_palabras = []
    while not result_queue.empty():
        nombre_archivo, cantidad = result_queue.get()
        resultados_palabras.append((nombre_archivo, cantidad))

   
    # Parte 2: Resolver ecuaciones
    # Leer las ecuaciones del archivo 'ecuaciones.txt' y almacenarlas en una lista
    contenido = os.listdir(directorio)
    archivo_ecuaciones = None
    for archivo in contenido:
        if archivo.endswith("ecuaciones.txt"):
            archivo_ecuaciones = os.path.join(directorio, archivo)
            break

    if archivo_ecuaciones is None:
        print("Error: No se encontró 'ecuaciones.txt' en el directorio especificado.")
        

    with open(archivo_ecuaciones, 'r') as f:
        equations = [line.strip() for line in f.readlines()]

    tuberia1, tuberia2 = mp.Pipe()


    thread_solve_equations(equations, tuberia2)

    #Recoger los resultados de las ecuaciones de la tubería result_pipe
    resultados_ecuaciones = []
    while tuberia1.poll():
        ecuacion, integral = tuberia1.recv()
        resultados_ecuaciones.append((ecuacion, integral))

 
    #Imprimir los resultados del conteo de palabras y las integrales de las ecuaciones.
    print()
    print("\n\033[1mResultados del conteo de palabras:\n\033[0m")
    for nombre_archivo, cantidad in resultados_palabras:
        print(f"{nombre_archivo}: {cantidad} palabras")



    print()
    print("\n\033[1mResultados de las integrales de las ecuaciones:\n\033[0m")

    
    for ecuacion, integral in resultados_ecuaciones:
        if "Error" in str(integral):
            print(f"Error al resolver la ecuación: {ecuacion}\n{integral}\n")
        else:
            print(f"La integral de la ecuación {ecuacion} es: {integral}\n")