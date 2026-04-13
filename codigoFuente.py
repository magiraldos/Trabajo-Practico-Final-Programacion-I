
def main():
    print("Log in") 
    print("1. Usuario")
    print("2. Administrador")
    opcion = int(input("Ingrese opcion: "))
    while opcion <= 0 or opcion > 2:
        print("Opcion invalida. Vuelva a intentarlo")
        opcion = int(input("Ingrese opcion: "))
    
    if opcion == 1:
        menu_user()
    else:
        menu_admin(clave_sistema)
        
def menu_user():
    """
    Función que determina el alcance del menú del usuario (operador / empleado)
    Acceso parcial del sistema
    """
    print("Menu Usuario")
    print("1. Realizar venta")
    print("2. Buscar producto, categoria o proveedor")
    print("0. Salir ")
    opcion = int(input("Ingrese opcion: "))
    while opcion < 0 or opcion > 5:
        print("Error, opcion no valida. Intente de nuevo")
        opcion = int(input("Ingrese opcion: "))
    
    if opcion == 1:
        print("opcion 1")
    elif opcion == 2:
        print("Busqueda de...")
        print("1. Productos")
        print("2. Categorias")
        print("3. Proveedores")
        sub_opcion = int(input("Ingrese opcion: "))
        while opcion <= 0 or opcion > 3:
            print("Error, opcion no valida. Intente de nuevo")
            opcion = int(input("Ingrese opcion: "))
        if sub_opcion == 1:
            buscar_productos(productos, encabezado_producto)
        elif sub_opcion == 2:
            print("Buscar categorias")
        else:
            print("Buscar proveedores")
    else:
        print("Saliendo del programa")

def menu_admin(clave_sistema):
    """
    Función que determina el alcance del menú del Administrador ( gerente / dueño)
    Acceso total del sistema
    """
    clave_entrante = input("Ingrese clave: ")
    # clave_sistema estará previamente definida
    if clave_entrante != clave_sistema:
        print("Error, clave incorrecta. Acceso denegado")
        main()
    else:
        print("Menu Administrador")
        print("1. Agregar nuevo producto")
        print("2. Buscar producto, categoria o preveedor")
        print("3. Modificar producto, categoria o proveedor")
        # Nota: que se muestren todos los productos al admin y al user solo los que tienen la bandera de baja lógica en falso
        print("4. Dar de baja producto")
        print("5. Estadisticas")
        print("0. Salir")
        opcion = int(input("Ingrese opcion: "))
        while opcion < 0 or opcion > 5:
            print("Error, opcion no valida. Intente de nuevo")
            opcion = int(input("Ingrese opcion: "))
        if opcion == 1:
            carga_producto(productos, id_producto, categorias, id_categoria, proveedores, id_proveedor)
        elif opcion == 2:
            print("opcion 2")
        elif opcion == 3:
            print("opcion 3")
        elif opcion == 4:
            print("opcion 4")
        elif opcion == 5:
            print("opcion 5")
        else:
            print("Saliendo del programa")

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
    # Si no existe se agregan los datos a las matrices
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
            dato_str = str(dato)
            if len(dato_str)>11:
                print(f"{str(dato_str):<{ancho}}"[:11] + "... ", end="")
            else:
                print(f"{str(dato_str):<{ancho}}", end="")
        print()
    print("=" * (ancho * len(encabezado_identidad)) + "\n")

def imprimir_otras_matrices(identidad, encabezado_identidad):
    """
    Funcion que sirve para imprimir otras matrices más basicas que la de inventario que es mas grande.
    Ej: proveedores, categoria, etc.
    """

def modificar_productos(productos):
    if not productos:
        print("El producto es inexistente")
        return productos
    
    buscar = int(input("Ingrese el ID del producto que quiere modificar: "))

    id_encontrado = -1
    for i in range(len(productos)):
        if productos[i][0] == buscar:
            id_encontrado = i

    if id_encontrado != -1:
        print(f"Producto encontrado: {productos[id_encontrado][1]}")
        print("1. Modificar Nombre")
        print("2. Modificar Precio")
        print("3. Modificar Stock")
        print("0. Cancelar operacion")
        opcionDos = int(input("Que desea modificar: "))

        if opcionDos == 1:
            nombre_modificado = input("ingrese el nombre nuevo: ")
            productos[id_encontrado][1] = nombre_modificado
        elif opcionDos == 2:
            precio_modificado = int(input("ingrese el nuevo precio: "))
            while precio_modificado <= 0:
                precio_modificado = int(input("El precio tiene que ser mayor a 0: "))
            productos[id_encontrado][2] = precio_modificado
        elif opcionDos == 3:
            stock_modificado = int(input("ingrese el nuevo stock: "))
            while stock_modificado <= 0:
                stock_modificado = int(input("El stock tiene que ser mayor a 0: "))
            productos[id_encontrado][3] = stock_modificado
        else:
            print("cancelado o no valido")
    else:
        print("No encontrado")
    return productos

def buscar_productos(productos, encabezado_producto):
    if not productos:
        print("El producto es inexistente")
        return productos
    buscarProductos = input("Ingrese el nombre, proovedor o categoria del producto deseado: ")
    resultados = []

    for filas in productos:
        if ((buscarProductos in str(filas[1])) or (buscarProductos in str(filas[4])) or (buscarProductos in str(filas[5]))):
            resultados.append(filas)

    print(f"Si, encontre {len(resultados)} !")
    imprimir_inventario(resultados, encabezado_producto, f"resultados encontrados para: {buscar_productos}")
#Esto estará en un archivo imagino ?
# Definimos las estructuras de datos: Matrices y sus respectivos encabezados y ids
# Cuando se va a cargar, se deben llenar todas las matrices (a excepción de ventas que es para el egreso)
# Despues se cambia
clave_sistema = "12345"

productos = [
[1, "ALFAJOR OREO", 1100, 50, "DULCE", "DISTRIBUIDORA DULCE SUR"],
[2, "RED BULL", 2800, 24, "BEBIDA", "ENERGIA TOTAL SA"],
[3, "JORGITO", 850, 100, "DULCE", "GOLOSINAS DEL PLATA"],
[4, "DORITOS", 2200, 30, "SNACK", "MACROSNACKS INC"],
[5, "PAPAS LAYS", 1900, 45, "SNACK", "DISTRIBUIDORA PEPSICO"],
[6, "JUGO CEPITA", 1400, 36, "BEBIDA", "CITRICOS DEL NORTE"],
[7, "COCA COLA 600", 1650, 72, "BEBIDA", "FEMSA LOGISTICA"],
[8, "MARLBORO", 3200, 20, "CIGARRILLOS", "TABACALERA CENTRAL"],
[9, "CHICLES BELDENT", 700, 150, "DULCE", "MONDELEZ DISTRIBUCION"],
[10, "AGUA 600", 1100, 48, "BEBIDA", "AGUAS DEL RETIRO"]
]
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

main()