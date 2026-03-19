# Importaciones
import agregar
import mostrar


MENU = """
¿Qué desea hacer?

1. --> Agregar Productos.
2. --> Mostrar Inventario.
3. --> Calcula Estadísticas.
4. --> Salir."""

# Lista de inventario
inventario = []

while True:
    print(MENU)

    try:
        opcion = int(input("Digite una opción. "))
    except ValueError:
        print("Valor invalido. Intentelo de nuevo")
        continue

    if opcion == 1:
        resultado = agregar.agregar_producto()
        inventario.append(resultado)
        print("Ha escogido la opción 1")
    elif opcion == 2:
        mostrar.mostrar_producto(inventario)
        print("Ha escogido la opción 2")
    elif opcion == 3:
        print("Ha escogido la opción 3")
    elif opcion == 4:
        break
    else:
        print("Opción invalida. Intentelo de nuevo.")

print("Gracias por usar este software.")





"""coders = []

while True:

    print(MENU)
    opcion = input("Escoja una opción: ")

    match opcion:

        case "1":

            coder = codersriwi.coder_riwi()
            coders.append(coder)"""
