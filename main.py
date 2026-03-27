# Importaciones
import agregar # Importo el archivo "agregar.py" a "main.py" 
import mostrar # Importo el archivo "mostrar.py" a "main.py" 
import calculo_estadisticas # Importo el archivo "calculo_estadisticas.py" a "main.py" 


# Menu que se muestra al iniciar el programa.
MENU = """
¿Qué desea hacer?

1. --> Agregar Productos.
2. --> Mostrar Inventario.
3. --> Calcular Estadísticas.
4. --> Ver Mayor Stock.
5. --> Salir."""

    
# Lista en donde se almacena el inventario.
inventario = []


def menu_estadistica():
    # Menú que se muestra al escoger la tercera opción en el primer menu
    MENU_ESTADISTICAS = """
    ¿Qué desea hacer?

    1. --> Ver Costo De Inventario.
    2. --> Ver Cantidad Total de Items.
    3. --> Salir."""
    
    
    while True: # Ciclo que se repite infinitamente.
        # Muestra el segundo menu.
        print(MENU_ESTADISTICAS)
        

        # Capturador de errores.
        try:
            # Captura la elección del usuario para el menú de estadísticas.
            opcion_estadisticas = int(input("Digite una opción. "))
        except ValueError:
            print("Valor invalido. Intentelo de nuevo.")
            continue


        if opcion_estadisticas == 1: # Precio Total de Inventario.
            # Guarda el return de la función que contiene el calculo de valor total del inventario y al mismo tiempo la llama.
            calculo_total = calculo_estadisticas.calcular_total(inventario)
            # Muestra en la terminal el mensaje que yo le puse y la variable que guarda el return de la función.
            print(f"El precio total de su inventario es de: {calculo_total}")


        elif opcion_estadisticas == 2: # Cantidad Total de Items.
            # Guarda el return de la función que contiene el calculo de la cantidad total de items y al mismo tiempo la llama.
            calculo_cantidad = calculo_estadisticas.calcular_cantidad(inventario)
            # Muestra en la terminal el mensaje que yo le puse y la variable que guarda el return de la función.
            print(f"La cantidad de productos en su inventario es de: {calculo_cantidad}")
            

        elif opcion_estadisticas == 3: # Salir.
            # Rompe el ciclo del while True y sale del menú.
            break



        else: # En caso de error.
            print("Opción invalida. Intentelo de nuevo.")



while True: # Ciclo que se repite infinitamente.
    # Muestra el primer menú.
    print(MENU)

    # Capturador de errores.
    try:
        # Captura la elección del usuario para el menú principal
        opcion = int(input("Digite una opción. "))
    except ValueError:
        print("Valor invalido. Intentelo de nuevo")
        continue

    if opcion == 1: # Agregar Productos.
        # Guarda el return de la función que contiene el diccionario y al mismo tiempo la llama.
        resultado = agregar.agregar_producto()
        # Guarda la variable que contiene el diccionario dentro de la lista llamada "inventario".
        inventario.append(resultado)



    elif opcion == 2: # Mostrar Inventario.
        # Llama a la función que contiene el algoritmo que muestra el inventario.
        mostrar.mostrar_producto(inventario)


    elif opcion == 3: # Calcular Estadisticas.
        # Llama a la función que contiene el segundo menu.
        menu_estadistica()


    elif opcion == 4:
        mostrar.maxstock(inventario)

        
    elif opcion == 5: # Salir
        # Rompe el ciclo del while True y sale del menú.
        break

    
    else: # En caso de error.
        # Muestra el mensaje de error en la consola.
        print("Opción invalida. Intentelo de nuevo.")




# Mensaje de despedida.
print("Gracias por usar este software.")

