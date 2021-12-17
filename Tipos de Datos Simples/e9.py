#Ejercicio 9

#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

capital_inicial = int(input("Cuanto desea invertir: "))
interes_anual = int(input("interes anual(porcentaje): "))
años = int(input('Años: '))

capital_final = round(capital_inicial*(interes_anual / 100 + 1)**años,2)

print('\nCapital obtenido es: ',capital_final)