def f(x):
    return 30*x+8

imagen = f(50)
print(imagen)

#Basico para hacer un ejercicion en matematica
import numpy as np
from scipy.optimize import fsolve

def f(x):
    return 10*x+80
x = np.linspace(0,100,1) #linspace es el valor que se le dara a la X
sol = fsolve(f,x)

print(sol[0])


def f(x):
    return 1.85*x-6600
x = np.linspace(0,100,1)
sol = fsolve(f,x)

print(f"El dominio va desde 0 hasta {sol[0]:.0f} horas")