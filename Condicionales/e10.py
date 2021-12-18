#Ejercicio 10

#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

    #Ingredientes vegetarianos: Pimiento y tofu.
    #Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

opcion = int(input("\nSeleccione su pizza (Opcion 1: Pizza vegetariana : Opcion 2: Pizza no vegetariana): "))

if opcion == 1:
    ingrediente = int(input("Seleccion el ingrediente: \n\t1-(Pimiento \n\t2-(Tofu \n\tOpcion:"))
    if ingrediente == 1:
        print(f"Pizza Vegetariana con mozzarella, tomate y Pimiento")
    else:
        print(f"Pizza Vegetariana con mozzarella, tomate y Tofu")
else:
    ingrediente = int(input("Seleccion el ingrediente: \n\t1-(Peperoni \n\t2-(Jamón \n\t3-(Salmón \n\tOpcion:"))
    if ingrediente == 1:
        print(f"Pizza No vegetariana con mozzarella, tomate y peperoni")
    elif ingrediente == 2:
        print(f"Pizza No vegetariana con mozzarella, tomate y jamon")
    else:
        print(f"Pizza No vegetariana con mozzarella, tomate y salmon")