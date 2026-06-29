import json
import menus

#========================================
# CARGA Y GUARDADO DE ARCHIVOS JSON
#========================================

def _cargar(archivo, clave):
    """Carga una lista desde un archivo JSON"""
    try:
        with open(archivo, encoding="utf-8") as f:
            return json.load(f)[clave]
    except FileNotFoundError:
        print(f"ERROR: No se encontro el archivo '{archivo}'.")
        return []
    except Exception:
        print(f"ERROR: No se pudo leer el archivo '{archivo}'.")
        return []

def _guardar(archivo, clave, datos):
    """Guarda una lista en un archivo JSON"""
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump({clave: datos}, f, ensure_ascii=False, indent=4)
    except Exception:
        print(f"ERROR: No se pudo guardar el archivo '{archivo}'.")

#========================================
# INICIO DEL PROGRAMA
#========================================

def main():
    """Carga datos desde JSON y arranque del sistema"""
    productos   = _cargar("archivos/productos.json",   "productos")
    categorias  = _cargar("archivos/categorias.json",  "categorias")
    proveedores = _cargar("archivos/proveedores.json", "proveedores")
    cuentas     = _cargar("archivos/cuentas.json",     "accounts")
    while True:
        try:
            menus.menu_login()
            opcion = int(input("Seleccione forma de acceso: "))
            while opcion < 0 or opcion > 2:
                print("Opcion invalida, vuelva a intentar")
                menus.menu_login()
                opcion = int(input("Seleccione forma de acceso: "))
            if opcion == 1:
                menus.menu_principal(0, productos, categorias, proveedores)
            elif opcion == 2:
                password_login = input("Ingrese contrasena: ")
                while password_login != cuentas[1]["password"] and password_login != "0":
                    print("Contrasena incorrecta, vuelva a intentarlo")
                    print("Ingrese 0 si desea salir\n")
                    password_login = input("Ingrese contrasena: ")
                if password_login != "0":
                    print("Acceso correcto")
                    menus.menu_principal(1, productos, categorias, proveedores)
            else:
                print("Saliendo del programa...")
                # Persistir cambios al salir
                _guardar("archivos/productos.json",   "productos",  productos)
                _guardar("archivos/categorias.json",  "categorias", categorias)
                _guardar("archivos/proveedores.json", "proveedores", proveedores)
                break
        except ValueError:
            print("Error: ingrese un numero valido")
        except Exception:
            print("Error inesperado, intente de nuevo")

main()
