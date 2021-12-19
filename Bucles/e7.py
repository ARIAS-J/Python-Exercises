#Ejercicio 7
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for i in range(1, 10 + 1):
    for j in range(1, 10 + 1):
        print(i * j, end="\t")
    print("")
