import crud
import funexclusivas

#========================================
# MENUS DE IMPRESION
#========================================

def menu_login():
    """Menu de login"""
    print("\n" + "=" * 30)
    print("\033[33m         Acceso de Cuenta\033[0m")
    print("=" * 30)
    print("  1. Usuario")
    print("  2. Administrador")
    print("  0. Salir")
    print("-" * 30)

def menu_user():
    """Menu de usuario"""
    print("=" * 80)
    print(f"\033[36m{'Menu del Sistema':^80}\033[0m")
    print("=" * 80)
    print("1. Buscar producto, proveedor o categoria")
    print("2. Realizar venta")
    print("0. Salir")

def menu_admin():
    """Menu de administrador"""
    print("=" * 80)
    print(f"\033[36m{'Menu del Sistema':^80}\033[0m")
    print("=" * 80)
    print("1. Gestion de Productos")
    print("2. Gestion de Categorias")
    print("3. Gestion de Proveedores")
    print("4. Realizar Venta")
    print("5. Estadisticas")
    print("0. Salir")

def menu_gestion_productos():
    """Menu CRUD de productos"""
    print("=" * 80)
    print(f"\033[36m{'CRUD | Productos':^80}\033[0m")
    print("=" * 80)
    print("1. Carga de Producto")
    print("2. Busqueda de Producto")
    print("3. Modificacion de Producto")
    print("4. Eliminacion de Producto")
    print("0. Volver")

def submenu_busqueda_productos():
    """Submenu de busqueda de productos"""
    print("=" * 80)
    print(f"\033[36m{'Busqueda de Productos':^80}\033[0m")
    print("=" * 80)
    print("1. Por coincidencia en el texto")
    print("2. Rango de precios")
    print("3. Por estado (activo / inactivo)")
    print("4. Productos sin categoria")
    print("5. Productos sin proveedor")
    print("0. Volver")

def submenu_modificar_productos():
    """Submenu de modificacion de productos"""
    print("=" * 80)
    print(f"\033[36m{'Modificacion de Productos':^80}\033[0m")
    print("=" * 80)
    print("1. Nombre")
    print("2. Precio")
    print("3. Stock")
    print("4. Categoria")
    print("5. Proveedor")
    print("6. Estado")
    print("0. Volver")

def menu_gestion_categorias():
    """Menu CRUD de categorias"""
    print("=" * 80)
    print(f"\033[36m{'CRUD | Categorias':^80}\033[0m")
    print("=" * 80)
    print("1. Carga de Categoria")
    print("2. Busqueda de Categoria")
    print("3. Modificacion de Categoria")
    print("4. Eliminacion de Categoria")
    print("0. Volver")

def submenu_busqueda_categorias():
    """Submenu de busqueda de categorias"""
    print("=" * 80)
    print(f"\033[36m{'Busqueda de Categorias':^80}\033[0m")
    print("=" * 80)
    print("1. Por coincidencia en el texto")
    print("2. Por volumen de productos")
    print("0. Volver")

def menu_gestion_proveedores():
    """Menu CRUD de proveedores"""
    print("=" * 80)
    print(f"\033[36m{'CRUD | Proveedores':^80}\033[0m")
    print("=" * 80)
    print("1. Carga de Proveedor")
    print("2. Busqueda de Proveedor")
    print("3. Modificacion de Proveedor")
    print("4. Eliminacion de Proveedor")
    print("0. Volver")

def submenu_busqueda_proveedores():
    """Submenu de busqueda de proveedores"""
    print("=" * 80)
    print(f"\033[36m{'Busqueda de Proveedores':^80}\033[0m")
    print("=" * 80)
    print("1. Por coincidencia en el texto")
    print("2. Listado completo")
    print("0. Volver")

def submenu_modificar_proveedores():
    """Submenu de modificacion de proveedores"""
    print("=" * 80)
    print(f"\033[36m{'Modificacion de Proveedores':^80}\033[0m")
    print("=" * 80)
    print("1. Nombre")
    print("2. Telefono")
    print("0. Volver")


#========================================
# NAVEGACION PRINCIPAL
#========================================

