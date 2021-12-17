#Ejercicio 6

#Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N  primeros enteros positivos puede ser calculada de la siguiente forma: suma = n(n+1)/2

n = int(input("Introduzca n entero positivo: "))

suma = n *(n + 1) / 2

print(f"la suma  de los primeros numeros enteros del 1 hasta {n} es: {suma}")