#Escriba un programa que entregue todos los divisores del número entero ingresado:

num = int(input("Número ingresado: "))
divisores = []

for ejercicio in range (1, num+1):
    if  num%ejercicio == 0:
        
        divisores.append(ejercicio)
        
print(f"los divisores de {num} son {divisores}")
