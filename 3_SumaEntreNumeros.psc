Algoritmo SumaEntreNumeros
	
	escribir "Ingrese un numero"
	leer n1
	escribir "Ingrese un numero"
	leer n2
	
	sumando = 0
	para i<-n1+1 hasta n2-1 con paso 1 Hacer
		sumando <- sumando + i
	FinPara
	
	escribir "La suma es ", sumando
FinAlgoritmo
