psitacidos = {
    "Guacamaya Roja": {
        "nombre_cientifico": "Ara macao",
        "familia": "Psittacidae",
        "distribucion": ["México", "América Central", "Brasil"],
        "estado_conservacion": "Preocupación menor",
        "colores": ["rojo", "amarillo", "azul"]
    },
    "Cacatúa Moluca": {
        "nombre_cientifico": "Cacatua moluccensis",
        "familia": "Cacatuidae",
        "distribucion": ["Indonesia"],
        "estado_conservacion": "Vulnerable",
        "colores": ["rosa salmón", "blanco"]
    },
    "Loro Gris": {
        "nombre_cientifico": "Psittacus erithacus",
        "familia": "Psittacidae",
        "distribucion": ["África Central y Occidental"],
        "estado_conservacion": "En peligro",
        "colores": ["gris", "rojo"]
    }
}


psitacido_buscar = input("Indique el Psitacido a buscar: ")
print(f"Información de la especie: {psitacido_buscar}")
print(f"Nombre científico: {psitacidos[psitacido_buscar]['nombre_cientifico']}")
print(f"Estado de conservación: {psitacidos[psitacido_buscar]['estado_conservacion']}")

psitacidos["Perico Monje"] = {
    "nombre_cientifico": "Myiopsitta monachus",
    "familia": "Psittacidae",
    "distribucion": ["Argentina", "Bolivia", "Brasil"],
    "estado_conservacion": "Preocupación menor",
    "colores": ["verde", "gris"]
}
print("\n--- Diccionario actualizado con 'Perico Monje' ---")

psitacido_buscar = input("Indique el Psitacido a eliminar: ")
del psitacidos[psitacido_buscar]
print("\n--- Diccionario después de eliminar 'Cacatúa Moluca' ---")
print(psitacidos)
