#Pregunta 1
#a)primeros 5 terminos
a=[]
for i in range (5):
    n=i+1
    a.append(3*n**2+7) 
    print(f'a_{n}={a[i]:.1f}')
print(" ")

#b)5 terminos despues del decimoquinto
a=[]
for i in range (5):
    n=i+16
    a.append(3*n**2+7) 
    print(f'a_{n}={a[i]:.1f}')
print(" ")

#Pregunta 2
#a) primeros 4 terminos de una sucesion
g=[]
for i in range (4):
    n=i+1
    g.append(5*n**3) 
    print(f'g_{n}={g[i]:.1f}')
print(" ")

#b) 4 terminos que vienen inmediatamente despues del octavo termino
g=[]
for i in range (4):
    n=i+9
    g.append(5*n**3) 
    print(f'g_{n}={g[i]:.1f}')
print(" ")

#c) Determinar si el termino 40.000 pertenece a la sucesion. Sies asi indicar posicion
final=40000 
termino=0
n=0

dif=final-termino
while dif > 0:
    n+=1
    termino = 5*n**3
    dif = final-termino
if dif == 0: #Si da 0 es decir si el numero 40000 esta en la sucesion este se resta con el mismo 40000
    print(f"El termino 40000 esta en la sucesion y esta en la posicion {n}")
else:
    print("Termino 40000 no pertenece a la sucesion")
print(" ")

"""RAZON AUREA"""

#Pregunta 4
#2*n
#1 cual es el valor del decimo termino?
h=[]
for i in range (100):
    n=i+1
    h.append(2*n) 
    if n==10:
        print(f"El decimo termino es {h[i]}")
print(" ")

#2 Calcula utilizando un ciclo for, la suma de los primeros 100 numeros 

suma = sum(h)
print(f"La suma de los 100 primeros numeros de la sucesion es {suma}")
print(" ")

#3 en que pisicion se encuentra el termino 58
final = 58
termino = 0
n=0

dif=final-termino
while dif > 0:
    n+=1
    termino = 2*n
    dif = final-termino
print(f"La posicion de 58 esta en la posicion {n}")
print(" ")

#PREGUNTA 5
"Susesion geometrica"
"Razon constante de 1.15 por que queremos aumentar en un 15% osea que de a nuestro 100% le sumaremos el 15% osea 115% = 1.15"

r=1.15
a_1=500*r
usuarios=[]

for i in range(12):
    n=i+1
    usuarios.append(a_1*r**(n-1))
    print(f"Mes {n} = {usuarios[i]:.0f} usuarios")

suma=sum(usuarios)
print(f"Luego de un año el software tendra {suma:.0f} usuarios")

#Pregunta 6
d=2000
a_2=12000
ahorro=[]

for i in range(24):
    n=i+1
    ahorro.append(a_2+(n-1)*d)
    print(f"Mes {n} = {ahorro[i]:.0f} ahorros")

#Pregunta 7
r = 0.9
a_1 = 3
a_5=a_1*r**4

print(f"La quinta fase dura {a_5:.1f} meses")

lista=[]
for i in range (10):
    n=i+1
    lista.append(a_1*r**(n-1))
suma=sum(lista)
print(f"la duracion total luego de 10 fases es {suma:.1f} meses")

#Pregunta 8 
