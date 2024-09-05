def g(t):
    return 1.85*t

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

t = np.arange(0,3569,1)#aqui le decimos que va desde 0 a 3568 de 1 en 1

plt.plot(t, g(t))

plt.title('Relacion entre el largo del cable instalado y el tiempo transcurrido')
plt.xlabel('Tiempo transcurrido (horas)')
plt.ylabel('Largo  del cable instalado (km)')

plt.grid(True)#Sirve para mostrar cuadriculas en el grafico si se pone False no se veran las cuadriculas
plt.show()#muestra el grafico


#otra pregunta 5
def f(x):
    return 1.85*x
sol = f(148)
print(f"Se instalaron {sol:.1f} metros de cable")

#pregunta 6
def f(x):
    return 1.85*x-3480

x = np.linspace(0,100,1)#para que busuqe el valor de X, hace recorrido de 0 a 100
sol = fsolve(f,x)
print(f"Llevan {sol[0]:.0f} horas de trabajo")


#pregunta 7

def f(x):
    return 1.85*x-6600
x = np.linspace(0,100,1)
sol = fsolve(f,x)

def f(t):
    return 0.4*t+30