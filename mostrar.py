def mostrar_producto(inventario):
    """Muestra todos los productos"""

    if not inventario:
        print("Inventario vacío")
        return

    for i in inventario:
        print(f"{i['nombre']} | Precio: {i['precio']} | Cantidad: {i['cantidad']}")


def buscar_elemento(inventario, nombre):
    """Busca un producto por nombre"""

    encontrado = False

    for i in inventario:
        if i["nombre"] == nombre:
            print(f"Encontrado: {i}")
            encontrado = True
            break

    if not encontrado:
        print("Producto no encontrado")


def producto_mayor_stock(inventario):
    """Muestra el producto con mayor cantidad"""

    if not inventario:
        return

    mayor = inventario[0]

    for i in inventario:
        if i["cantidad"] > mayor["cantidad"]:
            mayor = i

    print(f"Mayor stock: {mayor['nombre']} ({mayor['cantidad']})")