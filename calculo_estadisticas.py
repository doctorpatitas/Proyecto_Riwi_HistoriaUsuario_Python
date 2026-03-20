# Función que calcula el total de un producto (precio * cantidad).
def calcular_estadisticas(datos):
    # Busca en el diccionario las claves de "precio" y "cantidad", luego multiplica su valor y lo guarda en la variable de resultado.
    resultado = datos["precio"] * datos ["cantidad"]
    return resultado


# Función que suma el total de cada producto al acumulador.
def calcular_total(inventario):
    # Variable contadora que almacena el precio total del inventario.
    total = 0
    # Recorre cada producto de la lista.
    for i in inventario:
        # Accede al nombre y datos del producto.
        for nombre, datos in i.items():
            # Ingresa el calculo de la función "calcular_estadisticas" dentro de la variable total y incrementa para contar el valor total del inventario.
            total += calcular_estadisticas(datos)
    return total


# Función que suma la cantidad total de productos en el inventario.
def calcular_cantidad(inventario):
    # Variable contadora que almacena la cantidad total de productos.
    conteo = 0
    # Recorre cada producto de la lista.
    for i in inventario:
        # Accede al nombre y datos del producto.
        for nombre, datos in i.items():
            # Se incrementa para contar la cantidad total de productos.
            conteo += datos ["cantidad"]
    return conteo

