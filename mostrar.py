# Muestra todos los productos almacenados en el inventario.
def mostrar_producto(inventario):
    # Recorre cada producto de la lista.
    for i in inventario:
        # Accede al nombre y datos del producto.
        for nombre, datos in i.items():
            # Muestra el inventario en la terminal.
            print(f"{nombre} |Precio: {datos['precio']} |Cantidad: {datos['cantidad']}")
