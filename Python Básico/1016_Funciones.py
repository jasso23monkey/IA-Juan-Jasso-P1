# Definición de la base de datos de luchadores
LUCHADORES_DB = {
    "Mr. Iguana": {
        "tecnica": 8,
        "fuerza": 6,
        "carisma": 9,
        "tipo": "técnico"
    },
    "Pagano": {
        "tecnica": 7,
        "fuerza": 9,
        "carisma": 8,
        "tipo": "rudo"
    },
    "La Parka": {
        "tecnica": 9,
        "fuerza": 8,
        "carisma": 10,
        "tipo": "técnico"
    }
}

def buscar_luchador(nombre: str) -> dict | None:
    """Busca un luchador por su nombre en la base de datos."""
    return LUCHADORES_DB.get(nombre)

def mostrar_datos(nombre: str, datos: dict):
    """Imprime los datos de un luchador de forma legible."""
    print("\n¡Luchador encontrado!")
    print(f"Nombre: {nombre}")
    print(f"Técnica: {datos['tecnica']}")
    print(f"Fuerza: {datos['fuerza']}")
    print(f"Carisma: {datos['carisma']}")
    print(f"Es un luchador: {datos['tipo']}")

def comparar_caracteristica(nombre: str, datos: dict, caracteristica: str):
    """Compara una característica del luchador con el resto y muestra el resultado."""
    valor_luchador = datos[caracteristica]
    
    # Encuentra el valor mínimo y máximo de la característica en toda la base de datos
    max_valor = max(l['fuerza'] for l in LUCHADORES_DB.values()) if caracteristica == 'fuerza' else \
                max(l['tecnica'] for l in LUCHADORES_DB.values()) if caracteristica == 'tecnica' else \
                max(l['carisma'] for l in LUCHADORES_DB.values())
    
    min_valor = min(l['fuerza'] for l in LUCHADORES_DB.values()) if caracteristica == 'fuerza' else \
                min(l['tecnica'] for l in LUCHADORES_DB.values()) if caracteristica == 'tecnica' else \
                min(l['carisma'] for l in LUCHADORES_DB.values())
    
    print("\n--- Resultado de la comparación ---")
    if valor_luchador == max_valor:
        print(f"¡{nombre} es el luchador con más {caracteristica}!")
    elif valor_luchador == min_valor:
        print(f"¡{nombre} es el luchador con menos {caracteristica}!")
    else:
        print(f"El nivel de {caracteristica} de {nombre} es de {valor_luchador}, un nivel medio.")

def menu_luchador(nombre: str, datos: dict):
    """Maneja el menú interactivo para un luchador específico."""
    while True:
        print("\n--- Menú de Comparación ---")
        print("¿Qué quieres revisar? (tecnica, fuerza, carisma)")
        print("Escribe 'menu' para volver al menú de luchadores o 'salir' para terminar.")
        opcion = input("Opción: ").lower()
        
        match opcion:
            case "salir":
                print("Saliendo del programa. ¡Hasta la próxima!")
                exit()
            case "menu":
                break
            case "fuerza" | "tecnica" | "carisma":
                comparar_caracteristica(nombre, datos, opcion)
            case _:
                print("Opción no válida. Por favor, elige entre 'fuerza', 'tecnica', 'carisma', 'menu' o 'salir'.")

def main():
    """Función principal que ejecuta el flujo del programa."""
    while True:
        print("\n-------------------------------------")
        nombre_ingresado = input("Ingresa el nombre de un luchador (o 'salir' para terminar): ").title()
        
        if nombre_ingresado == 'Salir':
            print("Saliendo del programa. ¡Hasta la próxima!")
            break
        
        datos_luchador = buscar_luchador(nombre_ingresado)
        
        if datos_luchador:
            mostrar_datos(nombre_ingresado, datos_luchador)
            menu_luchador(nombre_ingresado, datos_luchador)
        else:
            print(f"Lo siento, '{nombre_ingresado}' no se encuentra en nuestra lista de luchadores.")

if __name__ == "__main__":
    main()