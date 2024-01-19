#Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están entre ellos. Por ejemplo, si los números son 1 y 7, debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20."

n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese un número: "))

sumando = 0 
for i in range(n1+1,n2):
    sumando += i

print(f"La suma es {sumando}")
