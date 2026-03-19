# Importaciones
import agregar
import mostrar
import calculo_estadisticas


# Menu que se muestra al iniciar el programa.
MENU = """
¿Qué desea hacer?

1. --> Agregar Productos.
2. --> Mostrar Inventario.
3. --> Calcular Estadísticas.
4. --> Salir."""


# Lista en donde se almacena el inventario.
inventario = []


def menu_estadistica():
    MENU_ESTADISTICAS = """
    ¿Qué desea hacer?

    1. --> Precio De Todos Los Productos.
    2. --> Cantidad de items.
    3. --> Salir."""
    

    while True:
        print(MENU_ESTADISTICAS)
        

        try:
            opcion_estadisticas = int(input("Digite una opción. "))
        except ValueError:
            print("Valor invalido. Intentelo de nuevo.")


        if opcion_estadisticas == 1:
            calculo_total = calculo_estadisticas.calcular_total(inventario)
            print(f"El precio total de su inventario es de: {calculo_total}")

        elif opcion_estadisticas == 2:
            calculo_cantidad = calculo_estadisticas.calcular_cantidad(inventario)
            print(f"La cantidad de productos en su inventario es de: {calculo_cantidad}")

        elif opcion_estadisticas == 3:
            break

        else:
            print("Opción invalida. Intentelo de nuevo.")


while True:
    print(MENU)

    try:
        opcion = int(input("Digite una opción. "))
    except ValueError:
        print("Valor invalido. Intentelo de nuevo")
        continue

    if opcion == 1: # Agregar Productos.
        resultado = agregar.agregar_producto()
        inventario.append(resultado)



    elif opcion == 2: # Mostrar Inventario.
        mostrar.mostrar_producto(inventario)


    elif opcion == 3: # Calcular Estadisticas.
        menu_estadistica()

        
    elif opcion == 4: # Salir
        break

    
    else: # En caso de error.
        print("Opción invalida. Intentelo de nuevo.")




# Mensaje de despedida.
print("Gracias por usar este software.")

