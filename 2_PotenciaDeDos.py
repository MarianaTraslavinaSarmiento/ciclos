#Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:

potencia = int(input("Ingrese num: "))
for i in range(potencia + 1):
    answer = 2**i
    print(answer, end= " ")
    