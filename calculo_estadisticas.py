def calcular_estadisticas(datos):
    resultado = datos["precio"] * datos ["cantidad"]
    return resultado

def calcular_total(inventario):
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


