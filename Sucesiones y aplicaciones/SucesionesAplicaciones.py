"""
Suceciones

- Aritmeticas -> Existe una diferencia constante (Ej. de 3 en 3 o de 2 a 2 etc.) se va sumando un valor constante
- Geometricas -> Existe una razon constante (Ej: multipicacion * 2) se va multiplicando con un valor constante
"""

#En este codigo podemos ver como declarar una lista acotada y luego ir recorriendo sus elementos

print("\nMostrar elementos de una sucesion\n")
b=[6,9,12,15]

for i in range (len(b)):
    n=i+1
    print(f'b_{n}={b[i]}') #Guion es sub (ej: B sub 1 seria "B_1")


print("\nGenerar los 4 primeros terminos de una sucesion\n")

a=[]
for i in range(4): #Aqui varia el numero dependiendo de la cantidad de numeros que queramos mostrar
    n=i+1
    a.append(3*n) #Aqui le decimos el tipo de sucesion numerica Ej: que vaya de 3 en 3
    print(f'a_{n}={a[i]}')


print("\nGenerar elementos ubicados desde la posicion 10 hasta la 15\n")

b=[]
for i in range (6):
    n=i+10 #Este es el que cambia para saber desde que sub B buscar, si cambio a 5 buscara de 5 al 10 dependiendo del rango
    b.append(5*0.92**n) #Esta formula la dan
    print(f'b_{n}={b[i]:.1f}')


print("\nPosicion que ocupa un termino en una secuencia\n")

final=10807 #Declaramos que numero queremos buscar
termino=0
n=0

dif=final-termino
while dif > 0:
    n+=1
    termino =3*n**2+7
    dif = final-termino
print(f"El termino 108077 esta en la posicion {n}")


print("\nEl 7mo termino de una posicion aritmetica\n")

a_1 = 3 #a sub 1
d = 2 #d diferencia aritmetica, que va de 2 en 2
n = 7 # es la posicion 7, que numero se encuentra en el a_7

a_7 = a_1+(n-1)*d
print(f"El septimo termino de la sucesion es {a_7}")


print("\nComo sumar los 10 primeros elementos de una sucesion aritmetica\n")

elementos = []
a_1 = 3
d = 2
for i in range(10):
    n = i+1
    elementos.append(a_1+(n-1)*d)
    suma = sum(elementos)
print(f"La suma total de los elementos es {suma}")
