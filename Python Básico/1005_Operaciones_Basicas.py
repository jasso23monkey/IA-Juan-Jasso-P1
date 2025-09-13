# --- Variables iniciales del luchador ---
fuerza = 15.5
agilidad = 10
tecnica = 8
carisma = 20
nivel = 2.2

# --- Operaciones ---
#   SUMA
combo_simple = fuerza + tecnica
print("Los puntos de combo son:", combo_simple)

#   RESTA
diferencia = fuerza - tecnica
print("Los puntos de diferencia son:", diferencia)

#   MULTIPLICACION
ataque_especial = agilidad * nivel
print("Los puntos del ataque especial son:", ataque_especial)

#   DIVISION
reaccion_publico = carisma / fuerza
print("Los puntos de la reaccion del publico son:", reaccion_publico)

#   MODULO
residuo_agilidad = agilidad % nivel
print("Los puntos de residuo de agilidad son:", residuo_agilidad)

#   POTENCIA
tecnica_aerea = tecnica ** nivel
print("Los puntos de tu tecnica area son:", tecnica_aerea)

#   OPERACIÓN COMPLEJA
puntaje_final = (fuerza + agilidad ** nivel) - (tecnica // nivel) + carisma
print("Tu puntaje final como luchador es: ", puntaje_final)