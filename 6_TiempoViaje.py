
#Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos. El programa deja de pedir tiempos de viaje cuando se ingresa un 0.

viaje_total = []
detener = 0

while True:
    tramos = int(input("Ingrese el tramo: "))
    
    if tramos == detener:
        break
        
    viaje_total.append(tramos)
    print(viaje_total)

suma = sum(viaje_total)
hora = int(suma/60)
minutos = suma%60

print(f"Tiempo total de viaje: {hora}:{minutos}")

