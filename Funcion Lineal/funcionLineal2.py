"""En funciones siempre encontraremos Variables independiente y dependiente
Ej: f(x) = mx + n
* f(x) : V.D.
* x : V.I.
* m : pendiente
* n : intercepto (interseccion de X e Y)
"""

#P.2
import numpy as np

gb = np.array([5,10,25,50,100])
ms = np.array([10,20,50,100,200])

pendiente, intercepto = np.polyfit(gb,ms,1)

print(f"La pendiente de la funcion es {pendiente:.1f} y el intercepto es {intercepto:.1f}.")

def T(x):
    return 2*x
print(f"En 73,2 GB toma {T(73.2):.1f} de tiempo de transferencia")

import numpy as np
from scipy.optimize import fsolve

#p. 5
def T(x):
    return 2*x-123.5

x = np.linspace(0,100,1)
sol = fsolve(T,x)
print(f"Cantidad de datos transferidos en 123,5 minutos es de {sol[0]:.0f}")