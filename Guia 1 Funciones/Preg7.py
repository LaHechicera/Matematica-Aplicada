import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

"""Pregunta 1: Defina variable dependiente e independiente, indicando unidad de medida.
VI: Tiempo (Tiempo en meses)
VD: Cantidad Usuarios (Cantidad de usuarios en unidades)"""

#pregunta 2: Determine la cantidad de usuarios transcurridos 12 meses.
def U(t):
    return 1000/(1+9*np.exp(-0.5*t))

print(f"Transcurridos 12 meses, la cantidad de usuarios es {U(12):.0f} Usuarios aproximadamente")

#pregunta 3: Grafique la función, utilizando la librería Matplotlib, para los primeros dos años de funcionamiento.
def U(t):
    return 1000/(1+9*np.exp(-0.5*t))

t = np.arange(0,24,1)#es un rango de numeros, pasa de uno en uno para encontrar el numero correcto 

plt.plot(t, U(t))
plt.plot(t, U(t))
plt.plot(t, U(t))
plt.plot(t, U(t))
plt.plot(t, U(t)) #el quinto es purpura :v

plt.title('Años de funcionamiento')
plt.xlabel('Tiempo transcurrido (meses)')
plt.ylabel('Usuarios a traves de los años')

plt.grid(True)
plt.show()

#pregunta 4: ¿Cuánto tiempo debe pasar para que la red social llegue a 800 usuarios?
def U(t):
    return 1000/(1+9*np.exp(-0.5*t)) - 800

t = np.linspace(0,100,1) #cuenta de 0 a 24, guarda un numero especifico
sol = fsolve(U,t)

print(f"Deben pasar {sol[0]:.1f} meses para alcanzar los 800 usuarios")