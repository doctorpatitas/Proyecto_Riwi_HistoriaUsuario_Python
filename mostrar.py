def mostrar_producto(inventario):
    for i in inventario:
        for nombre, datos in i.items():
            print(f"{nombre} |Precio: {datos['precio']} | Cantidad: {datos['cantidad']}")


