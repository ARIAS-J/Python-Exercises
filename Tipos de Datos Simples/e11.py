#Ejercicio 11

#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

ahorro = float(input("Ingresar la cantidad que desea depositar: "))

interes = 0.04

balance_primeraño = ahorro * (1 + interes)
balance_segundoaño = balance_primeraño * (1 + interes)
balance_terceraño = balance_segundoaño * (1 + interes)

print(f"\nEl balance tras el primer año es: {round(balance_primeraño,2)}", f"\nEl balance tras el segundo año es: {round(balance_segundoaño,2)}", f"\nEl balance tras el tercer año es: {round(balance_terceraño,2)}")