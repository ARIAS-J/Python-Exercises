#Ejercicio 4

#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = int(input("Ingresar un numero entero: "))

if numero % 2 == 0:
    print(f"{numero} Es par")
else:
    print(f"{numero} Es impar")