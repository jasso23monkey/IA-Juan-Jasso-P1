# Definición de la base de datos de luchadores
luchadores = {
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

# Bucle principal para que el usuario ingrese un luchador
while True:
    print("\n-------------------------------------")
    nombre_ingresado = input("Ingresa el nombre de un luchador (o 'salir' para terminar): ")
    nombre_ingresado = nombre_ingresado.title()  # Formatea la entrada para coincidir con las claves

    # 1. Uso de la función if-else para checar la existencia del luchador
    if nombre_ingresado == 'Salir':
        print("Saliendo del programa. ¡Hasta la próxima!")
        break
    
    if nombre_ingresado in luchadores:
        print("\n¡Luchador encontrado!")
        datos = luchadores[nombre_ingresado]
        print(f"Nombre: {nombre_ingresado}")
        print(f"Técnica: {datos['tecnica']}")
        print(f"Fuerza: {datos['fuerza']}")
        print(f"Carisma: {datos['carisma']}")
        print(f"Es un luchador: {datos['tipo']}")

        # Variables para el bucle y la comparación
        nombre_luchador = nombre_ingresado
        datos_luchador = luchadores[nombre_luchador]
        
        # 2. Uso de un bucle while para el menú interactivo
        while True:
            print("\n--- Menú de Comparación ---")
            print("¿Qué quieres revisar? (técnica, fuerza, carisma)")
            print("Escribe 'menu' para volver al menú de luchadores o 'salir' para terminar.")
            caracteristica_ingresada = input("Opción: ")
            caracteristica_ingresada = caracteristica_ingresada.lower() # Normaliza la entrada
            
            # 3. Uso de la función match para manejar las opciones
            match caracteristica_ingresada:
                case "salir":
                    print("Saliendo del programa. ¡Hasta la próxima!")
                    exit()
                case "menu":
                    break # Sale del bucle interior para volver al menú principal
                
                case "fuerza" | "tecnica" | "carisma":
                    valor_luchador = datos_luchador[caracteristica_ingresada]
                    
                    # 4. Uso de un bucle for para encontrar el valor más alto y más bajo
                    max_valor = 0
                    min_valor = 11 # Un valor inicial más alto que cualquier posible calificación
                    mas_fuerte = ""
                    mas_debil = ""
                    
                    for luchador, datos in luchadores.items():
                        if datos[caracteristica_ingresada] > max_valor:
                            max_valor = datos[caracteristica_ingresada]
                            mas_fuerte = luchador
                        
                        if datos[caracteristica_ingresada] < min_valor:
                            min_valor = datos[caracteristica_ingresada]
                            mas_debil = luchador
                    
                    # 5. Uso de if-else para comparar y mostrar resultados
                    print("\n--- Resultado de la comparación ---")
                    if valor_luchador == max_valor:
                        print(f"¡{nombre_luchador} es el luchador con más {caracteristica_ingresada}!")
                    elif valor_luchador == min_valor:
                        print(f"¡{nombre_luchador} es el luchador con menos {caracteristica_ingresada}!")
                    else:
                        print(f"El nivel de {caracteristica_ingresada} de {nombre_luchador} es de {valor_luchador}, un nivel medio.")
                
                case _:
                    print("Opción no válida. Por favor, elige entre 'fuerza', 'tecnica', 'carisma', 'menu' o 'salir'.")
                    
    else:
        # Si el luchador no se encuentra en el diccionario
        print(f"Lo siento, '{nombre_ingresado}' no se encuentra en nuestra lista de luchadores.")