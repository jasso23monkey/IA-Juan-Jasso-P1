try:
    # Intenta importar el paquete y crear los objetos.
    # Esta es la parte del código que podría fallar si el paquete no existe o hay un error de sintaxis.
    import Luchador.clases

    luchador_1 = Luchador.clases.LuchadorTecnico("El Santo", 9, 9, 8, 10, 95, "La de a caballo")
    luchador_2 = Luchador.clases.LuchadorRudo("El Cavernícola Galindo", 10, 7, 7, 9, 90, "El nudo ciego")

    # Si todo lo anterior funciona, continúa con la ejecución normal.
    print(f"Nombre del técnico: {luchador_1.nombre}")
    luchador_2.atacar()

except ImportError:
    # Este bloque se ejecuta si el paquete 'luchadores' o el módulo 'clases' no se pueden importar.
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
    # Es útil para tareas de limpieza.
    print("\nProceso de ejecución del script finalizado.")