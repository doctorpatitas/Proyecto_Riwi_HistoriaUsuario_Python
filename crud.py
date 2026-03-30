def actualizar_producto(inventario, nombre):
    """Actualiza precio o cantidad"""

    for i in inventario:
        if i["nombre"] == nombre:
            try:
                nuevo_precio = float(input("Nuevo precio: "))
                nueva_cantidad = int(input("Nueva cantidad: "))
                i["precio"] = nuevo_precio
                i["cantidad"] = nueva_cantidad
                print("Actualizado")
                return
            except:
                print("Error en datos")
                return

    print("No encontrado")


def eliminar_producto(inventario, nombre):
    """Elimina producto"""

    for i in inventario:
        if i["nombre"] == nombre:
            inventario.remove(i)
            print("Eliminado")
            return

    print("No encontrado")