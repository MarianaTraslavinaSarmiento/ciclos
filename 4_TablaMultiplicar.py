# Escriba un programa que muestre una tabla de multiplicar como la siguiente:


for numero in range(1,11):
    for multiplicar in range(1,11):
        answer = numero * multiplicar
        print(str(answer).rjust(3), end= " ")
    print("\n")