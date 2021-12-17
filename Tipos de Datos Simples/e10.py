#Ejercicio 10

#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

muñeca_peso = 75
payaso_peso = 112

muñeca = int(input("Introduzca la cantidad de muñeca: "))
payaso = int(input("Introduzca la cantidad de payaso: "))

peso_total = payaso * payaso_peso + muñeca * muñeca_peso

print(f"\nEl peso total del paquete es: {peso_total}g")

