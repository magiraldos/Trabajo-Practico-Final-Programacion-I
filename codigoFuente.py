# Datos que deben estar en archivos
#========================================/
#SE CREA LISTA CON DATOS DEL KIOSCO PARA EL ENCABEZADO DE LA FACTURA
import re
empresa = ["Kiosco 'La Puerta Lijada'", "30787654321", "Saraza 6247", "caba", 2026, 4, "WWW.LAPUERTALIJADA.COM", "contacto@lapuertalijada.com"]
encabezados_detalle = ["Código", "Descripción", "P. Unitario", "Cant.", "Subtotal"]

# Lista de Diccionarios reemplazando a las Listas de listas, hay que transferir los datos hardcodeados a archivos
productos = [
    {"id": 1, "producto": "ALFAJOR OREO", "precio": 1100, "stock": 50, "categoria": "DULCE", "proveedor": "DISTRIBUIDORA DULCE SUR", "activo": "Y"},
    {"id": 2, "producto": "RED BULL", "precio": 2800, "stock": 24, "categoria": "BEBIDA", "proveedor": "ENERGIA TOTAL SA", "activo": "Y"},
    {"id": 3, "producto": "ALFAJOR JORGITO", "precio": 850, "stock": 100, "categoria": "DULCE", "GOLOSINAS DEL PLATA": 3, "activo": "Y"},
    {"id": 4, "producto": "DORITOS", "precio": 2200, "stock": 30, "categoria": "SNACK", "proveedor": "MACROSNACKS INC", "activo": "Y"},
    {"id": 5, "producto": "PAPAS LAYS", "precio": 1900, "stock": 45, "categoria": "SNACK", "proveedor": "DISTRIBUIDORA PEPSICO", "activo": "Y"},
    {"id": 6, "producto": "JUGO CEPITA", "precio": 1400, "stock": 36, "categoria": "BEBIDA", "proveedor": "CITRICOS DEL NORTE", "activo": "Y"},
    {"id": 7, "producto": "COCA COLA 600", "precio": 1650, "stock": 72, "categoria": "BEBIDA", "proveedor": "FEMSA LOGISTICA", "activo": "Y"},
    {"id": 8, "producto": "MARLBORO", "precio": 3200, "stock": 20, "categoria": "CIGARRILLOS", "proveedor": "TABACALERA CENTRAL", "activo": "Y"},
    {"id": 9, "producto": "CHICLES BELDENT", "precio": 700, "stock": 150, "categoria": "DULCE", "proveedor": "MONDELEZ DISTRIBUCION", "activo": "Y"},
    {"id": 10, "producto": "AGUA 600", "precio": 1100, "stock": 48, "categoria": "BEBIDA", "proveedor": "AGUAS DEL RETIRO", "activo": "Y"}
]

categorias = [
    {"id": 1, "categoria": "DULCE"},
    {"id": 2, "categoria": "BEBIDA"},
    {"id": 3, "categoria": "SNACK"},
    {"id": 4, "categoria": "CIGARRILLOS"},
    {"id": 5, "categoria": "GOLOSINAS"}
]

proveedores = [
    {"id": 1, "proveedor": "DISTRIBUIDORA DULCE SUR", "telefono": "1145882930"},
    {"id": 2, "proveedor": "ENERGIA TOTAL SA", "telefono": "1159220041"},
    {"id": 3, "proveedor": "GOLOSINAS DEL PLATA", "telefono": "1147618822"},
    {"id": 4, "proveedor": "MACROSNACKS INC", "telefono": "1130049512"},
    {"id": 5, "proveedor": "DISTRIBUIDORA PEPSICO", "telefono": "1148203300"},
    {"id": 6, "proveedor": "CITRICOS DEL NORTE", "telefono": "1165447189"},
    {"id": 7, "proveedor": "FEMSA LOGISTICA", "telefono": "1122904455"},
    {"id": 8, "proveedor": "TABACALERA CENTRAL", "telefono": "1143019980"},
    {"id": 9, "proveedor": "MONDELEZ DISTRIBUCION", "telefono": "1151126674"},
    {"id": 10, "proveedor": "AGUAS DEL RETIRO", "telefono": "1149902113"}
]

facturas_ventas = []

# Cuentas asociadas al Sistema con sus respectivos nombres y contraseñas
accounts = [{"username": "user","password": None}, {"username": "admin", "password": "12345"}]
#========================================

