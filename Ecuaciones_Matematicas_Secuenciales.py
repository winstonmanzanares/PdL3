from sympy import symbols, integrate, sin, exp, log, sec 
import os
import time
import logging

# Configurar el logger
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger('mi-logger')

# Función para resolver una ecuación y almacenar el resultado
def solve_equation(equation):
    x, a, b = symbols('x a b')  # Definir variables simbólicas

    inicio = time.time()
    equation = equation.replace('^', '**')  
    resutlado_integral = integrate(eval(equation), x)
    fin = time.time()
    tiempo = fin - inicio

    # Registrar el tiempo de ejecución en el logger
    logger.debug(f"solve_equation_integral {equation} se ejecutó en {tiempo:.4f} s")
        
    return (equation, resutlado_integral)


def Inicializar():
    directorio = "C:\\Users\\bsori\\OneDrive\\Escritorio\\Laboratorio 3 programación\\Directorio"

    # Obtener la lista de archivos en el directorio
    contenido = os.listdir(directorio)
    archivos = [os.path.join(directorio, archivo) for archivo in contenido if os.path.isfile(os.path.join(directorio, archivo))]

    # Buscar el archivo de ecuaciones
    archivo_ecuaciones = None
    for archivo in archivos:
        if archivo.endswith("ecuaciones.txt"):
            archivo_ecuaciones = archivo
            break


    with open(archivo_ecuaciones, 'r') as ecuaciones:
        ecuaciones = [line.strip() for line in ecuaciones.readlines()]

    # Lista para almacenar los resultados
    resultados = []

    # Resolver las ecuaciones de manera secuencial (sin hilos ni procesos)
    for ecuacion in ecuaciones:
        resultado = solve_equation(ecuacion)
        resultados.append(resultado)

    # Imprimir los resultados
    print()
    print("\n\033[1mResultados de las integrales de las ecuaciones:\n\033[0m")

    for ecuacion, integral in resultados:
        print(f"La integral de la ecuación {ecuacion} es: {integral}\n")




Inicializar()
