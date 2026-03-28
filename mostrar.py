# Muestra todos los productos almacenados en el inventario.
def mostrar_producto(inventario):
    # Recorre cada producto de la lista.
    for i in inventario:
        # Accede al nombre y datos del producto.
        for nombre, datos in i.items():
            # Muestra el inventario en la terminal.
            print(f"{nombre} |Precio: {datos['precio']} |Cantidad: {datos['cantidad']}")


def producto_mayor_stock(inventario):
    lista_mas_stock = []
    for i in inventario:
        for nombre, datos in i.items():
            contenedor_cantidad = datos.get("cantidad")
            lista_mas_stock.append(contenedor_cantidad)
            mayor_stock = max(lista_mas_stock)
            
    print(f"{nombre}: {mayor_stock}")


def producto_mas_caro(inventario):
    lista_mas_caro = []
    for i in inventario:
        for nombre, datos in i.items():
            contenedor_precio = datos.get("precio")
            lista_mas_caro.append(contenedor_precio)
            mayor_precio = max(lista_mas_caro)

    print(f"{nombre}: {mayor_precio}")


def buscar_elemento(inventario, nombre):
    elemento = input("Introduzca el nombre del elemento que desea buscar: ")
    for i in inventario:
        for nombre, datos in i:      
            if i[elemento]["cantidad"] == elemento:
                elemento = i[nombre], datos["cantidad"]
        
    print(elemento)
