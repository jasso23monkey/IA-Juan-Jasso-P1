class Luchador:
    # Constructor de la clase
    def __init__(self, nombre, fuerza, tecnica, agilidad, carisma, nivel, tipo):
        self.nombre = nombre
        self.fuerza = fuerza
        self.tecnica = tecnica
        self.agilidad = agilidad
        self.carisma = carisma
        self.nivel = nivel
        self.tipo = tipo

    # Método para "alardear"
    def alardear(self):
        print(f"El luchador {self.nombre} está alardeando.")

    # Método para "atacar"
    def atacar(self):
        print(f"El luchador {self.nombre} está atacando.")

def crear_luchador():
    """Pide al usuario los datos para crear un objeto Luchador."""
    print("--- Ingresa los datos del nuevo luchador ---")
    
    nombre = input("Nombre: ")
    fuerza = int(input("Fuerza (1-10): "))
    tecnica = int(input("Técnica (1-10): "))
    agilidad = int(input("Agilidad (1-10): "))
    carisma = int(input("Carisma (1-10): "))
    nivel = int(input("Nivel (1-100): "))
    tipo = input("Tipo (técnico o rudo): ")
    
    # Crea la instancia de la clase Luchador con los datos ingresados
    return Luchador(nombre, fuerza, tecnica, agilidad, carisma, nivel, tipo)

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
print(f"Nivel: {mi_luchador.nivel}")
print(f"Tipo: {mi_luchador.tipo}")

# Bucle para que el usuario escoja una acción
while True:
    print("\n--- Menú de acciones ---")
    accion = input("¿Qué quieres que haga tu luchador? (alardear/atacar/salir): ").lower()

    if accion == "alardear":
        mi_luchador.alardear()
    elif accion == "atacar":
        mi_luchador.atacar()
    elif accion == "salir":
        print("El luchador se retira.")
        break
    else:
        print("Acción no válida. Por favor, elige entre 'alardear', 'atacar' o 'salir'.")