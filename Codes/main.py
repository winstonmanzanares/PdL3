from Conteo_palabras_Secuencial import procesar_secuencial
from Conteo_Palabras_Concurrente import procesar_concurrente
from Ecuaciones_Matematicas_Secuenciales import procesar_ecuaciones
from ecuaciones_matematicas_concurrente import procesar_ecuaciones_concurrente

def menu():
    """Menú principal del proyecto."""
    while True:
        print("""
===========================================
🔷 MENÚ PRINCIPAL 🔷
1- Conteo de palabras secuencial
2- Conteo de palabras concurrente
3- Ecuaciones secuenciales
4- Ecuaciones concurrentes
0- Salir
===========================================
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            procesar_secuencial()
        elif opcion == "2":
            procesar_concurrente()
        elif opcion == "3":
            procesar_ecuaciones()
        elif opcion == "4":
            procesar_ecuaciones_concurrente()
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.\n")

if __name__ == "__main__":
    menu()
