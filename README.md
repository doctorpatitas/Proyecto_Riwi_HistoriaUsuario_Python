# 🧾 Sistema de Inventario en Python
## Historia de usuario Mes 1

## 📋 Diagrama de flujo.

![alt text](image.png)

## 📌 Descripción

Este es un programa de **Inventario** sencillo de **Python** que permite al usuario ingresar productos, ver el inventario, calcular el costo total de su inventario y guardar o cargar los datos mediante archivos CSV.

## ⚙️ ¿Cómo funciona el programa?

El programa muestra un menú inicial y le pregunta al usuario si desea:
- Agregar Producto.
- Mostrar Inventario.
- Buscar Producto.
- Actualizar Producto.
- Eliminar Producto.
- Calcular Estadísticas.
- Guardar en CSV.
- Cargar desde CSV.
- Salir.

Dependiendo de la opción el programa muestra:

### **1. Agregar producto** 

Pregunta al usuario por:

- El nombre del producto.
- El precio del producto.
- La cantidad del producto.

Y finalmente guarda la información dentro de un diccionario.

---

### **2. Mostrar producto.**

Muestra la información de los productos que el usuario ha guardado con anterioridad.

---

### **3. Buscar producto.**

Permite al usuario buscar un producto por su nombre.

Si el producto existe, muestra su información.  
Si no existe, muestra un mensaje indicando que no fue encontrado.

---

### **4. Actualizar producto.**

Permite modificar el precio y la cantidad de un producto existente.

Si el producto no existe, muestra un mensaje de error.

---

### **5. Eliminar producto.**

Permite eliminar un producto del inventario.

Si el producto no existe, muestra un mensaje de error.

---

### **6. Calcular Estadísticas.**

Al entrar en esta opción le muestra un submenú al usuario y le pregunta si desea: 

- Ver Costo De Inventario.
- Ver Cantidad Total de Items.
- Ver Producto Más Caro.
- Ver Producto con Mayor Stock.
- Salir.

Si el usuario escoge **"Ver Costo De Inventario."** le muestra el valor total de su inventario. 

Si el usuario escoge **"Ver Cantidad Total de Items."** le muestra la cantidad de items en su inventario.

Si el usuario escoge **"Ver Producto Más Caro."** le muestra el producto con mayor precio.

Si el usuario escoge **"Ver Producto con Mayor Stock."** le muestra el producto con mayor cantidad disponible.

Si el usuario escoge **"Salir."** sale del submenú y regresa al menú inicial.

---

### **7. Guardar en CSV.**

Permite guardar todos los productos del inventario en un archivo `.csv`.

Si el inventario está vacío, muestra un mensaje indicando que no hay datos para guardar.

---

### **8. Cargar desde CSV.**

Permite cargar productos desde un archivo `.csv` previamente guardado.

Si el archivo no existe, muestra un mensaje de error.

---

### **9. Salir.**

Sale del menú y cierra el programa por completo.

---

Además, el programa incluye **validaciones para evitar errores**, como:
 
- No se permiten números negativos ni cadenas de texto para ambos menú del programa.
- Solo acepta números del 1 al 9 dependiendo del menú.
- No permite números ni caracteres especiales en el nombre del producto.
- No permite números negativos en el precio y la cantidad.
- Solo se permiten números en el precio.
- Solo se permiten números enteros en la cantidad.

## ¿Cómo es el flujo del programa?

El programa utiliza **bucles (`while`) y manejo de errores (`try / except` )** para validar los datos que ingrese el usuario y evitar errores durante la ejecución.

### El flujo del programa es el siguiente: 

1. Se muestra el **Menú inicial**.

2. Se valida la **elección** del usuario.

3. Dependiendo de la **elección** del usuario el programa puede:
- Preguntar por un **nombre**, **precio** y **cantidad** para agregar un producto.
- Mostrar el **inventario** del usuario.
- Buscar, actualizar o eliminar productos.
- Calcular las estadísticas y mostrarlas al usuario.
- Guardar o cargar datos mediante archivos CSV.
- Salir del menú y cerrar el programa.

---

## 🚀 Como usar el proyecto.

### 1️⃣ Descargar e Instalar Python 3.14.3.
En la siguiente opción se encuentra la url de descarga de Python 👉
[Python Link de Descarga](https://www.python.org/downloads/release/python-3143/)

### 2️⃣ Descargar e Instalar Visual Studio Code.
En la siguiente opción se encuentra la url de descarga de Visual Studio Code 👉 [Visual Studio Code Link de Descarga](https://code.visualstudio.com/download)

### 3️⃣ Descargar e Instalar Git.
En la siguiente opción se encuentra la url de descarga de Git 👉
[Git Link de Descarga](https://git-scm.com/install/)

### 4️⃣ Clonar el repositorio
En su **Escritorio** presione **Click Derecho** y presione donde diga **"Nueva Carpeta"** o parecidos.

Dentro de su carpeta presione **Click Derecho** y presione la opción que diga **Abrir en una terminal**.

Dentro de la terminal copie y pegue el siguiente comando:  
**git clone https://github.com/doctorpatitas/Proyecto_Riwi_HistoriaUsuario_Python.git**

Finalmente introduzca el comando **code .** para que le abra **Visual Studio Code** dentro de la carpeta en donde se encuentra ubicado.

### 5️⃣ Ejecutar el programa.
Dentro de **Visual Studio Code** diríjase arriba a la izquierda y presione la opción que diga **Terminal** y luego **New Terminal**

Dentro de la terminal escriba el siguiente comando:  
**python3 main.py**

Y su programa estará ejecutándose exitosamente. 

### Gracias por leer.
