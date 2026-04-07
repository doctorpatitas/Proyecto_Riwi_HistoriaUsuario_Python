import csv

def guardar_csv(inventario, ruta):
    """Guarda el inventario en CSV"""

    if not inventario:
        print("Inventario vacío")
        return

    try:
        with open(ruta, "w", newline="") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["nombre", "precio", "cantidad"])

            for i in inventario:
                writer.writerow([i["nombre"], i["precio"], i["cantidad"]])

        print("Guardado correctamente")

    except Exception as e:
        print(f"Error: {e}")


def cargar_csv(ruta):
    """Carga inventario desde CSV"""

    inventario = []

    try:
        with open(ruta, "r") as archivo:
            reader = csv.DictReader(archivo)

            for fila in reader:
                try:
                    inventario.append({
                        "nombre": fila["nombre"],
                        "precio": float(fila["precio"]),
                        "cantidad": int(fila["cantidad"])
                    })
                except:
                    continue

        print("Cargado correctamente")
        return inventario

    except FileNotFoundError:
        print("Archivo no encontrado")
        return []