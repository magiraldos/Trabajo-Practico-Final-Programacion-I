def main():
    """
    Esta funcion va a cumplir el rol del menu del sistema de control de inventario, cómo será la interfaz para interactuar con las funciones del programa
    """
    print("="*80)
    print(f"{"Menu del Sistema":^80}")
    print("="*80)
    print("1. Cargar nuevo producto en el inventario") # HECHO
    print("2. Buscar producto, proveedor o categoria") # ENCUESTA / ENCARGADO
    print("3. Modificar producto, proveedor o categoria") # PENDIENTE
    print("4. Eliminar producto, proveedor o categoria") # PENDIENTE
    print("5. Realizar venta de producto") # PENDIENTE (IDEA: GENERAR FACTURA)
    print("6. Estadisticas") # PENDIENTE
    
def carga_producto(productos, id_producto, categorias, id_categoria, proveedores, id_proveedor ):
    """
    Funcion que permite el ingreso de nuevos productos, registro de proveedores y categorías relacionadas al producto. 3 partes (validando que no existe):
    - Ingreso de los datos del producto (1)
    - Ingreso de los datos de la categoria (2)
    - Ingreso de los datos del proveedor (3)
    """
    # PARTE 1
    # Generamos ID del producto
    id_producto += 1
    # Pedimos datos del producto al usuario
    print("Ingreso de datos del producto")
    nombre_producto = (input("Ingrese el nombre del producto: ")).upper()
    precio_producto = float(input("Ingrese precio del producto: "))
    while precio_producto <= 0:
        print("Error, el precio debe ser mayor a 0")
        precio_producto = float(input("Ingrese precio del producto: "))
    stock_producto = int(input("Ingrese stock del producto: "))
    while stock_producto < 0:
        print("Error, el stock del producto debe ser un numero mayor o igual a 0")
        precio_producto = float(input("Ingrese stock del producto: "))
    # PARTE 2
    print("CATEGORIA")
    nombre_categoria = (input("Ingrese la categoria del producto: ")).upper()
    id_categoria += 1
    
    # PARTE 3
    print("PROVEEDOR")
    nombre_proveedor = (input("Ingrese el proveedor del producto:")).upper()
    telefono_proveedor = input("Ingrese telefono del proveedor (11 digitos): ")
    while len(telefono_proveedor) != 11:
        print("Error, tamaño invalido")
        telefono_proveedor = input("Ingrese telefono del proveedor (11 digitos): ")
    id_categoria += 1

    fila_productos = [id_producto, nombre_producto, precio_producto, stock_producto, nombre_categoria, nombre_proveedor]
    if fila_productos not in productos:
        productos.append(fila_productos)
        fila_categorias = [id_categoria, nombre_categoria, id_producto, nombre_producto]
        categorias.append(fila_categorias)
        fila_proveedores = [id_proveedor, nombre_proveedor, telefono_proveedor, id_producto, nombre_producto]
        proveedores.append(fila_proveedores)
    else:
        print("Ya existe este producto en el inventario")
    return productos, id_producto, id_categoria, id_proveedor

def imprimir_inventario(identidad, encabezado_identidad):
    filas = len(identidad)
    columnas = len(identidad[0])
    ancho = 15
    for titulo in encabezado_identidad:
        print(f"{titulo:<{ancho}}", end="")
    print()
    for fila in identidad:
        for dato in fila:
            print(f"{str(dato):<{ancho}}", end="")
        print()
    
# Definimos las estructuras de datos: Matrices y sus respectivos encabezados y ids
# Cuando se va a cargar, se deben llenar todas las matrices (a excepción de ventas que es para el egreso)
productos = []
id_producto = 0
encabezado_producto = ["ID", "Producto", "Precio", "Stock", "Categoria", "Proveedores"]


categorias = []
id_categoria = 0
encabezado_categoria = ["ID", "Categoria", "ID Producto", "Nombre Producto"]


proveedores = []
id_proveedor = 0
encabezado_proveedor = ["ID", "Proveedor", "Telefono", "ID Producto", "Producto"]


ventas = []
id_ventas = 0
encabezado_ventas = ["ID Venta", "ID Producto", "Cantidad Vendida", "Precio Total"]


# Imprimir la Matriz
carga_producto(productos,id_producto, categorias, id_proveedor, proveedores, id_proveedor)

imprimir_inventario(productos, encabezado_producto)