# Inicio de programa (es lo unico que tiene que quedar en "Principal")
def main(cuentas, productos, categorias, proveedores):
    """FUNCION QUE DETERMINA EL NIVEL DE ACCESO AL PROGRAMA, USUARIO O ADMIN y tronco del Sistema"""
    while True:
        try:
            menu_login()
            opcion = int(input("Seleccione forma de acceso: "))
            while opcion < 0 or opcion > 2:
                print("Opcion invalida, vuelva a intentar")
                # que se imprima lo de abajo con un poco de retraso, 1 seg y limpie pantalla 
                menu_login()
                opcion = int(input("Seleccione forma de acceso: "))
            if opcion == 1:
                nivel_permiso = 0
                menu_principal(nivel_permiso, productos, categorias, proveedores)
            elif opcion == 2:
                # con expresiones regulares podemos hacer algo aca !!!
                password_login = input("Ingrese contraseña: ")
                while password_login != cuentas[1]["password"] and password_login != "0":
                    print("Contraseña incorrecta, vuelva a intentarlo")
                    print("Ingrese 0 si desea salir \n")
                    password_login = input("Ingrese contraseña: ")
                if password_login != "0":
                    print("Acceso correcto")
                    nivel_permiso = 1
                    menu_principal(nivel_permiso, productos, categorias, proveedores)
                else:
                    main(cuentas) 
            else:
                print("Saliendo del programa...") 
                # retraso del tiempo despues del mensaje para la lectura 1 seg
            break
        except:
            print("Error en el ingreso de la opcion, intente de nuevo")
            # que se imprima lo de abajo con un poco de retraso, 1 seg y limpie pantalla
# MENUS Y SUBMENUS
#========================================/
def menu_login():
    """Impresion del menu de login"""
    print("\n" + "=" * 30)
    print("\033[33m         Acceso de Cuenta\033[0m")
    print("=" * 30)
    print("  1. Usuario")
    print("  2. Administrador")
    print("  0. Salir")
    print("-" * 30)

def menu_user():
    """Impresion del menu de usuario"""
    print("="*80)
    print(f"\033[36m{'Menu del Sistema':^80}\033[0m")
    print("="*80)
    print("1. Buscar producto, proveedor o categoria") 
    print("2. Realizar venta")
    print("0. Salir")
    
def menu_admin():
    """Impresion del menu de admininistrador"""
    print("="*80)
    print(f"\033[36m{'Menu del Sistema':^80}\033[0m")
    print("="*80)
    print("1. Gestión de Productos") 
    print("2. Gestión de Categorias") 
    print("3. Gestión de Proveedores") 
    print("4. Realizar Venta") 
    print("5. Estadisticas") 
    print("0. Salir")

def menu_principal(nivel_acceso,productos, categorias, proveedores): # HAY QUE AGREGAR EN CADA FUNCION QUE LLAME A LAS ESTRUCTURAS LOS ARGUMENTOS QUE REDIRIJAN A ELLAS, ASI EVITAMOS USAR VARIABLES GLOBALES
    """Se dirigira al operador del sistema segun el nivel de acceso, USER o ADMIN, que dispondra de un abanico de funcines en relacion al rol correspondiente"""
    if nivel_acceso == 0:
        while True:
            try:
                menu_user()
                opcion = int(input("Seleccione forma de acceso: "))
                while opcion < 0 or opcion > 2:
                    print("Opcion invalida, vuelva a intentar")
                    # que se imprima lo de abajo con un poco de retraso, 1 seg y limpie pantalla 
                    menu_user()
                    opcion = int(input("Seleccione forma de acceso: "))
                if opcion == 1:
                    print("a")
                elif opcion == 2:
                    print("b")
                else:
                    print("Saliendo del programa")
                    break
            except:
                print("Error en el ingreso de la opcion")
    else:
        while True:
            try:
                menu_admin()
                opcion = int(input("Ingrese opcion: "))
                while opcion < 0 or opcion > 5:
                    print("Opcion invalida, vuelva a intentar")
                    # que se imprima lo de abajo con un poco de retraso, 1 seg y limpie pantalla 
                    menu_admin()
                    opcion = int(input("Seleccione forma de acceso: "))
                if opcion == 1:
                    menu_gestion_productos()
                    opcion == int(input("Ingrese opcion: "))
                    if opcion == 1:
                        cargar_nuevo_producto(productos, categorias, proveedores)
                    elif opcion == 2:
                        buscar_producto()
                    elif opcion == 2:
                        modificar_producto()
                    elif opcion == 2:
                        eliminar_producto()
                elif opcion == 2:
                    menu_gestion_categorias(productos, categorias, proveedores)
                    opcion == int(input("Ingrese opcion: "))

                elif opcion == 3:
                    menu_gestion_proveedores(productos, categorias, proveedores)
                elif opcion == 4:
                    print("d")
                elif opcion == 5:
                    print("e")
                else:
                    print("Saliendo del programa")
                    break
            except:
                print("Error en el ingreso de la opcion")

