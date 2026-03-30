def agregar_producto():
    """
    Solicita datos al usuario y retorna un producto en forma de diccionario.
    """

    while True:
        nombre = input("Nombre: ")
        if nombre.strip() == "":
            print("Nombre inválido")
            continue
        break

    while True:
        try:
            precio = float(input("Precio: "))
            if precio < 0:
                print("No negativo")
                continue
            break
        except:
            print("Solo números")

    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad < 0:
                print("No negativo")
                continue
            break
        except:
            print("Solo enteros")

    return {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }