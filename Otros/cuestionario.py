import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

#Pregunta 1
def r(x):
    return 1.4*x**2-5.6*x+12.6 

def s(x):
    return -1.6*x**2+1.3*x+141.3

def f(x):
    return r(x)-s(x)

j = np.linspace(-10,10,2)#Recordar que aqui busca los rangos
sol = np.around(fsolve(f ,j), decimals=2) 
print(f"El rango de tiempo es {sol}")

#Pregunta 2
def U(x):
    return 150*x+100

print("Rango es de 0 a 15")

#Pregunta 3 (Cuando me dan la V.D. se resta se iguala a 0)
def D(t):
    return 50*np.exp(0.3*t)-551

t = np.linspace(0,1,1)
sol=fsolve(D,t)

print(f"En {sol[0]:.0f} meses alcanzara 551 terabytes")

#pregunta 4
def D(t):
    return 50*np.exp(0.3*t)

print(f"En 6 meses se almacenaran {D(6):.1f} terabytes")

#Pregunta 7
def M(x):
    return x**3-4*x**2+5*x

print(f"El uso de memoria cuando hay 10 objetos es {M(10):.1f}")

#Pregunta 8
def C(n):
    return 50*n+200-1500

n = np.linspace(0,1,1)
sol= fsolve(C,n)

print(f"Se procesaron {sol[0]:.0f} terabytes con un costo de 1500 dolares")

#pregunta 9
def C(n):
    return 50*n+200

print(f"El costo de procesamiento de 20TB son {C(20):.1f} dolares")

#pregunta 10
def f(x):
    return 1-2*x

x = np.arange(-5,5,0.01) 

plt.plot(x, f(x), label = 'h(x)', color='purple')


plt.title('Grafico')
plt.xlabel('X' )
plt.ylabel('Y')

plt.xlim(-5,10)
plt.ylim(-5,20)

plt.legend()
plt.grid(True)
#plt.show()

#pregunta 11
def S(n):
    return 2*n**2+3*n+5-500

n = np.linspace(0,1,1)
sol= fsolve(S,n)

print(f"En 500 GB se obtuvieron {sol[0]:.0f} registros")


#pregunta 12
def S(n):
    return 2*n**2+3*n+5
print(f"{S(50):.1f}")