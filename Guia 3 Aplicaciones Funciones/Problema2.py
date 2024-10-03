import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

#Problema 2: Graficar 2 funciones, una cuadratica y otra lineal

def h(x):
    return 2*(x-2)**2

def i(x):
    return x+1

x = np.arange(0,100,0.01) #En variablle independiente se le asigna un arreglo

plt.plot(x, h(x), label = 'h(x)', color='purple')
plt.plot(x, i(x), label = 'i(x)', color='red')

plt.title('Grafico')
plt.xlabel('X' )
plt.ylabel('Y')

#Delimitan las lineas de 0 a 20
plt.xlim(-5,10)
plt.ylim(0,20)

plt.legend()
plt.grid(True)
plt.show()

#Para graficar o buscar los puntos de interseccion
#Se restan las funciones, siempre la funcion de mayor exponente va primero y luego la menor
#Hay que definir una nueva funcion e igualar a 0 las funciones

#Solo nos ayuda a encontrar las coordenadas x de las funciones
def F(x):
    return h(x) - i(x)

j = np.linspace(0,10,10)

#En este tipo de problemas para buscar los puntos de interseccion es necesario resolver asi
sol = np.around(fsolve(F ,j), decimals=2) #np.around descarta las soluciones que se repiten
#Decimals se define en base a la funcionde mayor exponente en este caso una funcion cuadratica (2)
unica = np.unique(sol)
print(unica)

#Para encontrar coordenadas y se deben definir o reemplazar la x
print(f"Las coordenadas del primer punto son: (1 ,{i(1)}) y las coordenadas del segundo punto son: (3.5, {h(3.5)})")


#pregunta 5
#h(x)=50, aqui hay que igualar a 0

def h(x):
    return (2*(x-2)**2) - 50

x = np.linspace(-200,200,4)
sol = np.around(fsolve(h ,x), decimals=2)
#Molto importate
inter = np.unique(sol)
print(f"El punto en que la funcion es 50 es {inter}")