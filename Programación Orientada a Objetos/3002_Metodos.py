
class Luchador:
    # Constructor de la clase
    def __init__(self, nombre, fuerza, tecnica, agilidad, carisma, tipo):
        self.nombre = nombre
        self.fuerza = fuerza
        self.tecnica = tecnica
        self.agilidad = agilidad
        self.carisma = carisma
        self.tipo = tipo
        self.vida = 100
        self.suerte = 1.0

    # Método para "alardear"
    def alardear(self):
        print(f"El luchador {self.nombre} está alardeando y recuperando energía.")
        # Aumenta la vida del luchador. El carisma podría influir en la cantidad.
        vida_recuperada = self.carisma * 1.5 
        self.vida += vida_recuperada
        # Asegúrate de que la vida no exceda el máximo
        if self.vida > 100:
            self.vida = 100
        print(f"La vida de {self.nombre} ahora es {self.vida}.")

    # Método para "atacar"
    def atacar(self, tipo_ataque):
        # Definimos el daño base para cada tipo de ataque
        danos_base = {
            "golpe": 10,
            "aereo": 12,
            "sumision": 11
        }

        dano_inicial = danos_base.get(tipo_ataque, 0) # Obtiene el daño base o 0 si el tipo no existe

        # Cansancio: si la vida es menor o igual a 25, se reduce el daño
        if self.vida <= 25:
            multiplicador_cansancio = 0.75
        else:
            multiplicador_cansancio = 1.0

        # Multiplica el daño inicial por un atributo y el factor de cansancio
        if tipo_ataque == "golpe":
            dano_final = (dano_inicial + self.fuerza) * multiplicador_cansancio
            print(f"El luchador {self.nombre} dio un golpe.")
        elif tipo_ataque == "aereo":
            dano_final = (dano_inicial + self.tecnica) * multiplicador_cansancio
            print(f"El luchador {self.nombre} salto de la tercera cuerda.")
        elif tipo_ataque == "sumision":
            print(f"El luchador {self.nombre} intento rendir al oponente.")
            dano_final = (dano_inicial + self.agilidad) * multiplicador_cansancio
        else:
            dano_final = 0
            print("Ataque no válido.")

        return dano_final

def crear_luchador():
    """Pide al usuario los datos para crear un objeto Luchador."""
    print("--- Ingresa los datos del nuevo luchador ---")
    
    nombre = input("Nombre: ")
    fuerza = int(input("Fuerza (1-10): "))
    tecnica = int(input("Técnica (1-10): "))
    agilidad = int(input("Agilidad (1-10): "))
    carisma = int(input("Carisma (1-10): "))
    tipo = input("Tipo (técnico o rudo): ")
    
    # Crea la instancia de la clase Luchador con los datos ingresados
    return Luchador(nombre, fuerza, tecnica, agilidad, carisma, tipo)

# --- Programa principal ---

# Pide los datos al usuario y crea el objeto
mi_luchador = crear_luchador()

# Muestra los datos del luchador creado
print("\n--- ¡Tu luchador ha sido creado! ---")
print(f"Nombre: {mi_luchador.nombre}")
print(f"Fuerza: {mi_luchador.fuerza}")
print(f"Técnica: {mi_luchador.tecnica}")
print(f"Agilidad: {mi_luchador.agilidad}")
print(f"Carisma: {mi_luchador.carisma}")
print(f"Tipo: {mi_luchador.tipo}")
print(f"Vida: {mi_luchador.vida}")

# Bucle para que el usuario escoja una acción
while True:
    print("\n--- Menú de acciones ---")
    accion = input("¿Qué quieres que haga tu luchador? (alardear/atacar/salir): ").lower()

    if accion == "alardear":
        mi_luchador.alardear()
    elif accion == "atacar":
        ataque = input("¿Qué quieres que haga tu luchador? (golpe/aereo/sumision): ").lower()
        if ataque == "golpe": 
            mi_luchador.atacar(ataque)
        elif ataque == "aereo": 
            mi_luchador.atacar(ataque)
        elif ataque == "sumision": 
            mi_luchador.atacar(ataque)
        else:
            print("Golpe nop valido")
        
    elif accion == "salir":
        print("El luchador se retira.")
        break
    else:
        print("Acción no válida. Por favor, elige entre 'alardear', 'atacar' o 'salir'.")