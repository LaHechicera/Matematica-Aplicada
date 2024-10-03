"""
El tiempo de ejecución de un algoritmo de ordenación (en segundos) se puede modelar mediante la función:

A(n)=0,01n2+0,5n+2

donde n corresponde a la cantidad de elementos a ordenar. El algoritmo funciona desde las 23:00 horas hasta las 06:00 horas y debe ordenar 1.562 elementos.

1. Defina variable dependiente e independiente, indicando unidad de medida.
2. Determine el dominio contextualizado de la función.
3. Determine el tiempo de ejecución para ordenar 1.200 elementos.
4. Grafique, utilizando la biblioteca Matplotlib, la función A(n).
5. ¿Cuántos elementos ordena luego de 6 horas de funcionamiento?

"""
#Pregunta 1
"V.I.: Unidades  V.D.: Tiempo"

#Pregunta 2
"Dominio contextualizado 0 a 1.562"

#Pregunta 3
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

def A(n):
    return 0.01*n**2+0.5*n+2
print(f"Tiempo para ordenar 1200 elementos es {A(1200/3600):.1f} horas")

#Pregunta 4
def A(n):
    return 0.01*n**2+0.5*n+2

n = np.arange(0,1562,1)

plt.plot(n, A(n),color='purple')
plt.title('La ordenacion')
plt.xlabel('Unidades')
plt.ylabel('Tiempo')

plt.grid(True)
plt.show()

#Pregunta 5
def A(n):
    return 0.01*n**2+0.5*n+2 - 21600

n = np.linspace(0,100,1)
sol = fsolve(A,n)

print(f"Luego de 6 horas ordena {sol[0]:.1f} elementos")