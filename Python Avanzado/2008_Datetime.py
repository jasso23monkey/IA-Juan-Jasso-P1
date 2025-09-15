import datetime
import locale


# Se crea un objeto de tipo time
hora = datetime.time(14, 30, 20, 656)
# Se imprimen varios de sus atributos
print(f"Hora: {hora.hour}")
print(f"Minutos: {hora.minute}")
print(f"Segundos: {hora.second}")
print(f"Microsegundos: {hora.microsecond}")

#Se crea un objeto de tipo date
fecha = datetime.date(2027,12,20)
#Se imprime la fecha almacenada
print(f"Año: {fecha.year}")
print(f"Mes: {fecha.month}")
print(f"Día: {fecha.day}")


hora_actual = datetime.datetime.now()
print(hora_actual)

fecha_hoy = datetime.date.today()
print(fecha_hoy)

locale.setlocale(locale.LC_ALL, "es")
fecha_ahora = datetime.datetime.now()
fecha_formateada = fecha_ahora.strftime("%A, %d de %B de %Y a las %H:%M").capitalize()
print(fecha_formateada)