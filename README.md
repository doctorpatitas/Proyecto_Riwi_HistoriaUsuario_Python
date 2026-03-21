# 🧾 Sistema de Inventario en Python
## Historia de usuario Mes 1

## 📋 Diagrama de flujo.

![alt text](image.png)

## 📌 Descripción

Este es un programa de **Inventario** sencillo de python **Python** que permite al usuario ingresar productos, ver el inventario o calcular el costo total de su inventario.

## ⚙️ ¿Cómo funciona el programa?

El programa muestra un menú inicial y le pregunta al usuario si desea:
- Agregar Producto.
- Mostrar Inventario.
- Calcular Estadísticas.
- Salir.

Dependiendo de la opción el programa muestra:

### **1. Agregar producto** 

Pregunta al usuario por:

- El nombre del producto.
- El precio del producto.
- La cantidad del producto.

Y finalmente guarda la información dentro de un diccionario.

### **2. Mostrar producto.**

Muestra la información que de el producto que el usuario guardo con anterioridad.

### **3. Calcular Estadísticas.**

Al entrar en esta opción le muestra un submenú al usuario y le pregunta si desea: 

- Ver Costo De Inventario.
- Ver Cantidad Total de Items.
- Salir.

Si el usuario escoge **"Ver Costo De Inventario."** le muestra el valor total de su inventario. 

Si el usuario escoge **"Ver Cantidad Total de Items."** le muestra la cantidad de items en su inventario.

Si el usuario escoge **"Salir."** sale del submenú y regresa al menú inicial.

### **4. Salir.**

Sale del menú y cierra el programa por completo.

---


Además, el programa incluye **validaciones para evitar errores**, como:
 
- No se permiten números negativos ni cadenas de texto para ambos menú del programa.
- Solo acepta números del 1 al 4 y del 1 al 3 dependiendo de cada menú.
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
- Calcular las estadísticas y mostrarlas al usuario.
- Salir del menú y cerrar el programa.

---


## 🚀 Como usar el proyecto.

### 1️⃣ Descargar e Instalar Python 3.14.3.
En la siguiente opción se cuentra la url de descarga de Python 👉
[Python Link de Descarga](https://www.python.org/downloads/release/python-3143/)

### 2️⃣ Descargar e Instalar Visual Studio Code.
En la siguiente opción se cuentra la url de descarga de Visual Studio Code 👉 [Visual Studio Code Link de Descarga](https://code.visualstudio.com/download)

### 3️⃣ Descargar e Instalar Git.
En la siguiente opción se cuentra la url de descarga de Python 👉
[Git Link de Descarga](https://git-scm.com/install/)

### 4️⃣ Clonar el repositorio
En su **Escritorio** presione **Click Derecho** y presione donde diga **"Nueva Carpeta"** o parecidos.

Dentro de su carpeta presione **Click Derecho** y presiona la opción que diga **Abrir en una terminal**.

Dentro de la terminar copie y pegue el siguiente comando: **git clone https://github.com/doctorpatitas/Proyecto_Riwi_HistoriaUsuario_Python.git**

Finalmente introduzca el comando **code .** para que le habra **Visual Studio Code** dentro de la carpeta en donde se encuentra ubicado.

### 5️⃣ Ejecutar el programa.
Dentro de **Visual Studio Code** dirigase arriba a la izquierda y presione la opción que diga **Terminal** y luego **New Terminal**

Dentro de la terminal escriba el siguiente comando: **python3 main.py**

Y su programa estara ejecutandose exitosamente. 

### Gracias por leer.