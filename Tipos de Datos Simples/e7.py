#Ejercicio 7

#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso = input("Introduzca su peso en (kg): ")
estatura = input("Introduzca su estatura en (metros): ")

imc = round(float(peso)/float(estatura)**2,2)

print(f"Tu Indice de masa corporal(imc) es: {imc}")