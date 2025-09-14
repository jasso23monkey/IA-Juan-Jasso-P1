import Luchador.clases

luchador_1 = Luchador.clases.LuchadorTecnico("El Santo", 9, 9, 8, 10, 95, "La de a caballo")
luchador_2 = Luchador.clases.LuchadorRudo("El Cavernícola Galindo", 10, 7, 7, 9, 90, "El nudo ciego")

print(f"Nombre del técnico: {luchador_1.nombre}")
luchador_2.atacar()