def menu_principal(nivel_acceso, productos, categorias, proveedores):
    """Redirige al menu correspondiente segun el nivel de acceso"""
    if nivel_acceso == 0:
        _menu_usuario(productos, categorias, proveedores)
    else:
        _menu_administrador(productos, categorias, proveedores)


def _menu_usuario(productos, categorias, proveedores):
    """Loop del menu de usuario"""
    while True:
        try:
            menu_user()
            opcion = int(input("Seleccione una opcion: "))
            while opcion < 0 or opcion > 2:
                print("Opcion invalida, vuelva a intentar")
                menu_user()
                opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                crud.buscar_producto(productos, categorias, proveedores)
            elif opcion == 2:
                funexclusivas.realizar_venta()
            else:
                print("Saliendo del programa. Hasta luego!")
                break
        except ValueError:
            print("Error en el ingreso de la opcion")


def _menu_administrador(productos, categorias, proveedores):
    """Loop del menu de administrador"""
    while True:
        try:
            menu_admin()
            opcion = int(input("Ingrese opcion: "))
            while opcion < 0 or opcion > 5:
                print("Opcion invalida, vuelva a intentar")
                menu_admin()
                opcion = int(input("Ingrese opcion: "))

            if opcion == 1:
                _submenu_productos(productos, categorias, proveedores)
            elif opcion == 2:
                _submenu_categorias(productos, categorias)
            elif opcion == 3:
                _submenu_proveedores(productos, proveedores)
            elif opcion == 4:
                funexclusivas.realizar_venta()
            elif opcion == 5:
                funexclusivas.estadisticas()
            else:
                print("Saliendo del programa. Hasta luego!")
                break
        except ValueError:
            print("Error en el ingreso de la opcion")


#========================================
# SUBMENUS DE NAVEGACION
#========================================

def _submenu_productos(productos, categorias, proveedores):
    """Loop del submenu de gestion de productos"""
    while True:
        try:
            menu_gestion_productos()
            opcion = int(input("Ingrese opcion: "))
            while opcion < 0 or opcion > 4:
                print("Opcion invalida, vuelva a intentar")
                menu_gestion_productos()
                opcion = int(input("Ingrese opcion: "))

            if opcion == 1:
                crud.cargar_nuevo_producto(productos, categorias, proveedores)
            elif opcion == 2:
                crud.buscar_producto(productos, categorias, proveedores)
            elif opcion == 3:
                crud.modificar_producto(productos, categorias, proveedores)
            elif opcion == 4:
                crud.eliminar_producto(productos)
            else:
                break
        except ValueError:
            print("Error en el ingreso de la opcion")


def _submenu_categorias(productos, categorias):
    """Loop del submenu de gestion de categorias"""
    while True:
        try:
            menu_gestion_categorias()
            opcion = int(input("Ingrese opcion: "))
            while opcion < 0 or opcion > 4:
                print("Opcion invalida, vuelva a intentar")
                menu_gestion_categorias()
                opcion = int(input("Ingrese opcion: "))

            if opcion == 1:
                crud.cargar_nueva_categoria(categorias)
            elif opcion == 2:
                crud.buscar_categoria(productos, categorias)
            elif opcion == 3:
                crud.modificar_categoria(categorias)
            elif opcion == 4:
                crud.eliminar_categoria(productos, categorias)
            else:
                break
        except ValueError:
            print("Error en el ingreso de la opcion")


def _submenu_proveedores(productos, proveedores):
    """Loop del submenu de gestion de proveedores"""
    while True:
        try:
            menu_gestion_proveedores()
            opcion = int(input("Ingrese opcion: "))
            while opcion < 0 or opcion > 4:
                print("Opcion invalida, vuelva a intentar")
                menu_gestion_proveedores()
                opcion = int(input("Ingrese opcion: "))

            if opcion == 1:
                crud.cargar_nuevo_proveedor(proveedores)
            elif opcion == 2:
                crud.buscar_proveedor(productos, proveedores)
            elif opcion == 3:
                crud.modificar_proveedor(productos, proveedores)
            elif opcion == 4:
                crud.eliminar_proveedor(productos, proveedores)
            else:
                break
        except ValueError:
            print("Error en el ingreso de la opcion")
