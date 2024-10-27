import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

#Pregunta 3
x = np.array([6000, 24000, 42000, 60000])
y = np.array([3000, 12000, 21000, 30000])
#Si la función es de grado 1
pendiente, intercepto = np.polyfit(x, y, 1)

#print(f"{pendiente:.1f }{intercepto:.1f}")

#Pregunta 6
def l(x):
    return 40*x+0.5*x**2

def c(x):
    return 15*x+232

def F(x):
    return l(x)-c(x)

x = np.linspace(1,100,2)
solucion = fsolve(F,x)
print(solucion)


#Pregunta 7
def c(x):
    return 10*x+450-600

x = np.linspace(1,100,1)
solucion = fsolve(c,x)
print(solucion)

def l(x):
    return 50*x+0.5*x**2

print(l(15))

#Pregunta 8
