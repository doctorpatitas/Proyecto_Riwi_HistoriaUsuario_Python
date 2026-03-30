# Archivo principal que ejecuta todo el programa

import agregar
import mostrar
import calculo_estadisticas
import crud
import archivos

# Lista principal del inventario
inventario = []

MENU = """
¿Qué desea hacer?

1. Agregar producto
2. Mostrar inventario
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Estadísticas
7. Guardar CSV
8. Cargar CSV
9. Salir
"""

while True:
    print(MENU)

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Entrada inválida.")
        continue

    if opcion == 1:
        producto = agregar.agregar_producto()
        inventario.append(producto)

    elif opcion == 2:
        mostrar.mostrar_producto(inventario)

    elif opcion == 3:
        nombre = input("Nombre a buscar: ")
        mostrar.buscar_elemento(inventario, nombre)

    elif opcion == 4:
        nombre = input("Nombre a actualizar: ")
        crud.actualizar_producto(inventario, nombre)

    elif opcion == 5:
        nombre = input("Nombre a eliminar: ")
        crud.eliminar_producto(inventario, nombre)

    elif opcion == 6:
        stats = calculo_estadisticas.calcular_estadisticas(inventario)
        print(stats)

    elif opcion == 7:
        ruta = "inventario.csv"
        archivos.guardar_csv(inventario, ruta)

    elif opcion == 8:
        ruta = "inventario.csv"
        inventario = archivos.cargar_csv(ruta)

    elif opcion == 9:
        print("Adiós 👋")
        break

    else:
        print("Opción inválida")