def menu_gestion_productos():
    """ Menu de la gestion de productos"""
    print("="*80)
    print(f"\033[36m{'CRUD | Productos':^80}\033[0m")
    print("="*80)
    print("1. Carga de Producto") 
    print("2. Busqueda de Producto") 
    print("3. Modificación de Producto") 
    print("4. Eliminacion de producto") 
    print("0. Salir")
 
def submenu_busqueda_productos():
    """Submenu de la funcion de busqueda de productos"""
    print("="*80)
    print(f"\033[36m{'Busqueda de Productos':^80}\033[0m")
    print("="*80)
    print("1. Por coincidencia en el texto") 
    print("2. Rango de precios") 
    print("3. Por estado") 
    print("4. Productos sin categoria") 
    print("5. Productos sin proveedor")
    print("0. Salir")

def submenu_modificar_productos():
    """Modificar datos del producto"""
    print("="*80)
    print(f"\033[36m{'Modificacion de Productos':^80}\033[0m")
    print("="*80)
    print("1. Nombre") 
    print("2. Precio") 
    print("3. Stock") 
    print("4. Cateogria") 
    print("5. Proveedor")
    print("6. Estado")
    print("0. Salir")

def menu_gestion_categorias():
    """ Menu de la gestion de productos"""
    print("="*80)
    print(f"\033[36m{'CRUD | Categorias':^80}\033[0m")
    print("="*80)
    print("1. Carga de Categoria") 
    print("2. Busqueda de Categoria") 
    print("3. Modificación de Categoria") 
    print("4. Eliminacion de Categoria") 
    print("0. Salir")

def submenu_busqueda_categorias():
    """submenu de busqueda de categorias"""
    print("="*80)
    print(f"\033[36m{'Busqueda de Categorias':^80}\033[0m")
    print("="*80)
    print("1. Por coincidencia en el texto") 
    print("2. Volumen de productos") 
    print("3. ") 
    print("4. Productos sin categoria") 
    print("5. Productos sin proveedor")
    print("0. Salir")
    
def submenu_modificar_categorias():
    """submenu de modificación de categorias"""
    print("="*80)
    print(f"\033[36m{'Modificacion de Categorias':^80}\033[0m")
    print("="*80)
    print("1. Nombre") 
    print("2. ") 
    print("3. ") 
    print("0. Salir")
    
def menu_gestion_proveedores():
    """ Menu de la gestion de productos"""
    print("="*80)
    print(f"\033[36m{'CRUD | Proveedores':^80}\033[0m")
    print("="*80)
    print("1. Carga de Proveedores") 
    print("2. Busqueda de Proveedores") 
    print("3. Modificación de Proveedores") 
    print("4. Eliminacion de Proveedores") 
    print("0. Salir")

def submenu_busqueda_proveedores():
    """Submenu con las opciones  de busqueda de proveedores"""
    print("="*80)
    print(f"\033[36m{'Busqueda de Proveedores':^80}\033[0m")
    print("="*80)
    print("1 ") 
    print("2. ") 
    print("3. ") 
    print("4. ") 
    print("0. Salir")
    
def submenu_modificar_proveedores():
    """Submenu con las opciones de modificación de categorias"""
    print("="*80)
    print(f"\033[36m{'Modificacion de Proveedores':^80}\033[0m")
    print("="*80)
    print("1. Nombre") 
    print("2. telefono") 
    print("0. Salir")
    
#========================================  

