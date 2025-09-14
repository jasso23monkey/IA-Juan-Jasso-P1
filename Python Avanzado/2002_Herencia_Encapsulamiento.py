class Luchador:
    # Constructor de la clase base.
    def __init__(self, nombre, fuerza, tecnica, agilidad, carisma, nivel):
        self.nombre = nombre
        self.fuerza = fuerza
        self.tecnica = tecnica
        self.agilidad = agilidad
        self.carisma = carisma
        self.nivel = nivel
    
    # Método para "alardear"
    def alardear(self):
        print(f"El luchador {self.nombre} está alardeando.")

    # Método para "atacar"
    def atacar(self):
        print(f"El luchador {self.nombre} está atacando.")

class LuchadorTecnico(Luchador):
    # La clase hereda de Luchador.
    def __init__(self, nombre, fuerza, tecnica, agilidad, carisma, nivel, especial):
        # Llama al constructor de la clase padre (Luchador) para heredar sus atributos.
        super().__init__(nombre, fuerza, tecnica, agilidad, carisma, nivel)
        self.tipo = "Técnico"
        self.especial = especial

class LuchadorRudo(Luchador):
    # La clase hereda de Luchador.
    def __init__(self, nombre, fuerza, tecnica, agilidad, carisma, nivel, especial):
        # Llama al constructor de la clase padre (Luchador) para heredar sus atributos.
        super().__init__(nombre, fuerza, tecnica, agilidad, carisma, nivel)
        self.tipo = "Rudo"
        self.especial = especial

# Crear una instancia de cada subclase
luchador_tecnico = LuchadorTecnico("El Santo", 9, 9, 8, 10, 95, "La de a caballo")
luchador_rudo = LuchadorRudo("El Cavernícola Galindo", 10, 7, 7, 9, 90, "El nudo ciego")

# Mostrar los datos en pantalla
print("--- Datos del luchador técnico ---")
print(f"Nombre: {luchador_tecnico.nombre}")
print(f"Tipo: {luchador_tecnico.tipo}")
print(f"Poder especial: {luchador_tecnico.especial}")

print("\n--- Datos del luchador rudo ---")
print(f"Nombre: {luchador_rudo.nombre}")
print(f"Tipo: {luchador_rudo.tipo}")
print(f"Poder especial: {luchador_rudo.especial}")