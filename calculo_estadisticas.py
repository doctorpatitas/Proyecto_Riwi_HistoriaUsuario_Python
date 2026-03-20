# Función que el total de cada producto.
def calcular_estadisticas(datos):
    # Busca en el diccionario las claves de "precio" y "cantidad", luego multiplica su valor y lo guarda en la variable de resultado.
    resultado = datos["precio"] * datos ["cantidad"]
    # Retorna la variable llamada "resultado".
    return resultado


# Función que almacena el total calculado en la función llamada "calcular_estadisticas".
def calcular_total(inventario):
    # Variable contadora que almacena el precio total del inventario
    total = 0

    for i in inventario:

        for nombre, datos in i.items():

            total += calcular_estadisticas(datos)

    return total

def calcular_cantidad(inventario):
    conteo = 0
    for i in inventario:
        for nombre, datos in i.items():
            conteo += datos ["cantidad"]

    return conteo


