import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

"""Pregunta 1
1.  V.Independiente: unidades 
    V. Dependiente: tiempo (esta en segundos)
Pregunta 2
Dominio contextualizado son los valores que puede tomar n de 0 a 1562 elementos"""

#pregunta 3
def A(n):
    return 0.01*n**2+0.5*n+2
print(f"Tiempo de ejecucion para ordenar 1.200 elementos es de {A(1200)/3600:.0f} horas") #el ejercicio esta en segundos y hay que pasarlo a horas

#Pregunta 4
def A(n):
    return 0.01*n**2+0.5*n+2

n = np.arange(0,1562,1)

plt.plot(n, A(n),color='purple')
plt.title('Algoritmo')
plt.xlabel('Unidades')
plt.ylabel('Tiempo')

plt.grid(True)
plt.show()

#pregunta 5
def E(n):
    return 0.01*n**2+0.5*n+2-21600 #aqui se iguala a 0, son 21600 segundos por que son 6 horas
n = np.linspace(0,100,1)
sol = fsolve(E,n)
print(f"Elementos ordenados {sol[0]:.0f} en 6 horas")