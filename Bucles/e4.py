#Ejercicio 4
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

entero = int(input("Ingrese un numero entero: "))

for i in range(entero + 1):
    print(entero)
    entero -= 1