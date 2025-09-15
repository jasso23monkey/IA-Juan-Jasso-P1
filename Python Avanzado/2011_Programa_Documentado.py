# --- Función de simulación de lucha ---
def simular_lucha(luchador_1, luchador_2):
    """
    Simula un encuentro entre dos luchadores en el ring.

    Esta función presenta un menú al usuario para elegir una acción para cada luchador
    (atacar, alardear o salir). El bucle continúa hasta que el usuario decida salir.
    """
    while True:
        print("\n--- ¡Los luchadores están en el cuadrilátero! ---")
        print(f"1. {luchador_1.nombre}")
        print(f"2. {luchador_2.nombre}")
        print("3. Salir de la simulación")

        opcion_luchador = input("Elige una acción para el luchador: ")
        
        # Validar la entrada del usuario
        if opcion_luchador == '3':
            print("Saliendo de la simulación de lucha.")
            break
        
        if opcion_luchador not in ['1', '2']:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")
            continue  # Vuelve al inicio del bucle

        luchador_elegido = luchador_1 if opcion_luchador == '1' else luchador_2
        
        # Menú de acciones para el luchador elegido
        accion = input(f"\n¿Qué debe hacer {luchador_elegido.nombre}? (atacar/alardear): ").lower()
        
        if accion == 'atacar':
            luchador_elegido.atacar()
        elif accion == 'alardear':
            luchador_elegido.alardear()
        else:
            print("Acción no reconocida.")
            
# --- Programa principal ---
try:
    # Intenta importar el paquete y crear los objetos.
    import Luchador.clases

    luchador_1 = Luchador.clases.LuchadorTecnico("El Santo", 9, 9, 8, 10, 95, "La de a caballo")
    luchador_2 = Luchador.clases.LuchadorRudo("El Cavernícola Galindo", 10, 7, 7, 9, 90, "El nudo ciego")

    # Si la importación y la creación de objetos son exitosas, inicia la simulación.
    print(f"Nombre del técnico: {luchador_1.nombre}")
    print(f"Nombre del rudo: {luchador_2.nombre}")

    # Llamada a la nueva función
    simular_lucha(luchador_1, luchador_2)

except ImportError:
    # Este bloque se ejecuta si el paquete 'luchadores' no se puede importar.
    print("Error: No se pudo encontrar el paquete 'luchadores'.")
    print("Asegúrate de que la carpeta 'luchadores' esté en el mismo directorio que este script.")

except AttributeError:
    # Este bloque se ejecuta si se intenta acceder a una clase o método que no existe.
    print("Error: Una de las clases o métodos no se encuentra en el paquete.")
    print("Verifica que las clases 'LuchadorTecnico' y 'LuchadorRudo' estén correctamente definidas.")
    
except Exception as e:
    # Este bloque genérico captura cualquier otro error inesperado.
    print(f"Ocurrió un error inesperado: {e}")

finally:
    # Este bloque siempre se ejecuta, sin importar si hubo un error o no.
    print("\nProceso de ejecución del script finalizado.")