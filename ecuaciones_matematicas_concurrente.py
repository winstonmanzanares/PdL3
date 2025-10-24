import multiprocessing as mp
from sympy import symbols, integrate, sin, exp, log, sec 
import threading as th
import os
import time
import logging

# Configurar el logger
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger('mi-logger')

def solve_equation(equation, result_pipe):
   
    x, a, b = symbols('x a b')  

    try:
        inicio = time.time() 
        equation = equation.replace('^', '**')
        integral_result = integrate(eval(equation), x)
        fin = time.time()  
        tiempo = fin - inicio
        
        
        result_pipe.send((equation, integral_result))
        
       
        logger.debug(f"solve_equation_integral {equation} se ejecutó en {tiempo:.4f} s")
        
    except Exception as e:
        result_pipe.send((equation, f"Error: {str(e)}"))



def thread_solve_equations(equations, result_pipe):
    
    threads = []

    for ecuacion in equations:
        thread = th.Thread(target=solve_equation, args=(ecuacion, result_pipe))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()




def Inicializar():
  
    directorio = "C:\\Users\\bsori\\OneDrive\\Escritorio\\Laboratorio 3 programación\\Directorio"

    
    contenido = os.listdir(directorio)
    archivos = [os.path.join(directorio, archivo) for archivo in contenido if os.path.isfile(os.path.join(directorio, archivo))]

    
    archivo_ecuaciones = None
    for archivo in archivos:
        if archivo.endswith("ecuaciones.txt"):
            archivo_ecuaciones = archivo
            break

    if archivo_ecuaciones is None:
        print("Error: No se encontró 'ecuaciones.txt' en el directorio especificado")
        return

   
    with open(archivo_ecuaciones, 'r') as ecuaciones:
        equations = [line.strip() for line in ecuaciones.readlines()]

   
    tuberia1, tuberia2 = mp.Pipe()

  
    thread_solve_equations(equations, tuberia2)


    while tuberia1.poll():
        ecuacion, integral = tuberia1.recv()
        if "Error" in str(integral):
            print(f"Error al resolver la ecuación: {ecuacion}\n{integral}\n")
        else:
            print(f"Integral de la ecuación {ecuacion}: {integral}\n")

if __name__ == "__main__":
    Inicializar()
