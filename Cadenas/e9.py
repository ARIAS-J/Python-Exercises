#Ejercicio 9

#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

nacimiento = input("Introduzca su fecha de nacimiento(dd/mm/aaaa): ")

print(f"\nFecha de nacimiento Dia: {nacimiento[:2]} Mes: {nacimiento[3:5]} Año: {nacimiento[6:]}")

dia = nacimiento[:nacimiento.find("/")]
mesaño = nacimiento[nacimiento.find("/")+1:]
mes = mesaño[:mesaño.find("/")]
año = mesaño[mesaño.find("/")+1:]

print(f"Fecha de nacimiento Dia: {dia} Mes: {mes} Año: {año}")