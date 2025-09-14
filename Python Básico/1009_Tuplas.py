#   TUPLA
numeros = (10, 20, 30, 40, 50)
print(numeros)

# Desempaquetado de la tupla
num_1, num_2, num_3, *resto = numeros

print(num_1)
print(num_2)
print(num_3)
print(resto)