
import random

def generar_id(inventario):
    """
    Genera un ID aleatorio de 4 dígitos (0000–9999)
    y verifica que no exista en el inventario.
    """

    while True:
        # Genera número entre 0 y 9999
        numero = random.randint(0, 9999)

        # Formatea a 4 dígitos (ej: 5 → 0005)
        id_generado = str(numero).zfill(4)

        # Verifica si ya existe
        existe = False
        for producto in inventario:
            if producto["id"] == id_generado:
                existe = True
                break

        # Si no existe, lo usamos
        if not existe:
            return id_generado


def agregar_producto(inventario):
    """
    Solicita datos al usuario y crea un producto con ID único.
    """

    while True:
        nombre = input("Nombre: ").strip()
        if nombre == "":
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

    # 🔥 Generar ID único
    id_producto = generar_id(inventario)

    return {
        "id": id_producto,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }