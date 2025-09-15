import random

class Luchador:
    # Constructor de la clase
    def __init__(self, nombre, fuerza, tecnica, agilidad, carisma, tipo, *logros):
        self.nombre = nombre
        self.fuerza = fuerza
        self.tecnica = tecnica
        self.agilidad = agilidad
        self.carisma = carisma
        self.tipo = tipo
        self.vida = 100
        self.suerte = 1.0
        self.logros = logros

    # Método para "alardear"
    def alardear(self):
        print(f"El luchador {self.nombre} está alardeando...")
        
        # El carisma del luchador determina el cambio en la suerte
        if self.carisma >= 8:
            cambio_suerte = 0.5 + random.random() / 2  
            self.suerte += cambio_suerte
            print(f"¡La multitud lo anima! Su suerte aumenta a {self.suerte:.2f}.")
        else:
            self.suerte -= 0.25 
            if self.suerte < 0.25:
                self.suerte = 0.25
            print(f"La multitud lo abuchea. Su suerte disminuye a {self.suerte:.2f}.")

    # Método para "atacar"
    def atacar(self, tipo_ataque):
        danos_base = {
            "golpe": 10,
            "aereo": 12,
            "sumision": 11
        }
        dano_inicial = danos_base.get(tipo_ataque, 0)

        if self.vida <= 25:
            multiplicador_cansancio = 0.75
        else:
            multiplicador_cansancio = 1.0

        if tipo_ataque == "golpe":
            dano_final = (dano_inicial + self.fuerza) * multiplicador_cansancio
            print(f"El luchador {self.nombre} dio un golpe.")
        elif tipo_ataque == "aereo":
            dano_final = (dano_inicial + self.tecnica) * multiplicador_cansancio
            print(f"El luchador {self.nombre} salto de la tercera cuerda.")
        elif tipo_ataque == "sumision":
            dano_final = (dano_inicial + self.agilidad) * multiplicador_cansancio
            print(f"El luchador {self.nombre} intento rendir al oponente.")
        else:
            dano_final = 0
            print("Ataque no válido.")
        
        dano_final = dano_final * self.suerte
        print(f"El ataque fue de {dano_final:.2f} puntos")
        return dano_final
    
    def presentar_logros(self):
        if self.logros:
            print(f"¡Atención, damas y caballeros! Presentando a {self.nombre} y sus logros:")
            for i, logro in enumerate(self.logros, 1):
                print(f"  {i}. {logro}")
        else:
            print(f"{self.nombre} no tiene logros notables.")

## Clases de Luchadores Específicos

class LuchadorTecnico(Luchador):
    def __init__(self, nombre, fuerza, tecnica, agilidad, carisma, tipo, especial, *logros):
        super().__init__(nombre, fuerza, tecnica, agilidad, carisma, tipo, *logros)
        self.especial = especial
    
    def alardear(self):
        print(f"El luchador {self.nombre} está saludando al público con una pose acrobática.")
        self.vida += self.carisma * 2
        if self.vida > 100:
            self.vida = 100
        print(f"El público lo ovaciona, recupera vida. Vida actual: {self.vida}.")

    def atacar(self, oponente):
        print(f"{self.nombre} ejecuta su llave especial: '{self.especial}'!")
        dano = (self.tecnica * 3) + (self.agilidad * 2)
        oponente.vida -= dano
        print(f"¡{oponente.nombre} recibe {dano:.2f} de daño! Vida restante: {oponente.vida:.2f}")

