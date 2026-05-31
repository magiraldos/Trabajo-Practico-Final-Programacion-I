import crud
#========================================/
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
                        crud.cargar_nuevo_producto(productos, categorias, proveedores)
                    elif opcion == 2:
                        crud.buscar_producto()
                    elif opcion == 2:
                        crud.modificar_producto()
                    elif opcion == 2:
                        crud.eliminar_producto()
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