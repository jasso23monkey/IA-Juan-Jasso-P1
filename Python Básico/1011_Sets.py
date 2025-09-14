psitacidos_latinos = {"Guacamaya", "Loro", "Perico", "Cotorra"}
psitacidos_asiaticos = {"Perico"} # Un set con un solo elemento

print(psitacidos_latinos)
print(psitacidos_asiaticos)

psitacidos_latinos.add("Guacamaya Roja")
psitacidos_latinos.add("Loro")

psitacidos_latinos.remove("Perico")
print(psitacidos_latinos)

psitacidos_asiaticos.discard("Cacatua")
print(psitacidos_asiaticos)

cant_psitacidos_latinos = len(psitacidos_latinos)
cant_psitacidos_asiaticos = len(psitacidos_asiaticos)
print("La cantidad de psitacidos latinos son: ", cant_psitacidos_latinos)
print("La cantidad de psitacidos asiaticos son ", cant_psitacidos_asiaticos)

latinos_min = min(psitacidos_latinos)
latinos_max = max(psitacidos_latinos)
print("El primer psitacido alfabeticamente es: ", latinos_min)
print("El ultimo psitacido alfabeticamente es: ", latinos_max)

psitacidos_fav = frozenset(["Agapornis", "Guacamaya"])
print(psitacidos_fav)
