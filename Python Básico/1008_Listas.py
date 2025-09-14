luchadores1 = ["Mr Iguana", "La Parka", "Místico", "Kemonito"]
print(luchadores1)

luchadores1.append("Dominik Mysterio") #añade al final otro elemento a la lista
print(luchadores1)

luchadores1.insert(0,"Pagano") #inserta un valor a la lista en el indice que quiera
print(luchadores1)

luchadores2 = ["Rey Mysterio", "Alberto del Rio", "Jhon Cena", "Kemonito"]
luchadores1.extend(luchadores2) #combina las listas
print(luchadores1)

luchadores1.pop() #elimina el ultimo valor de la lista
print(luchadores1)

luchadores1.pop(3) #elimina el valor de la lista en el indice que quiera
print(luchadores1)

luchadores1.remove("Dominik Mysterio") #remueve lo puesto entre parentesis de la lista
print(luchadores1)

luchador = luchadores1.index("Mistico") #estrae el valor indicado de la lista
print(luchador)

coincidencias = luchadores1.count()
print("Hay" + coincidencias + "en los luchadores")
