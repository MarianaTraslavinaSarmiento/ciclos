#Escriba un programa que pida al usuario ingresar la el tamaño de las siguientes figuras geometricas: Rectangulo - Triangulo y hexagono

def rectangulo():

    print("RECTANGULO")
    altura = int(input("Altura: "))
    ancho = int(input("Ancho: "))

    for X in range(altura):
        for k in range(ancho):
            
            print("*", end=" ")
        print("", end="\n")
    
rectangulo()

def triangulo():
    
    print("TRIANGULO")
    altura = int(input("Altura: "))
    
    for X in range(1, altura+1):
        print("*"*X)

triangulo()

def hexagono():
    
    print("HEXAGONO")
    cantidad_lados = int(input("Lado :"))
    
    for X in range(cantidad_lados):
        nu = str("*"*(cantidad_lados+(2*X)))
        print(nu.center(30))
        
    partir_hexagono = (nu.count("*"))/2
    for X in range(int(partir_hexagono-2)):
        nu = nu[:-2]
        if nu.count("*")==cantidad_lados-2:break
        print(nu.center(30))

hexagono()

