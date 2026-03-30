def main():
    """
    Esta funcion va a cumplir el rol del menu del sistema de control de inventario.
    """ 
    print("="*80)
    print(f"{'Menu del Sistema':^80}")
    print("="*80)
    print("1. Cargar nuevo producto en el inventario") # HECHO
    print("2. Buscar producto, proveedor o categoria") # ENCUESTA / ENCARGADO
    print("3. Modificar producto, proveedor o categoria") # PENDIENTE
    print("4. Eliminar producto, proveedor o categoria") # PENDIENTE
    print("5. Realizar venta de producto") # PENDIENTE (IDEA: GENERAR FACTURA)   
    print("6. Estadisticas") # PENDIENTE
    print("0. Salir")

def carga_producto(productos, id_producto, categorias, id_categoria, proveedores, id_proveedor):
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
    print("\n--- Ingreso de datos del producto ---")
    nombre_producto = (input("Ingrese el nombre del producto: ")).upper()    
    
    precio_producto = float(input("Ingrese precio del producto: "))
    while precio_producto <= 0:
        print("Error, el precio debe ser mayor a 0")
        precio_producto = float(input("Ingrese precio del producto: "))        
        
    stock_producto = int(input("Ingrese stock del producto: "))
    while stock_producto < 0:
        print("Error, el stock del producto debe ser un numero mayor o igual a 0")
        stock_producto = int(input("Ingrese stock del producto: ")) 
        
    # PARTE 2
    print("\n--- CATEGORIA ---")
    nombre_categoria = (input("Ingrese la categoria del producto: ")).upper()
    id_categoria += 1
    
    # PARTE 3
    print("\n--- PROVEEDOR ---")
    nombre_proveedor = (input("Ingrese el proveedor del producto:")).upper()
    telefono_proveedor = input("Ingrese telefono del proveedor (11 digitos): ")
    while len(telefono_proveedor) != 11:
        print(f"Error, tamaño invalido (ingresaste {len(telefono_proveedor)} dígitos)")
        telefono_proveedor = input("Ingrese telefono del proveedor (11 digitos): ")
    
    id_proveedor += 1 

    fila_productos = [id_producto, nombre_producto, precio_producto, stock_producto, nombre_categoria, nombre_proveedor]
    
    # Validación de existencia simple por nombre
    existe = False
    i = 0
    while i < len(productos) and not existe:
        if productos[i][1] == nombre_producto:
            existe = True
        i += 1

    if not existe:
        productos.append(fila_productos)
        fila_categorias = [id_categoria, nombre_categoria, id_producto, nombre_producto]
        categorias.append(fila_categorias)
        fila_proveedores = [id_proveedor, nombre_proveedor, telefono_proveedor, id_producto, nombre_producto]
        proveedores.append(fila_proveedores)
        print("\n Producto cargado exitosamente.")
    else:
        print("\n Ya existe este producto en el inventario.")
        
    return productos, id_producto, id_categoria, id_proveedor


def obtener_stock(fila):
    """ Retorna el valor del stock (índice 3) para que sorted pueda ordenar """
    return fila[3]


#  FUNCION PARA ORDENAMIENTO
def ordenar_por_stock(matriz, descendente=False):
    """ Ordena la matriz usando la función auxiliar """
    return sorted(matriz, key=obtener_stock, reverse=descendente)

def imprimir_inventario(identidad, encabezado_identidad, titulo="REPORTE"):
    
    
    if not identidad:
        print("\n No hay datos para mostrar.")
        return

    ancho = 15
    print("\n" + "=" * (ancho * len(encabezado_identidad)))
    print(f"{titulo:^{ancho * len(encabezado_identidad)}}")
    print("=" * (ancho * len(encabezado_identidad)))

    # Encabezados
    for titulo_col in encabezado_identidad:
        print(f"{titulo_col:<{ancho}}", end="")
    print("\n" + "-" * (ancho * len(encabezado_identidad)))

    # Filas
    for fila in identidad:
        for dato in fila:
            print(f"{str(dato):<{ancho}}", end="")
        print()
    print("=" * (ancho * len(encabezado_identidad)) + "\n")

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
encabezado_provider = ["ID", "Proveedor", "Telefono", "ID Producto", "Producto"]

ventas = []
id_ventas = 0
encabezado_ventas = ["ID Venta", "ID Producto", "Cantidad Vendida", "Precio Total"]
# BUCLE PRINCIPAL 
opcion = ""

while opcion != "0":
    main() # Muestra menu
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Ejecutamos la carga
        productos, id_producto, id_categoria, id_proveedor = carga_producto(
            productos, id_producto, categorias, id_categoria, proveedores, id_proveedor
        )

    elif opcion == "6":
        # Mostramos los reportes que ya teniamos
        imprimir_inventario(productos, encabezado_producto, "INVENTARIO COMPLETO")
        
        inv_asc = ordenar_por_stock(productos, descendente=False)
        imprimir_inventario(inv_asc, encabezado_producto, "STOCK: MENOR A MAYOR")
        
        inv_desc = ordenar_por_stock(productos, descendente=True)
        imprimir_inventario(inv_desc, encabezado_producto, "STOCK: MAYOR A MENOR")

    elif opcion == "0":
        print("\nPrograma Finalizado, suerte Crack 🔵🟡")
    
    elif opcion in ["2", "3", "4", "5"]:
        print(f"\nLa opción {opcion} no esta por ahora.")
    
    else:
        print("\nOpción no válida. Intente de nuevo.")

    ##if opcion != "0":
   ##     input("\nPresione Enter para volver al menú")