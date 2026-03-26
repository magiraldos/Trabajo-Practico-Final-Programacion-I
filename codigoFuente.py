# Carga de la Matriz con Datos
def carga_producto(productos, id_producto):
    """
    Funcion que permite el ingreso de productos, registro de proveedores y categorías relacionadas al producto. 3 partes:
    - Ingreso de los datos del producto (1)
    - Ingreso de los datos de la categoria (2)
    - Ingrso de los datos del proveedor (3)
    """
    # PARTE 1
    # Generamos ID del producto
    nuevo_id = id_producto + 1
    # Pedimos datos del producto al usuario
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_producto = float(input("Ingrese precio del producto: "))
    stock_producto = int(input("Ingrese stock del producto: "))
    categoria = input("Ingrese la categoria del producto: ")
    proveedor = input("Ingrese el proveedor del producto: ")
    # Los insertamos en la matriz de producto
    fila_productos = [nuevo_id, nombre_producto, precio_producto, stock_producto, categoria, proveedor]
    productos.append(fila_productos)
    
    # PARTE 2
    
    # PARTE 3
    
    return productos, nuevo_id

def imprimir_inventario(inventario, encabezado_inventario):
    filas = len(inventario)
    columnas = len(inventario[0])
    for titulo in encabezado_inventario: # Imprimimos los títulos
        print(titulo, end="\t")
    print()
    for fila in range(filas): # Imprimimos la matriz
        for columna in range(columnas):
            print(inventario[fila][columna], end="\t")
        print()
    
# Agregar los 5 casos de ejemplos del Google Sheets ////
# Definimos las estructuras de datos: Matrices y sus respectivos encabezados y ids
# Cuando se va a cargar, se deben llenar todas las matrices (a excepción de ventas que es para el egreso)
productos = []
id_producto = 0
encabezado_producto = ["ID Producto", "Producto", "Precio", "Stock", "Categoria", "Proveedores"]


categorias = []
id_categoria = 0
encabezado_categoria = ["ID Categoría", "Categoria", "ID Producto", "Nombre Producto"]


proveedores = []
id_proveedor = 0
encabezado_proveedor = ["ID Proveedor", "Proveedor", "Telefono", "ID Producto", "Producto"]


ventas = []
id_ventas = 0
encabezado_ventas = ["ID Venta", "ID Producto", "Cantidad Vendida", "Precio Total"]


# Imprimir la Matriz
for i in range(0,3):
    carga_producto(productos,id_producto)
    imprimir_inventario(productos, encabezado_producto)

