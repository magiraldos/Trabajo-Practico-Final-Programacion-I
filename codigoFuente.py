
# Carga de la Matriz con Datos
def agregar_productos(matriz_productos, id_actual):
    # Generamos ID del producto
    nuevo_id = id_actual + 1
    # Pedimos datos al usuario
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_producto = float(input("Ingrese precio del producto: "))
    stock_producto = int(input("Ingrese stock del producto: "))
    categoria = input("Ingrese la categoria del producto: ")
    proveedor = input("Ingrese el proveedor del producto: ")
    fila_producto = [nuevo_id, nombre_producto, precio_producto, stock_producto, categoria, proveedor]
    matriz_productos.append(fila_producto)
    return matriz_productos, nuevo_id

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
    
# Creación de la Matriz y ID
inventario = []
id_contador = 0
encabezado_inventario = ["ID", "Nombre", "Precio", "Stock", "Categoria", "Proveedores"]

# Imprimir la Matriz
for i in range(0,3):
    agregar_productos(inventario,id_contador)
    imprimir_inventario(inventario, encabezado_inventario)

