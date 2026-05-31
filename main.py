import re
import datos
import menus
import crud
import funexclusivas

# Inicio de programa (es lo unico que tiene que quedar en "Principal")
def main(cuentas, productos, categorias, proveedores):
    """FUNCION QUE DETERMINA EL NIVEL DE ACCESO AL PROGRAMA, USUARIO O ADMIN y tronco del Sistema"""
    while True:
        try:
            menus.menu_login()
            opcion = int(input("Seleccione forma de acceso: "))
            while opcion < 0 or opcion > 2:
                print("Opcion invalida, vuelva a intentar")
                # que se imprima lo de abajo con un poco de retraso, 1 seg y limpie pantalla 
                menus.menu_login()
                opcion = int(input("Seleccione forma de acceso: "))
            if opcion == 1:
                nivel_permiso = 0
                menus.menu_principal(nivel_permiso, productos, categorias, proveedores)
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
                    menus.menu_principal(nivel_permiso, productos, categorias, proveedores)
                else:
                    main(cuentas) 
            else:
                print("Saliendo del programa...") 
                # retraso del tiempo despues del mensaje para la lectura 1 seg
            break
        except:
            print("Error en el ingreso de la opcion, intente de nuevo")
            # que se imprima lo de abajo con un poco de retraso, 1 seg y limpie pantalla

# Inicio del programa
main(datos.accounts, datos.productos, datos.categorias, datos.proveedores)
