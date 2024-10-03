"""m: Pendiente de funcion lineal es el grado de inclinacion respecto al eje Y
n: coeficiente de posicion (el valor inicial) es el que intersecta la recta con el eje Y

Funcion lineal (expresion algebraica)
f(x)=m*x+n

"""

import numpy as np

VINDEP = np.array([1.6,1.92,2.16,2.56])
VDEP = np.array([2,2.4,2.7,3.2])

#Siempre debe estar estas variables ya que estamos sacando la m (pendiente) y n 
pendiente, intercepto = np.polyfit(VINDEP,VDEP,1) #Aqui colocamos 1 por que le indicamos al programa que lo ajuste a un polinomio 
#de grado 1 es decir una funcion lineal

print(f"La pendiente de la funcion es {pendiente:.1f} y el intercepto es {intercepto:.1f}.")

#La funcion lineal es f(x) = 1.25x en el ejercicio anterior (Para dejarlo centrado en colab es $$ f(x) = 1.25x $$)


#Pregunta 2:

unidades = np.array([100,200,500,1000,2000])
milisegundos = np.array([2,4,10,20,40])

pendiente, intercepto = np.polyfit(unidades,milisegundos,1)

print(f"La pendiente de la funcion es {pendiente:.2f} y el intercepto es {intercepto:.2f}.")