# CRUD
#========================================/
def cargar_nuevo_producto(productos, categorias, proveedores):
    """agrega nuevo producto al sistema"""
    producto = input("Ingrese nombre del nuevo producto: ").upper()
    # Buscamos coincidencias en la lista de diccionarios
    # esto deberia estar en busqueda de productos, es decir, hacerla una funcion para poder reutilizarla aca y allá
    coincidencias = [p for p in productos if re.search(producto, p["producto"])]
    if coincidencias:
        print(f"\nSe encontraron productos similares a '{producto}':")
        print(f"{'ID':<4}| {'PRODUCTO':<20}")
        print("-" * 26)
        for p in coincidencias:
            print(f"{p['id']:<4}| {p['producto']:<20}")
    else:
        print("\nNo se encontraron coincidencias\n")

    while True:
        try:
            eleccion = input("\n¿Desea cargar nuevo producto ( N / Y)? ").upper()
            while eleccion != "Y" and eleccion != "N":
                print("Error, eleccion invalida, vuelva a intentar")
                eleccion = input("Ingrese N / Y:  ").upper()
                
            if eleccion == "Y":
                # --- Lógica de Carga ---
                # Para el ID, buscamos el máximo ID actual en la lista y sumamos 1
                nuevo_id = len(productos) + 1
                print("\nCARGA DE PRODUCTO NUEVO")
                producto = input("Ingrese nombre del producto nuevamente: ").upper()
                precio = int(input("Ingrese el precio: "))
                while precio <= 0:
                    print("Error, el precio debe ser mayor a 0")
                    precio = int(input("Ingrese precio: "))
                stock = int(input("Ingrese el stock inicial: "))
                while stock < 0:
                    print("Error, el stock debe ser mayor o igual a 0")
                    precio = int(input("Ingrese stock: "))
                # Relacionar producto con categoria
                print("\n--- CATEGORIA ---") #Imprime las categorias actuales para que el usuario pueda elegir sin duplicar
                print(f"\nCategorias existentes:")
                print("=" * 26)
                print(f"{'ID':<4}| {'CATEGORIA':<20}")
                print("-" * 26)
                for cat in categorias:
                    print(f"{cat['id']:<4}| {cat['categoria']:<20}")
                sel = int(input("Ingrese el ID de la categoría deseada ( 0 para una nueva): "))
                max_id_cat = len(categorias) #Tomo el maximo para asegurarme que el usuario coloque un id valido
                while sel < 0 or sel > max_id_cat:
                    sel = int(input("SELECCIÓN INCORRECTA, INTENTE NUEVAMENTE: "))
                if sel != 0: #Si la opcion ingresada corresponde a un id valido automaticamente tomo el valor del nombre para ese id
                    categoria = categorias[sel - 1]["categoria"] 
                else: #Si el usuario ingresa 0 le permito cargar una nueva categoria
                    categoria = cargar_nueva_categoria(categorias)
                print("\n--- PROVEEDOR ---") 
                print(f"\Proveedores existentes:")
                print("=" * 26)
                print(f"{'ID':<4}| {'PROVEEDOR':<20}")
                print("-" * 26)
                for prov in proveedores:
                    print(f"{prov['id']:<4}| {prov['proveedor']:<20}")
                sel = int(input("Ingrese el ID del proveedor deseado ( 0 para una nueva): "))
                max_id_prov = len(proveedores) 
                while sel < 0 or sel > max_id_prov:
                    sel = int(input("SELECCIÓN INCORRECTA, INTENTE NUEVAMENTE: "))
                if sel != 0: 
                    proveedor = proveedores[sel - 1]["proveedor"] 
                else: 
                    proveedor = cargar_nuevo_proveedor(proveedores)
                    
                # Confirmacion de todos los datos que se cargaran en productos
                confirmar = input(f"¿Confirma la carga de {producto}? ( N / Y ): ").upper()
                while confirmar != "Y" and confirmar != "N":
                    print("Opcion invalida, vuelva a intentarlo")
                    confirmar = input(f"¿Confirma la carga de {producto}? ( N / Y ): ")
                if confirmar == "Y":
                    nuevo_producto = {
                        "id": nuevo_id,
                        "producto": producto,
                        "precio": precio,
                        "stock": stock,
                        "categoria": categoria,
                        "proveedor": proveedor,
                        "activo": "Y"
                    }
                    productos.append(nuevo_producto)
                    print(f"Producto {producto} cargado con éxito.")
                else:
                    print(f"Carga del Producto {producto} cancelada")       
            break
        except:
            print("Eleccion no valida, vuelva a intentar")

def buscar_producto():
    try:
        submenu_busqueda_productos()
        opcion = int(input("Ingrese opcion: "))
        while opcion < 0 and opcion > 5:
            print("Opcion invalida, vuelva a intentarlo")
            submenu_busqueda_productos()
            opcion = int(input("Ingrese opcion: "))
    except:
        print("ERROR, opcion invalida")
    "busca producto en el sistema // por texto predictivo, por rango de precios (min,max), por estado (baja logica), ¿por stock crítico (habría que establecer el minimo y agregar una bandera que indique el estado), productos sin proveedor, productos sin proveedor?"
def modificar_producto():
    "modifica los datos de un producto del sistema // se me ocurre que cuando se eliminen proveedores de productos existentes, estos pasen a figurar Sin proveedor, y puedas modificar por filtros todos esos, capaz filtrando tambien por categoría, viceversa"
def eliminar_producto():
    "elimina producto del sistema, junto con todos sus datos (afectara tambien a categorias y proveedores)"

