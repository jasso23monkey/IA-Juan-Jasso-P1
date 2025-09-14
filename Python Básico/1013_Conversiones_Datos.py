numero_1 = input("Ingrese un numero a sumar: ")
numero_2 = input("Ingrese un segundo numero a sumar: ")

suma = numero_1 + numero_2
print(f"Tipo de numero_1: {type(numero_1)}")
print(f"Tipo de numero_2: {type(numero_2)}")
print(suma)
print(f"Tipo de suma: {type(suma)}")

print("**Convirtiendo a enteros**")

numero_1 = int(numero_1)
numero_2 = int(numero_2)
suma = numero_1 + numero_2
print(f"Tipo de numero_1: {type(numero_1)}")
print(f"Tipo de numero_2: {type(numero_2)}")
print(suma)
print(f"Tipo de suma: {type(suma)}")


numero_1 = int(input("Ingrese un numero a sumar: "))
numero_2 = float(input("Ingrese un segundo numero flotante a sumar: "))
suma = numero_1 + numero_2
print(suma)
print(f"Tipo de suma: {type(suma)}")
suma = int(suma)
print("**Convertir a entero**")
print(suma)
print(f"Tipo de suma: {type(suma)}")
print("**Convertiendo a otro tipo")
hexa = hex(suma)
print(hexa)
print(f"Tipo del cambio: {type(hexa)}")



