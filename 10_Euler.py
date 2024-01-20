
#Desarrolle un programa que entregue un valor aproximado de e, calculando esta suma hasta que la diferencia entre dos sumandos consecutivos sea menor que 0,0001.

from math import factorial


euler = 0
iteracion = 0
X = 0
suma = 1
while abs(X-suma) >= 0.0001: #Abs imprime el valor absoluto de  0-1 = -1 POR LO TANTO el valor absoluto es 1
    iteracion += 1 
    X = suma #convertimos X(0) a suma(1)
    suma += 1/factorial(iteracion)

print(suma)
