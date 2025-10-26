import matplotlib.pyplot as plt
import numpy as np
import threading
import sys
import time

from Conteo_palabras_Secuencial import procSecTime
from Conteo_Palabras_Concurrente import procConcTime
from Ecuaciones_Matematicas_Secuenciales import procEcSecTime
from ecuaciones_matematicas_concurrente import procEcConTime



# Cantidad de simulaciones
N = 16  # Cada una lleva aproximadamente 1 minuto! Se recomienda usar valores bajos
poly_deg = 3  # Grado de ajuste polinómico

# Hilo de onda de carga   -->   ˥ ˦ ˧ ˨ ˩                                     
def spinner(stop_event):
    frames = "˥ ˦ ˧ ˨ ˩ ˩ ˨","˦ ˧ ˨ ˩ ˩ ˨ ˧","˧ ˨ ˩ ˩ ˨ ˧ ˦","˨ ˩ ˩ ˨ ˧ ˦ ˥","˩ ˩ ˨ ˧ ˦ ˥ ˥","˩ ˨ ˧ ˦ ˥ ˥ ˦","˨ ˧ ˦ ˥ ˥ ˦ ˧","˧ ˦ ˥ ˥ ˦ ˧ ˨","˦ ˥ ˥ ˦ ˧ ˨ ˩","˥ ˥ ˦ ˧ ˨ ˩ ˩"
    while not stop_event.is_set():
        for frame in frames:
            sys.stdout.write(f"\rProcesando simulaciones... {frame}")
            sys.stdout.flush()
            time.sleep(0.06)
    sys.stdout.write("\rProcesamiento completo!       \n")


def inicio():
    stop_event = threading.Event()
    spinner_thread = threading.Thread(target=spinner, args=(stop_event,))
    spinner_thread.start()

    try:
        # Generador de listas de valores de tiempo
        sec_word = [procSecTime() for _ in range(N)]
        conc_word = [procConcTime() for _ in range(N)]
        sec_eq = [procEcSecTime() for _ in range(N)]
        conc_eq = [procEcConTime() for _ in range(N)]

    finally:
        # Detiene la animación de carga
        stop_event.set()
        spinner_thread.join()

    # Cantidad de simulaciones
    runs = np.arange(1, N + 1)

    # --- Plot 1: Conteo de Palabras ---
    plt.figure(figsize=(10, 6))
    plt.plot(runs, sec_word, 'o-', color='red', label='Secuencial')
    plt.plot(runs, conc_word, 'o-', color='green', label='Concurrente')


    plt.title("Conteo de Palabras: Tiempos de Ejecución", fontsize=14)
    plt.xlabel("Número de simulación")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()
    plt.grid(alpha=0.6)
    plt.tight_layout()
    plt.savefig("Tiempos_Conteo_Palabras.png", dpi=300)
    plt.show()

    # --- Plot 2: Ecuaciones Matemáticas ---
    plt.figure(figsize=(10, 6))
    plt.plot(runs, sec_eq, 'o-', color='red', label='Secuencial')
    plt.plot(runs, conc_eq, 'o-', color='green', label='Concurrente')

    plt.title("Ecuaciones Matemáticas: Tiempos de Ejecución", fontsize=14)
    plt.xlabel("Número de simulación")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()
    plt.grid(alpha=0.6)
    plt.tight_layout()
    plt.savefig("Tiempos_Ecuaciones_Matematicas.png", dpi=300)
    plt.show()

    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("▒▒ Gráficos generados correctamente ▒▒")
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")


if __name__ == "__main__":
    inicio()
