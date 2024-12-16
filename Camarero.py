import threading
import time


def servir_cafe():
    # Simula servir café para 5 clientes
    for i in range(5):  
        print(f"Camarero: Sirviendo café {i + 1}")
        # Tiempo necesario para servir un café
        time.sleep(1)  
    print("Camarero: Terminó de servir todos los cafés")

def poner_tostadas():
    # Simula poner tostadas para 5 clientes
    for i in range(5):  
        print(f"Camarero: Poniendo tostada {i + 1}")
        # Tiempo necesario para preparar una tostada
        time.sleep(1.5)  
    print("Camarero: Terminó de poner todas las tostadas")

def hacer_tortilla():
    # Simula hacer tortillas para 5 clientes
    for i in range(5):  
        print(f"Camarero: Haciendo tortilla {i + 1}")
        # Tiempo necesario para hacer una tortilla
        time.sleep(2)  
    print("Camarero: Terminó de hacer todas las tortillas")

if __name__ == "__main__":
    # Crear los hilos para cada tarea
    hilo_cafe = threading.Thread(target=servir_cafe)
    hilo_tostadas = threading.Thread(target=poner_tostadas)
    hilo_tortilla = threading.Thread(target=hacer_tortilla)

    # Iniciar los hilos
    hilo_cafe.start()
    hilo_tostadas.start()
    hilo_tortilla.start()

    # Esperar a que todos los hilos terminen
    hilo_cafe.join()
    hilo_tostadas.join()
    hilo_tortilla.join()

    print("Fin del programa")