#Ejercicio 10
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

numero = int(input("Ingrese un numero entero: "))

i = 2

while numero % i != 0:
    i += 1
if i == numero:
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")
