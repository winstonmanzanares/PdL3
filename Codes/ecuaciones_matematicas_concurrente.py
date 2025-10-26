import multiprocessing as mp
from sympy import symbols, integrate, sin, exp, log, sec
import threading as th, time, logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger('mi-logger')

def solve_equation(equation, result_pipe):
    """Resuelve una integral simbólica en un hilo y envía el resultado por una tubería."""
    x, a, b = symbols('x a b')
    try:
        inicio = time.time()
        equation = equation.replace('^', '**')
        resultado = integrate(eval(equation), x)
        fin = time.time()
        tiempo = fin - inicio
        result_pipe.send((equation, resultado, tiempo))
        logger.debug(f"Integral {equation} calculada en {tiempo:.5f}s")
    except Exception as e:
        result_pipe.send((equation, f"Error: {str(e)}", 0))

def thread_solve_equations(equations, result_pipe):
    """Crea un hilo por cada ecuación y espera a que terminen."""
    threads = []
    for ecuacion in equations:
        thread = th.Thread(target=solve_equation, args=(ecuacion, result_pipe))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()






########################################################################
# Bloque de funciones similares a las originales pero sin el datalogger

def silsolve_equation(equation, result_pipe):
    """Resuelve una integral simbólica en un hilo y envía el resultado por una tubería."""
    x, a, b = symbols('x a b')
    try:
        inicio = time.time()
        equation = equation.replace('^', '**')
        resultado = integrate(eval(equation), x)
        fin = time.time()
        tiempo = fin - inicio
        result_pipe.send((equation, resultado, tiempo))
        #logger.debug(f"Integral {equation} calculada en {tiempo:.5f}s")
    except Exception as e:
        result_pipe.send((equation, f"Error: {str(e)}", 0))

def silthread_solve_equations(equations, result_pipe):
    """Crea un hilo por cada ecuación y espera a que terminen."""
    threads = []
    for ecuacion in equations:
        thread = th.Thread(target=silsolve_equation, args=(ecuacion, result_pipe))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

def procEcConTime():
    """Ejecuta las ecuaciones del archivo en paralelo con hilos."""
    with open("ecuaciones.txt", "r", encoding="utf-8") as f:
        ecuaciones = [line.strip() for line in f.readlines()]

    tuberia1, tuberia2 = mp.Pipe()
    inicio_total = time.time()
    silthread_solve_equations(ecuaciones, tuberia2)
    while tuberia1.poll():
        ecuacion, integral, tiempo = tuberia1.recv()
     
    fin_total = time.time()
    return fin_total - inicio_total



########################################################################







def procesar_ecuaciones_concurrente():
    """Ejecuta las ecuaciones del archivo en paralelo con hilos."""
    with open("ecuaciones.txt", "r", encoding="utf-8") as f:
        ecuaciones = [line.strip() for line in f.readlines()]

    tuberia1, tuberia2 = mp.Pipe()
    inicio_total = time.time()
    thread_solve_equations(ecuaciones, tuberia2)

    print("\nResolución concurrente de ecuaciones:\n")
    while tuberia1.poll():
        ecuacion, integral, tiempo = tuberia1.recv()
        print(f"{ecuacion} → {integral} (tardó {tiempo:.5f} s)")
    fin_total = time.time()
    print(f"\nTiempo total concurrente: {fin_total - inicio_total:.5f} s\n")

if __name__ == "__main__":
    procesar_ecuaciones_concurrente()
