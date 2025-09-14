class Luchador:
    # Constructor de la clase base.
    def __init__(self, nombre, fuerza, tecnica, agilidad, carisma, nivel):
        self.nombre = nombre
        self.fuerza = fuerza
        self.tecnica = tecnica
        self.agilidad = agilidad
        self.carisma = carisma
        self.nivel = nivel
    
    # Método para "alardear" (genérico)
    def alardear(self):
        print(f"El luchador {self.nombre} está alardeando.")

    # Método para "atacar" (genérico)
    def atacar(self):
        print(f"El luchador {self.nombre} está atacando con un movimiento básico.")

class LuchadorTecnico(Luchador):
    # La clase hereda de Luchador.
    def __init__(self, nombre, fuerza, tecnica, agilidad, carisma, nivel, especial):
        super().__init__(nombre, fuerza, tecnica, agilidad, carisma, nivel)
        self.tipo = "Técnico"
        self.especial = especial
    
    # Sobrescribe el método atacar de la clase padre
    def atacar(self):
        print(f"El luchador {self.nombre} está atacando con su llave especial: '{self.especial}'!")
    
    # Sobrescribe el método alardear de la clase padre
    def alardear(self):
        print(f"¡{self.nombre} es un luchador {self.tipo}, y se prepara para el combate!")

class LuchadorRudo(Luchador):
    # La clase hereda de Luchador.
    def __init__(self, nombre, fuerza, tecnica, agilidad, carisma, nivel, especial):
        super().__init__(nombre, fuerza, tecnica, agilidad, carisma, nivel)
        self.tipo = "Rudo"
        self.especial = especial

    # Sobrescribe el método atacar de la clase padre
    def atacar(self):
        print(f"El luchador {self.nombre} ataca sin piedad con su jugada ilegal: '{self.especial}'!")
    
    # Sobrescribe el método alardear de la clase padre
    def alardear(self):
        print(f"¡{self.nombre} es un luchador {self.tipo} y provoca a la multitud!")

# Crear una instancia de cada subclase
luchador_tecnico = LuchadorTecnico("El Santo", 9, 9, 8, 10, 95, "La de a caballo")
luchador_rudo = LuchadorRudo("El Cavernícola Galindo", 10, 7, 7, 9, 90, "El nudo ciego")

# Lista de luchadores para demostrar el polimorfismo
cuadrilatero = [luchador_tecnico, luchador_rudo]

# Recorremos la lista y llamamos al mismo método en cada objeto.
# Python automáticamente llama a la versión correcta de 'atacar' para cada tipo.
for luchador in cuadrilatero:
    print("\n------------------------------")
    luchador.alardear()
    luchador.atacar()