import crud
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
    opcion = 100
    while opcion != 0:
        print("="*80)
        print(f"{'Menu de estadisticas':^80}") #submenu
        print("="*80)
        print("1. Listado de productos") 
        print("2. Reportes de ventas")
        print("0. Regresar al menu anterior")
        opcion = int(input("Ingrese opcion deseada: "))
        if opcion == 1:
            crud.listado_de_productos()
        elif opcion == 2:
            crud.reporte_ventas()
                       