class LuchadorRudo(Luchador):
    def __init__(self, nombre, fuerza, tecnica, agilidad, carisma, tipo, especial, *logros):
        super().__init__(nombre, fuerza, tecnica, agilidad, carisma, tipo, *logros)
        self.especial = especial
    
    def alardear(self):
        print(f"El luchador {self.nombre} está insultando al público.")
        self.suerte -= 0.5
        if self.suerte < 0:
            self.suerte = 0
        print(f"El público lo abuchea, su suerte baja a {self.suerte:.2f}.")

    def atacar(self, oponente):
        print(f"{self.nombre} ataca con una jugada ilegal: '{self.especial}'!")
        dano = (self.fuerza * 3) + (self.agilidad * 1.5)
        oponente.vida -= dano
        print(f"¡{oponente.nombre} recibe {dano:.2f} de daño! Vida restante: {oponente.vida:.2f}")

# --- La función crear_luchador() ha sido modificada ---
def crear_luchador():
    """
    Pide los datos al usuario y crea un objeto LuchadorTecnico o LuchadorRudo
    según la elección del usuario.
    """
    print("--- Ingresa los datos de tu luchador ---")
    
    nombre = input("Nombre: ")
    fuerza = int(input("Fuerza (1-10): "))
    tecnica = int(input("Técnica (1-10): "))
    agilidad = int(input("Agilidad (1-10): "))
    carisma = int(input("Carisma (1-10): "))
    
    while True:
        tipo = input("Tipo (tecnico/rudo): ").lower()
        if tipo in ["tecnico", "rudo"]:
            break
        print("Tipo no válido. Por favor, ingresa 'tecnico' o 'rudo'.")
    
    especial = input(f"Ingrese el movimiento especial de su luchador {tipo}: ")
    logros_str = input("Ingrese los logros separados por comas: ")
    logros = [l.strip() for l in logros_str.split(',') if l.strip()]

    # Condicional que decide qué clase instanciar
    if tipo == "tecnico":
        return LuchadorTecnico(nombre, fuerza, tecnica, agilidad, carisma, tipo, especial, *logros)
    elif tipo == "rudo":
        return LuchadorRudo(nombre, fuerza, tecnica, agilidad, carisma, tipo, especial, *logros)

# --- Programa principal ---

# Pide los datos al usuario y crea el objeto
# Ahora mi_luchador será de la clase correcta (LuchadorTecnico o LuchadorRudo)
mi_luchador = crear_luchador()

# Crear al oponente
oponente = LuchadorRudo("El Cavernicola Galindo", 10, 7, 7, 9, "rudo", "El nudo ciego", "Campeon de rudeza")

# Muestra los datos del luchador creado
print("\n--- ¡Tu luchador ha sido creado! ---")
print(f"Nombre: {mi_luchador.nombre}")
print(f"Fuerza: {mi_luchador.fuerza}")
print(f"Técnica: {mi_luchador.tecnica}")
print(f"Agilidad: {mi_luchador.agilidad}")
print(f"Carisma: {mi_luchador.carisma}")
print(f"Tipo: {mi_luchador.tipo}")
print(f"Vida: {mi_luchador.vida}")
mi_luchador.presentar_logros()

# Muestra los datos del oponente creado
print("\n--- ¡Tu contrincante esta subiendo al ring! ---")
print(f"Nombre: {oponente.nombre}")
print(f"Fuerza: {oponente.fuerza}")
print(f"Técnica: {oponente.tecnica}")
print(f"Agilidad: {oponente.agilidad}")
print(f"Carisma: {oponente.carisma}")
print(f"Tipo: {oponente.tipo}")
print(f"Vida: {oponente.vida}")
oponente.presentar_logros()


# Bucle para que el usuario escoja una acción
while True:
    print("\n--- Menú de acciones ---")
    accion = input("¿Qué quieres que haga tu luchador? (alardear/atacar/salir): ").lower()

    if accion == "alardear":
        mi_luchador.alardear()
    elif accion == "atacar":
        # Aquí, el método 'atacar' de las subclases requiere un 'oponente'
        mi_luchador.atacar(oponente) # Le pasas el oponente al método
    elif accion == "salir":
        print("El luchador se retira.")
        break
    else:
        print("Acción no válida. Por favor, elige entre 'alardear', 'atacar' o 'salir'.")
