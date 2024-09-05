#horas a minutos
print("Horas a minutos")
horas = int(input("Ingrese las horas a transformar en minutos: "))
minutos = horas*60
print(f"La hora en minutos es {minutos}")

#horas a segundos
print("Horas a segundos")
horas = int(input("Ingrese las horas a transformar en segundos: "))
segundos = horas*3600
print(f"La hora en segundos es {segundos}")

#minutos a horas
print("Minutos a horas")
min1 = int(input("Ingrese los minutos a transformar en horas: "))
hora1 = min1/60
print(f"La hora en minutos es {hora1:.1f}")

#segundos a horas
print("Segundos a horas")
seg1 = int(input("Ingrese los segundos a transformar en horas: "))
hora2 = seg1/3600
print(f"La hora en minutos es {hora2:.1f}")