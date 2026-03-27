# Función que solicita los datos al usuario para ingresar sus productos al programa.
def agregar_producto():
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
            # Muestra el mensaje de error en la terminal.
            print(f"Error: {e}Inténtelo de nuevo.")
        
        
        while True: # Ciclo que se repite infinitamente.
            # Capturador de errores
            try:
                # Solicita el precio del producto a ingresar.
                precio = float(input("Ingrese el precio del producto: "))
                # En caso de que sea un número negativo.
                if precio < 0:
                    print("No se permiten números negativos. Intentelo de nuevo")
                else:
                    # Rompe el ciclo del while True y sale de la petición.
                    break
            except ValueError:
                # Muestra el mensaje de error en la terminal.
                print("Error: Solo se permiten números. Intentelo nuevamente")


        while True: # Ciclo que se repite infinitamente.
            # Capturador de errores
            try:
                # Solicita la cantidad del producto a ingresar
                cantidad = int(input("Ingrese la cantidad del producto: "))
                # En caso de que sea un número negativo.
                if cantidad < 0:
                    print("No se permiten números negativos. Intentelo de nuevo")
                else:
                    # Rompe el ciclo del while True y sale de la petición.
                    break
            except ValueError:
                # Muestra el mensaje de error en la terminal.
                print("Error: Solo se permiten números enteros. Intentelo nuevamente")
        break
    

    # Diccionario que almacena los datos ingresados por el usuario.
    producto = {
        "papa": {
            "precio": 21,
            "cantidad": 3452
        },
        "libra de arroz": {
            "precio": 13452,
            "cantidad": 1234345
        }
    }


    # Se guarda el producto en formato de diccionario. 
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
        }

    # Retorna el diccionario llamado "producto".
    return producto

