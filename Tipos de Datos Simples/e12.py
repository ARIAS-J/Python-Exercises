#Ejercicio 12

#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

precio_habitual = 3.49

descuento = 0.6

barra_pan = int(input("Introducir la cantidad de barras vendidas que no son frescas: "))

coste_final = barra_pan * precio_habitual * (1 - descuento)

print(f"\nEl precio de una barra fresca es: {precio_habitual}", f"\nEl descuento de una barra no fresca es: {descuento*100}%", f"\nEl coste final a pagar es: {round(coste_final,2)}")