def cargar_nueva_categoria(categorias):
    """agrega nueva categoria al sistema"""
    categoria = input("Ingrese nombre de la categoria para encontrar coincidencias: ").upper()
    # Buscamos coincidencias en la lista de diccionarios de categorias
    coincidencias = [c for c in categorias if re.search(categoria, c["categoria"])]
    if coincidencias:
        print(f"\nSe encontraron categorias similares a '{categoria}':")
        print(f"{'ID':<4}| {'CATEGORIA':<20}")
        print("-" * 26)
        for c in coincidencias:
            print(f"{c['id']:<4}| {c['categoria']:<20}")
    else:
        print("\nNo se encontraron coincidencias\n")
    
    categoria = input("Ingrese nombre de la nueva categoria (0 para cancelar): ").upper()
    while categoria in categorias[1]["categoria"] and categoria != "0":
        print(f"ERROR, la categoria '{categoria}' ya existe")
        categoria = input("Ingrese la nueva categoria: ").upper()
    if categoria != "0":
        nuevo_id_categoria = len(categorias) + 1
        nueva_categoria = {
            "id": nuevo_id_categoria,
            "categoria": categoria
        }
        categorias.append(nueva_categoria)
        print("Nueva categoria cargada con exito")
    else:
        print("Se ha cancelado la carga de categoria o se asigno SINCATEGORIA")
        categoria = "SINCATEGORIA"
    return categoria

    
def buscar_categoria():
    "busca categoria en el sistema // por texto predictivo, según el volumen de productos que contienen, ¿categorias vacias?"
    
def modificar_categoria():
    "modifica los datos de una categoria del sistema"
def eliminar_categoria():
    "elimina categoria del sistema, junto con todos sus datos (afectara tambien a productos)"

def cargar_nuevo_proveedor(proveedores):
    proveedor = input("Ingrese nombre del proveedor para encontrar coincidencias: ").upper()
    # Buscamos coincidencias en la lista de diccionarios de proveedores
    coincidencias = [prov for prov in proveedores if re.search(proveedor, prov["proveedor"])]
    if coincidencias:
        print(f"\nSe encontraron proveedores similares a '{proveedor}':")
        print(f"{'ID':<4}| {'PROVEEDOR':<20}")
        print("-" * 26)
        for prov in proveedores:
            print(f"{prov['id']:<4}| {prov['proveedor']:<20}")
    else:
        print("\nNo se encontraron coincidencias\n")
    
    proveedor = input("Ingrese nombre del nuevo proveedor (0 para cancelar): ").upper()
    while proveedor in proveedores[1]["proveedor"] and proveedor != "0":
        print(f"ERROR, el proveedor '{proveedor}' ya existe")
        proveedor = input("Ingrese el nuevo proveedor: ").upper()
    if proveedor != "0":
        telefono = int(input("Ingrese telefono del proveedor (10 digitos): "))
        while telefono < 10000000 and telefono > 99999999:
            print("Error, telefono invalido, vuelva a intentar ")
            telefono = int(input("Ingrese telefono del proveedor (10 digitos): "))
        nuevo_id_proveedor = len(proveedores) + 1
        nuevo_proveedor = {
            "id": nuevo_id_proveedor,
            "proveedor": proveedor,
            "telefono": telefono
        }
        proveedores.append(nuevo_proveedor)
        print("Nuevo proveedor cargado con exito")
    else:
        print("Se ha cancelado la carga del proveedor con exito o asignado SINPROVEEDOR")
        proveedor = "SINPROVEEDOR"
    return proveedor
    
def buscar_proveedor():
    "busca proveedor en el sistema // por texto predictivo, por reputación (nuevo campo, al crear un proveedor, este recibe Sin evaluacion)"
def modificar_proveedor():
    "modifica los datos de un proveedor del sistema"
def eliminar_proveedor():
    "elimina proveedor del sistema, junto con todos sus datos (afectara tambien a productos)"
#=========================================

# Funcion exclusiva de vendedor + pedacitos del crud (buscar producto, categoría o proveedor)
#========================================/
def realizar_venta():
    "Realizar venta, esto afectara al sistema de stock de los productos vendidos, generar factura"
    
#========================================
    
# Funciones exclusivas de administrador + CRUD COMPLETO DE CADA ENTIDAD + Funcion exclusiva del vendedor
#========================================/
def estadisticas():
    "Esta funcion debe reflejar las estadisticas del negocio en funcion de las ventas y otras cosas"
#========================================

# Inicio del programa
main(accounts, productos, categorias, proveedores)
