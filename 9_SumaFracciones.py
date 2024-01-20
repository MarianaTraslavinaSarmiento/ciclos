
#Programa que permita trabajar con las potencias fraccionales entre dos

fraccion = 1
exponente = 1
suma = 0
print("Potencia    Fraccion     Suma ")

while fraccion>0.000001:
    fraccion = 1/2**exponente
    suma +=fraccion
    print(str(exponente).ljust(8), str(round(fraccion, 7)).center(10), str(round(suma, 7)).rjust(10))
    exponente+=1







