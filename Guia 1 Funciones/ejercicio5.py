"""

Un turista ha llegado a Santiago y desea conocer algunos lugares de la ciudad. Ha decidido visitar el Palacio de la Moneda y desde ahí trasladarse al centro comercial 
"Costanera Center", utilizando algún medio de transporte que ofrece la ciudad.

Si se traslada en metro deberá abordar en estación La Moneda y bajar en la estación Tobalaba (9 estaciones). La función f(t) permite calcular la distancia recorrida 
utilizando el metro (en kilómetros) transcurridos t minutos.

f(t)=0,4t

Si se traslada en bus, el turista podrá observar la ciudad y otros atractivos en su viaje. La función g(t) permite calcular la distancia recorrida en bus (en kilómetros) 
transcurridos t minutos.

g(t)=0,3t

Según la información anterior:

1 Grafique ambas funciones, indicando el nombre de cada eje junto con su unidad de medida. Para realizar el gráfico utilice la biblioteca Matplotlib.
2 Si se sabe que el metro se demora 1,2 minutos en llegar desde una estación a otra y espera 30 segundos en cada estación, indique el dominio contextualizado para f(t).
3 Mediante análisis gráfico, indique cuál medio de transporte es más conveniente en términos de tiempo, para el turista. Justifique.
4 Si se sabe que desde estación La Moneda hasta Tobalaba son aproximadamente 6 kilómetros ¿cuántos tiempo tardará el turista en llegar a su destino con cada una de las opciones?

"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

#Pregunta 1
def F(t):
    return 0.4*t
def G(t):
    return 0.3*t

t = np.arange(0,9,1)

plt.plot(t, F(t))
plt.plot(t, G(t))

plt.title('Titulo')
plt.xlabel('Distancia')
plt.ylabel('Tiempo')

plt.grid(True)
plt.show()

#Pregunta 2
"El dominio contextualizado es de 15.3"

#Pregunta 3
"El bus por que se recorre mas distancia en menos tiempo"

#Pregunta 4
def F(t):
    return 0.4*t-6

def G(t):
    return 0.3*t-6

t = np.linspace(0,100,1)

sol = fsolve(F,t)
sol1 = fsolve(G,t)

print(f"El tiempo que se demorara en metro serian {sol[0]:.1f}")
print(f"El tiempo que se demorara en bus serian {sol1[0]:.1f}")