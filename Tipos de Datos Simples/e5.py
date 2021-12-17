#Ejercicio 5

#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas = float(input("Numero de horas trabajadas: "))
coste = float(input("Coste por hora: "))

paga = horas * coste

print(f"La paga correspondiente es: {paga}")


