def crear_lista(*args):
    # Creamos una lista vacía.
    lista = []

    # Añadimos los datos a la lista.
    for dato in args:
        lista.append(dato)

    return lista

# Llamamos a la función.
llamada = crear_lista(7,45,32,134,563,23)

# Imprimimos la lista.
print("Los valores en la lista son:", llamada)

def funcion(a, b, *args):
    print(a, b, args)

funcion(1, 4, 5, 23, 45)

def luchadores(**kwargs):
    print(kwargs)

luchadores(nombre="Mr Iguana",
            tecnica=8,
            carisma=10,
            edad="27")

def datos(*args, **kwargs):
    print(args)
    print(kwargs)

usuario1 = {"nombre":"Gabriela",
            "apellidos":"Gómez de la barca",
            "edad":"27"}

datos(10,50,60, **usuario1)


def info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"Clave: {clave}, Valor: {valor}")

argumentos = {"Nombre": "Enrique",
              "Edad": 32,
              "Teléfono": "123456789"}

info(**argumentos)

suma = lambda x, y: x + y
print(suma(5, 20))
print(suma(3, 7))

# Calcula la raíz cuadrada
def raiz_cuadrada(numero):
    return numero ** 2

# Lista con números
lista_numeros = [9, 15, 150, 63, 70]

# Hacemos los cálculos
resultado = map(raiz_cuadrada, lista_numeros)

# Comprobamos el tipo de dato que crea map
print(type(resultado))

# Creamos la lista con los cálculos
lista_raices = list(resultado)

# Comprobamos el resultado
print(lista_raices)


def raices_cuadradas(numeros):
    cuadrados = map(lambda numero: numero ** 2, numeros)
    return list(cuadrados)

# Lista para probar la función
lista_numeros = [9, 15, 150, 63, 70]

# Se crea la lista con las raices cuadradas calculadas
raices = raices_cuadradas(lista_numeros)

# Comprobamos los valores
print(raices)

def decoradora(funcion_parametro):
    print("El resultado de la operación es: ")
    funcion_parametro()
    print("Operación realizada con éxito.")

@decoradora
def sumar():
    print(10 + 10)

@decoradora
def restar():
    print(10 - 20)

@decoradora
def multiplicar():
    print(45 * 2)

@decoradora
def dividir():
    print(4 / 87)