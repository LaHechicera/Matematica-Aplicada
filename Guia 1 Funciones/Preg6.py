#Pregunta 1:
"V.I.: Horas V.D.: Grados"

#Pregunta 2:
"Dominio contextualizado es 9"

#Pregunta 3:
def T(t):
    return -0.5*t**2+3*t+20

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker #sirve para decirle al grafico que vaya de cierto numero en numero
import numpy as np
fig, ax = plt.subplots()

t = np.arange(0,9,0.01)

plt.plot(t, T(t))
plt.title('Temperatura servidor')
plt.xlabel('Tiempo transcurrido (horas)')
plt.ylabel('Temperatura (C°)')

plt.grid(True)#Sirve para mostrar cuadriculas en el grafico si se pone False no se veran las cuadriculas

ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))

plt.show()

#Pregunta 4: Se llama a la funcion y se reemplaza
def T(t):
    return -0.5*t**2+3*t+20

print(f"Transcurridas 3 horas la temperatura máxima del servidor es de {T(3):.1f} °C")

#Pregunta 5: 
def T(t):
    return -0.5*t**2+3*t+20
print(f"A las 13:00 hrs la temperatura del servidor es de {T(5):.1f} °C")
print(f"A las 17:00 hrs la temperatura del servidor es de {T(9):.1f} °C")

