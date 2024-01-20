#Programa que imprima la secuencia de Collatz de un numero entero:

def punto1():
    
    num = int(input("n: "))

    while num!=1:
        print(int(num), end=" ")
        if num%2==0:
            num = num/2
        else:
            num = 3*num+1
            
    print(1)

punto1()


#Programa que grafique los largos de las secuencuas de collatz de los numeros enteros positivos menores que el ingresado por el usuario:

def punto2():

    n = int(input("n: "))

    for I in range (1, n+1):
        new = I
        asteriscos = 1
        while new!=1:
            if new%2==0:
                new=int(new/2)
                asteriscos += 1
            else:
                new=(new*3+1)
    
        print(I, asteriscos*"*")

punto2()




