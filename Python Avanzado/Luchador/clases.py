# luchadores/clases.py

class Luchador:
    def __init__(self, nombre, fuerza, tecnica, agilidad, carisma, nivel):
        self.nombre = nombre
        self.fuerza = fuerza
        self.tecnica = tecnica
        self.agilidad = agilidad
        self.carisma = carisma
        self.nivel = nivel
    
    def alardear(self):
        print(f"El luchador {self.nombre} está alardeando.")

    def atacar(self):
        print(f"El luchador {self.nombre} está atacando con un movimiento básico.")

class LuchadorTecnico(Luchador):
    def __init__(self, nombre, fuerza, tecnica, agilidad, carisma, nivel, especial):
        super().__init__(nombre, fuerza, tecnica, agilidad, carisma, nivel)
        self.tipo = "Técnico"
        self.especial = especial
    
    def atacar(self):
        print(f"El luchador {self.nombre} está atacando con su llave especial: '{self.especial}'!")
    
class LuchadorRudo(Luchador):
    def __init__(self, nombre, fuerza, tecnica, agilidad, carisma, nivel, especial):
        super().__init__(nombre, fuerza, tecnica, agilidad, carisma, nivel)
        self.tipo = "Rudo"
        self.especial = especial

    def atacar(self):
        print(f"El luchador {self.nombre} ataca sin piedad con su jugada ilegal: '{self.especial}'!")