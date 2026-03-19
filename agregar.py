def agregar_producto():
    # Solicitar datos al usuario.
    while True: # Ciclo que se repite infinitamente.
        # Capturador de errores
        try:
            # Solicita el nombre del producto a ingresar.
            nombre = input("Ingrese el nombre del producto: ")
            # Condicional que  esta en caso de que el valor entregado por input no sea una cadena de texto
            if not nombre.isalpha():
                # Muestro el mensaje en la terminal
                print("No se permiten números ni caracteres especiales. \n")
                continue
        except ValueError as e:
            print(f"Error: {e}Inténtelo de nuevo.")
        
        
        while True: # Ciclo que se repite infinitamente.
            # Capturador de errores
            try:
                # Solicita el precio del producto a ingresar.
                precio = float(input("Ingrese el precio del producto: "))
                if precio < 0:
                    print("No se permiten números negativos. Intentelo de nuevo")
                else:
                    # Rompe el ciclo del while True y sale de la petición.
                    break
            except ValueError:
                print("Error: Solo se permiten números. Intentelo nuevamente")


        while True: # Ciclo que se repite infinitamente.
            # Capturador de errores
            try:
                # Solicita la cantidad del producto a ingresar
                cantidad = int(input("Ingrese la cantidad del producto: "))
                if cantidad < 0:
                    print("No se permiten números negativos. Intentelo de nuevo")
                else:
                    # Rompe el ciclo del while True y sale de la petición.
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

