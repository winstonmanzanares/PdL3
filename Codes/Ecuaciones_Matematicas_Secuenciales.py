from sympy import symbols, integrate, sin, exp, log, sec
import os, time, logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger('mi-logger')

def solve_equation(equation):
    """Resuelve una integral simbólica de forma secuencial."""
    x, a, b = symbols('x a b')
    inicio = time.time()
    equation = equation.replace('^', '**')
    resultado_integral = integrate(eval(equation), x)
    fin = time.time()
    logger.debug(f"Integral {equation} calculada en {fin - inicio:.5f}s")
    return (equation, resultado_integral, fin - inicio)




########################################################################
# Bloque de funciones similares a las originales pero sin el datalogger


def silsolve_equation(equation):
    """Resuelve una integral simbólica de forma secuencial."""
    x, a, b = symbols('x a b')
    inicio = time.time()
    equation = equation.replace('^', '**')
    resultado_integral = integrate(eval(equation), x)
    fin = time.time()
    return (equation, resultado_integral, fin - inicio)


def procEcSecTime():
    with open("ecuaciones.txt", "r", encoding="utf-8") as f:
        ecuaciones = [line.strip() for line in f.readlines()]

    inicio_total = time.time()

    for eq in ecuaciones:
        ecuacion, resultado, tiempo = silsolve_equation(eq)

    fin_total = time.time()
    return fin_total - inicio_total



########################################################################






def procesar_ecuaciones():
    """Lee ecuaciones.txt y las integra una por una."""
    with open("ecuaciones.txt", "r", encoding="utf-8") as f:
        ecuaciones = [line.strip() for line in f.readlines()]

    inicio_total = time.time()
    print("\nResolución secuencial de ecuaciones:\n")

    for eq in ecuaciones:
        ecuacion, resultado, tiempo = solve_equation(eq)
        print(f"   {ecuacion} → {resultado} (tardó {tiempo:.5f} s)")

    fin_total = time.time()
    print(f"\nTiempo total secuencial: {fin_total - inicio_total:.5f} s\n")

if __name__ == "__main__":
    procesar_ecuaciones()
