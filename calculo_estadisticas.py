def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario.
    """

    if not inventario:
        return "Inventario vacío"

    unidades = 0
    valor_total = 0

    mas_caro = inventario[0]
    mayor_stock = inventario[0]

    for i in inventario:
        unidades += i["cantidad"]
        valor_total += i["precio"] * i["cantidad"]

        if i["precio"] > mas_caro["precio"]:
            mas_caro = i

        if i["cantidad"] > mayor_stock["cantidad"]:
            mayor_stock = i

    return {
        "unidades_totales": unidades,
        "valor_total": valor_total,
        "producto_mas_caro": mas_caro["nombre"],
        "producto_mayor_stock": mayor_stock["nombre"]
    }
