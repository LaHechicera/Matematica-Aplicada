import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve



VINDEP= np.array([1,2,4,5,8])
VDEP= np.array([10,20,40,50,80])

pendiente, intercepto = np.polyfit(VINDEP,VDEP,1)

#PREGUNTA 1: Determina la forma algebraica de la funcion que modela la distancia recorrida por el atleta 2 en funcion 
#del tiempo ¿Que tipo de funcion es?

print(f"La pendiente de la funcion es {pendiente:.1f} y el intercepto es {intercepto:.1f}.")

#Cuando nos piden determinar forma algebraica se refiere a sacar la pendiente e intercepto y se utiliza esta formula
"Respuesta: Atleta 2: f(t) = 10t" #En este caso intercepto es 0.0 asi que no se anota, en el caso de que el intercepto
#tuviera valor la funcion quedaria "f(t) = 10t + 2(aqui cualquier valor que de resultado)"

#PREGUNTA 2: A que distancia distancia se encontraban uno del otro cuando transcurren 8 segundos?
"Cuando preguntan por cierta variable (en este caso DISTANCIA) ese seria el resultado que buscamos, tal como aparece mas abajo"

def g(t):
    return 0.7*t**2

def f(t):
    return 10*t

print (f"El primer atleta se encontraba a una distancia de {g(8):.1f} km y el segundo a {f(8):.1f} km")

#PREGUNTA 3: Cuanto tiempo a transcurrido para que los atletas se vuelvan a encontrar? Que distancia llevan recorrida?
def F(t):
    return g(t) - f(t)

j = np.linspace(0,10,2) #Se le pone 2 ya que es una funcion de grado 2
sol = np.around(fsolve(F ,j), decimals=2) 
#unica = np.unique(sol)
print(sol)



#PRENGUTA 4: En que periodo el atleta 1 es mas rapido que el atleta 2?
def g(t):
    return 0.7*t**2

def f(t):
    return 10*t

t = np.arange(0,20,0.5) 

plt.plot(t, g(t), label = 'g(t)', color='purple')
plt.plot(t, f(t), label = 'f(t)', color='red')

plt.title('Distancia recorrida por atletas')
plt.xlabel('Tiempo' )
plt.ylabel('Distancia')

plt.xlim(0,20)
plt.ylim(0,20)

plt.legend()
plt.grid(True)
plt.show()