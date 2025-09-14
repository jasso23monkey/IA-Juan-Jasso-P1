#   Objetos Mutables: Objetos que pueden cambiar su valor despues de su cracion
lista = [10,30,40]
lista[0] = 20
print(lista)

#   Objetos Inmutables: Objetos que no pueden cambiar su valor despues de su cracion
tupla = (10, 20, 30, 40)
print(tupla)

#   Objetos Hashables: debe ser inmutable, tener un valor de hash constante en tiempo 
#  de ejecución y que sea comparable con otros objetos de su tipo para determinar si son iguales
saludo = "Hola Humano"
print(saludo)
print(hash(saludo))

