#Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario:

numero1 = int(input("¿Cual tabla deseas ver?: "))

for i in range(1,11):
    product = numero1 * i
    print(f"{numero1} x {i} = {product}")


