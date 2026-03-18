def agregar_producto():
    # Solicitar datos al usuario.
    while True: # Condicional que se repite hasta que las condiciones sean correctas
        # Capturador de errores
        try:
            # Solicita el nombre del producto a ingresar.
            nombre = input("Ingrese el nombre del producto: ")
            if not nombre.isalpha():
                print("No se permiten números ni caracteres especiales. \n")
                continue
        except ValueError as e:
            print(f"Error: {e}Inténtelo de nuevo.")
        
        
        while True: # Condicional que se repite hasta que las condiciones sean correctas
            # Capturador de errores
            try:
                # Solicita el precio del producto a ingresar.
                precio = float(input("Ingrese el precio del producto: "))
                if precio < 0:
                    print("No se permiten números negativos. Intentelo de nuevo")
                break
            except ValueError:
                print("Error: Solo se permiten números. Intentelo nuevamente")


        while True: # Condicional que se repite hasta que las condiciones sean correctas
            # Capturador de errores
            try:
                # Solicita la cantidad del producto a ingresar
                cantidad = int(input("Ingrese la cantidad del producto: "))
                if precio < 0:
                    print("No se permiten números negativos. Intentelo de nuevo")
                break
            except ValueError:
                print("Error: Solo se permiten números enteros. Intentelo nuevamente")
        break
    
    producto = {}

    producto[nombre] = {
        "precio": precio,
        "cantidad": cantidad
        }
    return producto


"""print(f
Producto: {nombre}
Precio: {precio}
Cantidad: {cantidad})
Total: {cantidad_total}




Este programa"""