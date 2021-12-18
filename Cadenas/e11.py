#Ejercicio 11

#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

producto = input("Ingresar nombre del producto: ")

precio = float(input("Ingresar precio del producto: "))

unidades = int(input("Ingresar unidades del producto: "))

print("{producto}: {unidades:3d} por {precio:9.2f}$ = {total:11.2f}".format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))