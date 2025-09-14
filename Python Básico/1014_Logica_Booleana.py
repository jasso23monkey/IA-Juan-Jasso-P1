"""
== -> Igual que
!= -> Difernte que
<  -> Menor que
>  -> Mayor que
<= -> Menor o igual que
>= -> Menor o igual que
"""

num_1 = int(input("Ingrese un numero: "))
num_2 = int(input("Ingrese otro numero: "))

comparacion = num_1 == num_2
print("Son iguales: ", comparacion)
comparacion = num_1 != num_2
print("Son diferentes: ", comparacion)
comparacion = num_1 < num_2
print("El numero 1 es menor que el numero 2: ", comparacion)
comparacion = num_1 > num_2
print("El numero 1 es mayor que el numero 2: ", comparacion)
comparacion = num_1 <= num_2
print("El numero 1 es menor o igual que el numero 2: ", comparacion)
comparacion = num_1 >= num_2
print("El numero 1 es mayor o igual que el numero 2: ", comparacion)

num_3 = int(input("Ingrese otro numero: "))

comparacion = num_1 > num_2 and num_2 > num_3 
print("Numero 1 mayor que Numero 2 y Numero 2 mayor que Numero 3: ", comparacion)
comparacion = num_1 == num_2 or num_2 < num_3 
print("Numero 1 es igual que Numero 2 y Numero 2 menor que Numero 3: ", comparacion)
comparacion = not comparacion
print("Negando el anterior resultado: ", comparacion)