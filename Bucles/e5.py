#Ejercicio 5
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

inversion = float(input("Ingrese cantidad a invertir: "))
interes = int(input("Ingrese el interes: "))
tiempo = int(input("Ingrese cantidad a invertir: "))

for i in range(1,tiempo + 1):
    print(f"\n El Capital optenido en el año {i} es: {round(inversion*(interes / 100 + 1)**i, 2)}")
