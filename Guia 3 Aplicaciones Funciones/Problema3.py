import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

"Pregunta 1"

def w(x):
    return 0.6*x**2+1.5

def t(x):
    return 0.8*x**3-10*x+10

x = np.arange(-20,10,0.01) 

plt.plot(x, w(x), label = 'w(x)', color='purple')
plt.plot(x, t(x), label = 't(x)', color='red')

plt.title('Grafico')
plt.xlabel('X' )
plt.ylabel('Y')

plt.xlim(-3,4)
plt.ylim(-4,24)

plt.legend()
plt.grid(True)
plt.show()


"Pregunta 2"
def F(x):
    return t(x) - w(x)

j = np.linspace(0,10,10)
sol = np.around(fsolve(F ,j), decimals=2) 
unica = np.unique(sol)
print(unica)


"Pregunta 3"
def t(x):
    return 0.8*x**3-10*x+10 - 6

x = np.linspace(-200,200,4)
sol = np.around(fsolve(t ,x), decimals=3)
inter = np.unique(sol)
print(f"El punto en que la funcion en 6 es {inter}")