# LISTAS ORIGINALES
productos = [
    [1, "ALFAJOR OREO", 1100, 50, "DULCE", "DISTRIBUIDORA DULCE SUR","Y"],
    [2, "RED BULL", 2800, 24, "BEBIDA", "ENERGIA TOTAL SA","Y"],
    [3, "ALFAJOR JORGITO", 850, 100, "DULCE", "GOLOSINAS DEL PLATA","Y"],
    [4, "DORITOS", 2200, 30, "SNACK", "MACROSNACKS INC","Y"],
    [5, "PAPAS LAYS", 1900, 45, "SNACK", "DISTRIBUIDORA PEPSICO","Y"],
    [6, "JUGO CEPITA", 1400, 36, "BEBIDA", "CITRICOS DEL NORTE","Y"],
    [7, "COCA COLA 600", 1650, 72, "BEBIDA", "FEMSA LOGISTICA","Y"],
    [8, "MARLBORO", 3200, 20, "CIGARRILLOS", "TABACALERA CENTRAL","Y"],
    [9, "CHICLES BELDENT", 700, 150, "DULCE", "MONDELEZ DISTRIBUCION","Y"],
    [10, "AGUA 600", 1100, 48, "BEBIDA", "AGUAS DEL RETIRO","Y"]
]

categorias = [
[1,"DULCE"],
[2,"BEBIDA"],
[3,"SNACK"],
[4,"CIGARRILLOS"],
[5,"GOLOSINAS"]    
]

proveedores = [
[1,"DISTRIBUIDORA DULCE SUR","1145882930",1,"ALFAJOR OREO"],
[2,"ENERGIA TOTAL SA","1159220041",2,"RED BULL"],
[3,"GOLOSINAS DEL PLATA","1147618822",3,"ALFAJOR JORGITO"],
[4,"MACROSNACKS INC","1130049512",4,"DORITOS"],
[5,"DISTRIBUIDORA PEPSICO","1148203300",5,"PAPAS LAYS"],
[6,"CITRICOS DEL NORTE","1165447189",6,"JUGO CEPITA"],
[7,"FEMSA LOGISTICA","1122904455",7,"COCA COLA 600"],
[8,"TABACALERA CENTRAL","1143019980",8,"MARLBORO X20"],
[9,"MONDELEZ DISTRIBUCION","1151126674",9,"CHICLES BELDENT"],
[10,"AGUAS DEL RETIRO","1149902113",10,"AGUA 600"]
]


#SE CREA LISTA CON DATOS DEL KIOSCO PARA EL ENCABEZADO DE LA FACTURA
empresa = ["Kiosco 'La Puerta Lijada'", "30787654321", "Saraza 6247", "caba", 2026, 4, "WWW.LAPUERTALIJADA.COM", "contacto@lapuertalijada.com"]
encabezados_detalle = ["Código", "Descripción", "P. Unitario", "Cant.", "Subtotal"]

# CREAMOS LOS DICCIONARIOS VACIOS
productos_dict = {}
categorias_dict = {}
proveedores_dict = {}
facturas_dict = {}
login_account = {}

login_account = {
    'user': None,
    'admin': 'admin',
    'pablo': 'pablo',
    'mati': 'mati',
    'tadeo': 'tadeo',
    'jero': 'jero',
    'lucas': 'lucas'
}

# RELLENAMOS LOS DICCIONARIOS CON LOS VALORES DE LAS LISTAS
for p in productos:
    productos_dict[p[0]] = {
        "nombre": p[1],
        "precio": p[2],
        "stock": p[3],
        "categoria": p[4],
        "proveedor": p[5],
        "activo": p[6]
    }

for c in categorias:
    categorias_dict[c[0]] = {
        "categoria": c[1]
    }

for p in proveedores:
    proveedores_dict[p[0]] = {
        "nombre": p[1],
        "telefono": p[2],
        "id producto": p[3],
        "producto": p[4]
    }

def imprimir_productos():
    # Imprime los enunciados de las columnas
    print(f"{"ID":<6}{"PRODUCTO":<20}{"PRECIO":<12}{"STOCK":<12}{"CATEGORIA":<20}{"PROVEEDOR":<30}{"ACTIVO"}")
    print("-" * 100) # Una línea decorativa
    #Imprime el diccionario completo
    for id_prod, datos in productos_dict.items():
        nombre = datos['nombre']
        precio = datos['precio']
        stock = datos['stock']
        cat = datos['categoria']
        prov = datos['proveedor']
        act = datos['activo']
        
        print(f"{id_prod:<6}{nombre:<20}${precio:<11}{stock:<12}{cat:<20}{prov:<30}{act:^6}")

def imprimir_producto_resaltado(sel):
# Imprime los enunciados de las columnas
    print(f"{"ID":<6}{"PRODUCTO":<20}{"PRECIO":<12}{"STOCK":<12}{"CATEGORIA":<20}{"PROVEEDOR":<30}{"ACTIVO"}")
    print("-" * 100) # Una línea decorativa
    #Imprime el diccionario completo y resalta el id recibido como argumento
    for id_prod, datos in productos_dict.items():
        nombre = datos['nombre']
        precio = datos['precio']
        stock = datos['stock']
        cat = datos['categoria']
        prov = datos['proveedor']
        act = datos['activo']
        
        if id_prod==sel:
            print(f"\033[41;37m{id_prod:<6}{nombre:<20}${precio:<11}{stock:<12}{cat:<20}{prov:<30}{act:^6}\033[0m")
        else:
            print(f"{id_prod:<6}{nombre:<20}${precio:<11}{stock:<12}{cat:<20}{prov:<30}{act:^6}")

# FUNCION PARA CARGAR NUEVO PRODUCTO
def cargar_nuevo_producto(nombre): #Ya recibe por parametro el nombre del producto
    nuevo_id = max(productos_dict.keys()) + 1 #Calcula el nuevo id para que sea incremental y unico
    precio = int(input("Ingrese el precio: "))
    while precio <= 0:
        print("Error, el precio debe ser mayor a 0")
        precio = int(input("Ingrese precio del producto: "))
    stock = int(input("Ingrese el stock inicial: "))
    while stock < 0:
        print("Error, el stock del producto debe ser un numero mayor o igual a 0")
        stock = int(input("Ingrese stock del producto: ")) 
    print("\n--- CATEGORIA ---") #Imprime las categorias actuales para que el usuario pueda elegir sin duplicar
    print(f"\nCategorias existentes:")
    print("=" * 26)
    print(f"{'ID':<6}{'CATEGORIA':<20}")
    print("-" * 26)
    for id, datos in categorias_dict.items():
        cat = datos["categoria"]
        print(f"{id:<6}{cat:<20}")
    sel = int(input("Ingrese el ID de la categoría deseada o ingrese 0 para cargar una nueva: "))
    max_id = max(categorias_dict.keys()) #Tomo el maximo para asegurarme que el usuario coloque un id valido
    while sel < 0 or sel > max_id:
        sel = int(input("SELECCIÓN INCORRECTA, INTENTE NUEVAMENTE: "))
    if sel != 0: #Si la opcion ingresada corresponde a un id valido automaticamente tomo el valor del nombre para ese id
        categoria = categorias_dict[sel]["categoria"] 
    else: #Si el usuario ingresa 0 le permito cargar una nueva categoria
        categoria = input("Ingrese la categoría: ").upper()
        nuevo_id_cat = max(categorias_dict.keys()) + 1
        categorias_dict[nuevo_id_cat] = { #Inserta la nueva categoria en el diccioanrio de categorias
            "categoria": categoria
        }
    proveedor = input("Ingrese el proveedor: ").upper()
    id_prov = max(proveedores_dict.keys()) + 1
    telefono = int(input("Ingrese el telefono del proveedor sin guiones y con codigo de area sin 0\nPor ejemplo: 1122334455: "))
    while len(str(telefono)) != 10:
        telefono = input("Telefono incorrecto, ingrese nuevamente: ")
    print(f"{"PRODUCTO":<20}{"PRECIO":<12}{"STOCK":<12}{"CATEGORIA":<20}{"PROVEEDOR":<30}{"ACTIVO"}")
    print("-" * 100)
    print(f"{nombre:<20}${precio:<11}{stock:<12}{categoria:<20}{proveedor:<30}{"Y":^6}") #Imprimo todo sin el id para confirmar
    sel = (input("Confirma los datos para su carga? (SI/NO): ")).upper()
    while sel != "SI" and sel != "NO":
        sel = input("Responda SI O NO\n¿Desea modificar alguno de estos productos? (SI/NO): ").upper()
    if sel == "SI": #Si el usuario confirma la carga se procede a rellenar los diccionarios correspondientes
        productos_dict[nuevo_id] = {
            "nombre": nombre,
            "precio": precio,
            "stock": stock,
            "categoria": categoria,
            "proveedor": proveedor,
            "activo": "Y"
        }
        print(f"\nSe cargo correctamente el producto {nombre} con el ID: {nuevo_id}, vendido por el proveedor: {proveedor}")
        proveedores_dict[id_prov] = {
            "nombre": proveedor,
            "telefono":telefono,
            "id Producto": nuevo_id,
            "producto": nombre
        }
    else:
        print(f"\nLa carga del producto {nombre} fue anulada correctamente") #Si anula la carga se desecha

def carga_stock(sel): 
    """
    Funcion para actualizar stock. Recibe como argumento el id del producto a modificar
    """
    print("=" * 45)
    print(f"{"||"}{"ACTUALIZACION DE STOCK":^38}{"||":>2}")
    print("=" * 45)
    nombre = productos_dict[sel]["nombre"]
    stock = productos_dict[sel]["stock"]
    print(f"El stock actual del producto {nombre} es de {stock}\nQue desea hacer?")
    opcion = 912 #Seteo de la variable distinta a 0 para que ingrese al bucle
    while opcion != 0: 
        print("\n1. Aumentar stock") 
        print("2. Disminuir stock") 
        print("0. Regresar al menu anterior")
        opcion = int(input("Ingrese opcion deseada: "))
        backup = productos_dict[sel]["stock"] #Guarda el stock actual en una variable por si algo sale mal
        if opcion == 1:
            nro = int(input("Ingrese el valor de unidades para agregar al stock actual: "))
            productos_dict[sel]["stock"] += nro #Sobreescribe el valor del stock
            new_stock = productos_dict[sel]["stock"]
            print(f"El nuevo stock para el producto {nombre} es de {new_stock}")
            opcion_2 = input("Confirma la operación? (SI/NO): ").upper()
            while opcion_2 != "SI" and opcion_2 != "NO":
                        opcion_2 = input("Responda SI O NO\n¿Desea modificar alguno de estos productos? (SI/NO): ").upper()
            if opcion_2 == "SI": #Si confirma la operacion se actualiza el stock
                print("El stock se ACTUALIZADO correctamente")
                opcion = 0 #Igualo la opcion a 0 para que salga del bucle principal
            else: #Si anula la operacion se vuelve a almacenar el valor del stock guardado como backup
                print("La actualización se ha CANCELADO correctamente")
                productos_dict[sel]["stock"] = backup
                opcion = 0 #Igualo la opcion a 0 para que salga del bucle principal
        elif opcion == 2:
            nro = int(input("Ingrese el valor de unidades para restar al stock actual: "))
            if nro > stock:
                print("El numero ingresado es superior al stock inicial, se reduce el stock a 0")
                nro = stock #Si se quiere restar mas del stock disponible igual la variable al stock para que quede en 0
            productos_dict[sel]["stock"] -= nro
            new_stock = productos_dict[sel]["stock"]
            print(f"El nuevo stock para el producto {nombre} es de {new_stock}")
            opcion_2 = input("Confirma la operación? (SI/NO): ").upper()
            while opcion_2 != "SI" and opcion_2 != "NO":
                        opcion_2 = input("Responda SI O NO\n¿Desea modificar alguno de estos productos? (SI/NO): ").upper()
            if opcion_2 == "SI":
                print("El stock se ha ACTUALIZADO correctamente")
                opcion = 0 #Igualo la opcion a 0 para que salga del bucle principal
            else:
                print("La actualización se ha CANCELADO correctamente")
                productos_dict[sel]["stock"] = backup
                opcion = 0 #Igualo la opcion a 0 para que salga del bucle principal
        elif opcion == 0:
            print("Regresa al menu anterior")
        else:
            print("OPCION INCORRECTA")
        
    if opcion_2 == "SI": #Si se hizo algun tipo de modificacion imprimo resaltada la modificacion realizada
        imprimir_producto_resaltado(sel)
        print("\n\n")

def carga_producto():
    """ SUBMENU para cargar producto o modificar stock de un producto existente (en caso de error en el stock de la carga de un nuevo producto)"""
    opcion = ""
    while opcion != "0":
        print("="*80)
        print(f"{'Menu de carga de producto':^80}") #submenu
        print("="*80)
        print("1. Cargar nuevo producto en el inventario") 
        print("2. Modificar stock de producto ya existente") 
        print("0. Regresar al menu anterior")
        opcion = input("Ingrese opcion deseada: ")
        if opcion == "1":
            nombre = input("Ingrese nombre del producto: ").upper()
            coincidencias = list(filter(lambda p: nombre in p[1]["nombre"],productos_dict.items())) 
            if coincidencias:
                print(f"\n Se encontraron productos similares a '{nombre}':")
                print(f"{'ID':<6}{'NOMBRE':<20}")
                print("-" * 26)
                for id_coinc, nombre_coinc in coincidencias:
                    print(f"{id_coinc:<6}{nombre_coinc['nombre']:<20}") #Muestra los productos coincidentes con la busqueda y sus respectivos ids
                sel = input("\n¿Desea modificar alguno de estos productos? (SI/NO): \n").upper()
                while sel != "SI" and sel != "NO":
                    sel = input("Responda SI O NO\n¿Desea modificar alguno de estos productos? (SI/NO): ").upper()
                if sel == "SI": #Si el usuario quiere modificar un producto ya existente se lo deriva a cargar stock
                    sel = int(input("Ingrese el ID a modificar: \n")) 
                    carga_stock(sel)
                else: #Sino se lo deriva a cargar producto
                    cargar_nuevo_producto(nombre)
            else: #Si no hay resultados en la busqueda se lo deriva a cargar producto
                print("\nNo se encontraron coincidencias, se procede a cargar un nuevo producto.\n")
                cargar_nuevo_producto(nombre)
        elif opcion == "2":
            print("\n---- PRODUCTOS ACTUALES ----\n") #Se imprimen todos los productos para que el usuario pueda elegir el id correspondiente
            imprimir_productos()
            sel = int(input("\nIngrese el ID del producto a modificar: \n")) 
            carga_stock(sel) #Se llama a la funcion cargar stock con el id del producto como argumento
        elif opcion == "0":
            print("Regresa al menu anterior")
        else:
            print("\nOpción no válida. Intente de nuevo.")

def buscar_producto():
    """SUBMENU para buscar producto, proveedor o categoria"""
    opcion = 100
    while opcion != 0:
        print("="*80)
        print(f"{'Menu de busqueda':^80}") #submenu
        print("="*80)
        print("1. Buscar producto") 
        print("2. Buscar proveedor") 
        print("3. Buscar categoria")
        print("0. Regresar al menu anterior")
        opcion = int(input("Ingrese opcion deseada: "))
        if opcion == 1:
            nombre = input("Ingrese nombre del producto a buscar: ").upper()
            coincidencias = list(filter(lambda p: nombre in p[1]["nombre"],productos_dict.items())) 
            if coincidencias:
                print(f"\n Se encontraron productos similares a '{nombre}':")
                print(f"{'ID':<6}{'NOMBRE':<20}")
                print("-" * 26)
                for id_coinc, nombre_coinc in coincidencias:
                    print(f"{id_coinc:<6}{nombre_coinc['nombre']:<20}")
                sel = int(input("Ingrese el ID del producto a desplegar: "))
                print("\n---- PRODUCTO DESGLOSADO ----\n")
                print(f"{"ID":<6}{"PRODUCTO":<20}{"PRECIO":<12}{"STOCK":<12}{"CATEGORIA":<20}{"PROVEEDOR":<30}{"ACTIVO"}")
                print("-" * 107)
                p = productos_dict[sel]
                print(f"{sel:<6}{p["nombre"]:<20}${p["precio"]:<11}{p["stock"]:<12}{p["categoria"]:<20}{p["proveedor"]:<30}{p["activo"]:^6}")
            else:
                print("\nNo se encontraron resultados para la busqueda\n")
        elif opcion == 2:
            nombre = input("Ingrese nombre del proveedor a buscar: ").upper()
            coincidencias = list(filter(lambda p: nombre in p[1]["nombre"],proveedores_dict.items())) 
            if coincidencias:
                print(f"\n Se encontraron proveedores similares a '{nombre}':")
                print(f"{'ID':<6}{'NOMBRE':<20}")
                print("-" * 26)
                for id_coinc, nombre_coinc in coincidencias:
                    print(f"{id_coinc:<6}{nombre_coinc['nombre']:<20}")
                sel = int(input("Ingrese el ID del proveedor a desglosar: "))
                print("\n---- PROVEEDOR DESGLOSADO ----\n")
                print(f"{"ID":<6}{"PROVEEDOR":<20}{"TELEFONO":<12}{"ID PRODUCTO":<6}{"PRODUCTO":<20}")
                print("-" * 69)
                p = proveedores_dict[sel]
                print(f"{sel:<6}{p["nombre"]:<20}{p["telefono"]:<12}{p["id producto"]:<6}{p["producto"]:<20}")
            else:
                print("\nNo se encontraron resultados para la busqueda\n")
        elif opcion == 3:
            nombre = input("Ingrese nombre de la categoría a buscar: ").upper()
            coincidencias = list(filter(lambda p: nombre in p[1]["categoria"],categorias_dict.items())) 
            if coincidencias:
                for id,cat in coincidencias:
                    print(f"\n Se encontró la categoría '{cat["categoria"]}' con el id {id}")
            else:
                print("\nNo se encontraron resultados para la busqueda\n")
        elif opcion == 0:
            print("Regresa al menu anterior")
        else:
            print("\nOpción no válida. Intente de nuevo.")
    
def modificar_producto():
    """SUBMENU para la modificacion de un producto o proveedor"""
    opcion = 100
    while opcion != 0:
        print("="*80)
        print(f"{'Menu de modificación':^80}") 
        print("="*80)
        print("1. Modificar producto") 
        print("2. Modificar proveedor")
        print("0. Regresar al menu anterior")
        opcion = int(input("Ingrese opcion deseada: "))
        if opcion == 1:
            nombre = input("Ingrese nombre del producto a modificar: ").upper()
            coincidencias = list(filter(lambda p: nombre in p[1]["nombre"],productos_dict.items())) 
            if coincidencias:
                print(f"\n Se encontraron productos similares a '{nombre}':")
                print(f"{'ID':<6}{'NOMBRE':<20}")
                print("-" * 26)
                for id_coinc, nombre_coinc in coincidencias:
                    print(f"{id_coinc:<6}{nombre_coinc['nombre']:<20}")
                sel = int(input("Ingrese el ID del producto a desplegar: "))
                print("\n---- PRODUCTO DESGLOSADO ----\n")
                print(f"{"ID":<6}{"PRODUCTO":<20}{"PRECIO":<12}{"STOCK":<12}{"CATEGORIA":<20}{"PROVEEDOR":<30}{"ACTIVO"}")
                print("-" * 107)
                p = productos_dict[sel]
                print(f"{sel:<6}{p["nombre"]:<20}${p["precio"]:<11}{p["stock"]:<12}{p["categoria"]:<20}{p["proveedor"]:<30}{p["activo"]:^6}")

                mod = input("Desea modificar el precio? (SI/NO): ").upper()
                while mod != "SI" and mod != "NO":
                    mod = input("Responda SI O NO\n¿Desea modificar el precio? (SI/NO): ").upper()
                if mod == "SI":
                    precio = int(input("Ingrese el nuevo precio: "))
                    p["precio"] = precio

                mod = input("Desea modificar el stock? (SI/NO): ").upper()
                while mod != "SI" and mod != "NO":
                    mod = input("Responda SI O NO\n¿Desea modificar el stock? (SI/NO): ").upper()
                if mod == "SI":
                    stock = int(input("Ingrese el nuevo stock: "))
                    p["stock"] = stock

                mod = input("Desea modificar la categoria? (SI/NO): ").upper()
                while mod != "SI" and mod != "NO":
                    mod = input("Responda SI O NO\n¿Desea modificar la categoria? (SI/NO): ").upper()
                if mod == "SI":
                    categoria=modificar_categoria
                    p["categoria"] = categoria
                print("\nProducto modificado con exito\n")
                imprimir_producto_resaltado(sel)
            else:
                print("\nNo se encontraron resultados para la busqueda\n")

        elif opcion == 2:
            nombre = input("Ingrese nombre del proveedor a modificar: ").upper()
            coincidencias = list(filter(lambda p: nombre in p[1]["nombre"],proveedores_dict.items())) 
            if coincidencias:
                print(f"\n Se encontraron proveedores similares a '{nombre}':")
                print(f"{'ID':<6}{'NOMBRE':<20}")
                print("-" * 26)
                for id_coinc, nombre_coinc in coincidencias:
                    print(f"{id_coinc:<6}{nombre_coinc['nombre']:<20}")
                sel = int(input("Ingrese el ID del proveedor a desglosar: "))
                print("\n---- PROVEEDOR DESGLOSADO ----\n")
                print(f"{"ID":<6}{"PROVEEDOR":<20}{"TELEFONO":<12}{"ID PRODUCTO":<6}{"PRODUCTO":<20}")
                print("-" * 69)
                p = proveedores_dict[sel]
                print(f"{sel:<6}{p["nombre"]:<20}{p["telefono"]:<12}{p["id producto"]:<6}{p["producto"]:<20}")
                telefono = int(input("\nIngrese el nuevo telefono del proveedor sin guiones y con codigo de area sin 0\nPor ejemplo: 1122334455: "))
                while len(str(telefono)) != 10 or type(telefono) is not int:
                    telefono = input("Telefono incorrecto, ingrese nuevamente: ")
                p["telefono"] = telefono
            else:
                print(f"\nNo se encontraron proveedores similares a {nombre}")         
        elif opcion == 0:
            print("Regresa al menu anterior")
        else:
            print("\nOpción no válida. Intente de nuevo.")           

def modificar_categoria():
    """Funcion que muestra las categorias existentes que sirve de apoyo en la carga de producto, 0 para cargar nueva, id de categoria para asignar al producto"""
    print("\n--- CATEGORIA ---")
    print(f"\nCategorias existentes:")
    print("=" * 26)
    print(f"{'ID':<6}{'CATEGORIA':<20}")
    print("-" * 26)
    for id, datos in categorias_dict.items():
        cat = datos["categoria"]
        print(f"{id:<6}{cat:<20}")
    sel = int(input("Ingrese el ID de la categoría deseada o ingrese 0 para cargar una nueva: "))
    max_id = max(categorias_dict.keys())
    while sel < 0 or sel > max_id:
        sel = int(input("SELECCIÓN INCORRECTA, INTENTE NUEVAMENTE: "))
    if sel != 0: 
        categoria = categorias_dict[sel]["categoria"]
    else:
        categoria = input("Ingrese la categoría: ").upper()
        nuevo_id_cat = max(categorias_dict.keys()) + 1
        categorias_dict[nuevo_id_cat] = {
            "categoria": categoria
        }
    return categoria

def eliminar_producto():
    imprimir_productos()
    sel = int(input("\nIngrese el id del producto a eliminar: "))
    nombre = productos_dict[sel]["nombre"]
    stock = productos_dict[sel]["stock"]
    opcion = input(f"\nConfirma la baja del producto {nombre}? (SI/NO): ").upper()
    while opcion != "SI" and opcion != "NO":
        opcion = input("Responda SI O NO\n¿Confirma la baja del producto? (SI/NO): ").upper()
    if opcion == "SI":
        if stock > 0:
            opcion = input(f"\nEl producto tiene un stock actual de {stock}. \nDesea reducirlo a 0? (SI/NO): ").upper()
            while opcion != "SI" and opcion != "NO":
                opcion = input("Responda SI O NO\n¿Confirma la reduccion del stock a 0? (SI/NO): ").upper()
            if opcion == "SI":
                productos_dict[sel]["stock"] = 0
        productos_dict[sel]["activo"] = "N" #Se hace la baja logica
        print(f"\nEl producto {nombre} fue dado de baja correctamente\n\n")
        imprimir_producto_resaltado(sel)
    else:
        print("\nOperacion cancelada con exito")

def estadisticas():
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
            listado_de_productos()
        elif opcion == 2:
            reporte_ventas()
                       
def listado_de_productos():
    print("="*80)
    print(f"{'Sub menu de estadisticas - Listado de productos':^80}") #submenu
    print("="*80)
    print("1. Ver todos los productos ordenados\n2. Ver productos filtrados por actividad\n3. Ver productos filtrados por cantidad de stock\n4. Ver productos filtrados por precio") 
    print("0. Regresar al menu anterior\n")
    opcion = int(input("Ingrese opcion deseada: "))
    while opcion < 0 or opcion > 4:
        opcion = int(input("Opcion invalida, ingrese nuevamente: "))

    if opcion == 1:
        print("\nComo quiere ordenar los productos?\n1. Por nombre\n2. Por stock\n3. Por precio")
        sel = int(input("Seleccione una opcion: "))
        while sel < 1 or sel > 3:
            sel = int(input("Opcion invalida, ingrese nuevamente: "))
        all_keys = {1: "nombre",2: "stock",3: "precio"}
        key = all_keys.get(sel)
        if sel == 1:
            asc = int(input("Ingrese 1 para ordenar por nombre A-Z\nO ingrese 2 para ordenar por nombre Z-A: "))
            while asc != 1 and asc!= 2:
                asc = int(input("Opcion invalida, ingrese nuevamente: "))
            if asc == 1:
                ordenados = sorted(productos_dict.items(), key=lambda i: i[1][key])
            else:
                ordenados = sorted(productos_dict.items(), key=lambda i: i[1][key], reverse=True)
            print(f"\n{"ID":<6}{"PRODUCTO":<20}{"PRECIO":<12}{"STOCK":<12}{"CATEGORIA":<20}{"PROVEEDOR":<30}{"ACTIVO"}")
            print("-" * 100)
            for id, datos in ordenados:
                print(f"{id:<6}{datos["nombre"]:<20}${datos["precio"]:<11}{datos["stock"]:<12}{datos["categoria"]:<20}{datos["proveedor"]:<30}{datos["activo"]:^6}")
        else:
            asc = int(input("Ingrese 1 para ordenar de forma ascendente\nO ingrese 2 para ordenar de forma descendente: "))
            while asc != 1 and asc!= 2:
                asc = int(input("Opcion invalida, ingrese nuevamente: "))
            if asc == 1:
                ordenados = sorted(productos_dict.items(), key=lambda i: i[1][key])
            else:
                ordenados = sorted(productos_dict.items(), key=lambda i: i[1][key], reverse=True)
            print(f"\n{"ID":<6}{"PRODUCTO":<20}{"PRECIO":<12}{"STOCK":<12}{"CATEGORIA":<20}{"PROVEEDOR":<30}{"ACTIVO"}")
            print("-" * 100)
            for id, datos in ordenados:
                print(f"{id:<6}{datos["nombre"]:<20}${datos["precio"]:<11}{datos["stock"]:<12}{datos["categoria"]:<20}{datos["proveedor"]:<30}{datos["activo"]:^6}")

    if opcion == 2:
        sel = input("Ingrese 'Y' para filtrar los productos activos\nO ingrese 'N' para filtrar los productos inactivos: ").upper()
        while sel != "Y" and sel != "N":
            sel = input("Opcion invalida, intente nuevamente: ").upper()
        if sel == "Y":
            filtrados = list(filter(lambda x: x[1]["activo"] == "Y",productos_dict.items()))
            print(f"\n--- Productos con status ACTIVO ---")
        else:
            filtrados = list(filter(lambda x: x[1]["activo"] == "N",productos_dict.items()))
            print(f"\n--- Productos con status INACTIVO ---")
        print(f"{"ID":<6}{"PRODUCTO":<20}{"PRECIO":<12}{"STOCK":<12}{"CATEGORIA":<20}{"PROVEEDOR":<30}{"ACTIVO"}")
        print("-" * 100)
        for id, datos in filtrados:
            print(f"{id:<6}{datos["nombre"]:<20}${datos["precio"]:<11}{datos["stock"]:<12}{datos["categoria"]:<20}{datos["proveedor"]:<30}{datos["activo"]:^6}")

    if opcion == 3:
        sel = int(input("\n1. Productos con stock MAYOR a X\n2. Productos con stock MENOR a X\nIngrese la opción deseada: "))
        while sel <1 and sel >2:
            sel = int(input("Opcion incorrecta, intente nuevemante: "))
        lim = int(input("\nIngrese limite de filtrado: "))
        if sel == 1:
            filtrados = list(filter(lambda x: x[1]["stock"] > lim,productos_dict.items()))
            print(f"\n--- Productos con stock mayor a {lim} ---")
        else:
            filtrados = list(filter(lambda x: x[1]["stock"] < lim,productos_dict.items()))
            print(f"\n--- Productos con stock menor a {lim} ---")
        print(f"{"ID":<6}{"PRODUCTO":<20}{"PRECIO":<12}{"STOCK":<12}{"CATEGORIA":<20}{"PROVEEDOR":<30}{"ACTIVO"}")
        print("-" * 100)
        for id, datos in filtrados:
            print(f"{id:<6}{datos["nombre"]:<20}${datos["precio"]:<11}{datos["stock"]:<12}{datos["categoria"]:<20}{datos["proveedor"]:<30}{datos["activo"]:^6}")

    if opcion == 4:
        sel = int(input("\n1. Productos con precio MAYOR a X\n2. Productos con precio MENOR a X\nIngrese la opción deseada: "))
        while sel <1 and sel >2:
            sel = int(input("Opcion incorrecta, intente nuevemante: "))
        lim = int(input("\nIngrese limite de filtrado: "))
        if sel == 1:
            filtrados = list(filter(lambda x: x[1]["precio"] > lim,productos_dict.items()))
            print(f"\n--- Productos con precio mayor a {lim} ---")
        else:
            filtrados = list(filter(lambda x: x[1]["precio"] < lim,productos_dict.items()))
            print(f"\n--- Productos con precio menor a {lim} ---")
        print(f"{"ID":<6}{"PRODUCTO":<20}{"PRECIO":<12}{"STOCK":<12}{"CATEGORIA":<20}{"PROVEEDOR":<30}{"ACTIVO"}")
        print("-" * 100)
        for id, datos in filtrados:
            print(f"{id:<6}{datos["nombre"]:<20}${datos["precio"]:<11}{datos["stock"]:<12}{datos["categoria"]:<20}{datos["proveedor"]:<30}{datos["activo"]:^6}")
    
    if opcion == 0:
        print("\nRegresa al menu anterior\n")
    
    else:
        print("Opcion incorrecta, Intente nuevamente\n")

# FUNCIONES PARA FACTURA

def imprimir_encabezado(empresa):
    if len(facturas_dict) == 0:
        nro_factura = 1
    else:   
        nro_factura= max(facturas_dict.keys()) + 1
    # Armado de datos
    linea = "="*80
    razon_social = empresa[0].title()
    cuit = empresa[1]
    cuit_texto = f'CUIT {cuit[:2]}-{cuit[2:10]}-{cuit[len(cuit)-1:]}'
    domicilio = empresa[2]
    localidad = empresa[3].upper()
    domicilio_completo = f'Domicilio fiscal: {domicilio}, {localidad}'
    factura_completo = f'Factura B N° 0002-{str(nro_factura).zfill(8)}'
    periodo = f'Periodo: {str(empresa[4])}-{str(empresa[5]).zfill(2)}'
    web = f'Web: {empresa[6].lower()}'
    soporte = f'Soporte: {empresa[7]}'
    
    # Impresión
    print(linea)
    print(factura_completo.rjust(80))
    print()
    print(razon_social.ljust(39), cuit_texto.rjust(40))
    print(domicilio_completo)
    print(web)
    print(soporte.ljust(39), periodo.rjust(40))
    print(linea)
    return nro_factura

def agregar_producto():
    opcion = ""
    lineas_fact = [] # Se crea la lista que va a almacenar todas las lineas de la factura
    while opcion != "NO": #Se agregan todos los productos
        imprimir_productos()
        sel = int(input("Ingrese el ID del producto a vender: "))
        while sel not in productos_dict:
            sel = int(input("\nID no existe. Ingreselo nuevamente: "))
        p = productos_dict[sel]
        cant = int(input("\nIngrese la cantidad de productos vendidos: "))
        while cant <1 or cant > p["stock"]:
            cant = int(input("\nLa cantidad ingresada no es válida o supera el stock actual. \nIntente nuevamente: "))
        subtotal = p["precio"]*cant
        lin_fact = (sel,p["nombre"],p["precio"],cant,subtotal)
        p["stock"] -= cant #Se resta la cantidad vendida al stock
        lineas_fact.append(lin_fact) #Se agrega el producto a las lineas de esta factura para su posterior impresion
        opcion = input("\nProducto añadido correctamente.\nDesea agregar otro producto? (SI/NO): ").upper()
        while opcion != "SI" and opcion != "NO":
            opcion = input("Opcion incorrecta. Ingrese SI o NO: ").upper()
        if opcion == "SI":
            print("\n--- AGREGAR NUEVO PRODUCTO ---\n")
    return lineas_fact

def mostrar_productos(lineas_fact, encabezados):

    ancho_total = 80
    print(f'{encabezados[0]:<8}{encabezados[1]:<40}{encabezados[2]}{encabezados[3]:>8}{encabezados[4]:>12}')
    print("-" * ancho_total)

    for producto in lineas_fact:
        # Descripción recortada si excede el ancho
        desc = producto[1]
        if len(desc) > 39:
            desc = desc[:36] + "..."
        print(f'{producto[0]:<8}{desc:<40}{producto[2]:>12.2f}{producto[3]:>8}{producto[4]:>12.2f}')
    print("-" * ancho_total)

def mostrar_totales(matriz_productos):
    
    ancho_total = 80
    
    # Calcular total general
    total_general = 0
    for producto in matriz_productos:
        total_general += producto[4]

    # Impresión alineada a la derecha
    print(f'{"TOTAL:":>68}{total_general:>12.2f}')
    print("=" * ancho_total)
    return total_general

#FIN FUNCIONES PARA FACTURA

def cargar_venta():
    """"""
    nueva_fact = agregar_producto() #Va a seleccionar todos los productos a vender y los guarda en la lista nueva_fact
    id_cant = {l[0]:l[3] for l in nueva_fact}
    n_fac= imprimir_encabezado(empresa) #Imprime el encabezado y guarda el nro de factura
    mostrar_productos(nueva_fact,encabezados_detalle) #Muestra el detalle de los productos seleccionados antes
    total = mostrar_totales(nueva_fact) #Muestra el total de la factura y almacena el valor
    print (f"\nFactura {n_fac} impresa y emitida con éxito. Todos los stocks han sido actualizados.\n")
    #UNA VEZ IMPRESA LA FACTURA GUARDA LA INFO EN EL DICCIONARIO DE VENTAS
    facturas_dict[n_fac] = {
        "items": id_cant,
        "total": total
    }

def reporte_ventas():
    """FUNCION DE REPORTE DE VENTAS, LE SIRVE AL ADMINISTRADOR"""
    print("\n"+"="*80)
    print(f"{'REPORTE DE VENTAS':^80}")
    print("="*80)
    total_gral = 0
    ventas = 0
    total_items = 0
    prod_unicos = set () #El "set" es para no duplicar ids de productos y saber efectivamente los productos unicos que se vendieron
    for id_f, datos in facturas_dict.items():
        total_gral += datos["total"]
        ventas += 1
        for id_p, cant in datos["items"].items():
            total_items += cant
            prod_unicos.add(id_p)
    prod = len(prod_unicos) #Devuelve la cantidad de productos diferentes vendidos
    if ventas > 0:

        rendimiento_x_prod ={} #DICCIONARIO TEMPORAL PARA ALMACENAR LAS VENTAS POR ID
        unidades_x_prod = {} #DICCIONARIO TEMPORAL PARA ALMACENAR LAS UNIDADES VENDIDAS POR ID
        for f in facturas_dict.values():
            for id, cant in f["items"].items():
                vtas = productos_dict[id]["precio"] #Busca el precio en el diccionario de productos usando el id de producto guardado
                subtotal = vtas * cant

                if id in rendimiento_x_prod: #SI EL ID YA EXISTE EN EL DICCIONARIO POR UNA VENTA ANTERIOR, SUMA EL TOTAL VENDIDO
                    rendimiento_x_prod[id] += subtotal
                    unidades_x_prod[id] += cant
                else: #SINO LO GUARDA
                    rendimiento_x_prod[id] = subtotal
                    unidades_x_prod[id] = cant
        ranking_plata = sorted(rendimiento_x_prod.items(), key=lambda x: x[1], reverse=True) #ORDENAMOS POR TOTAL DE VENTA DE MAYOR A MENOR TODAS LAS VENTAS
        top_5_plata = ranking_plata[:5] #ME QUEDO CON LOS PRIMEROS 5
        ranking_unidades = sorted(unidades_x_prod.items(), key=lambda x: x[1], reverse=True)
        top_5_unidades = ranking_unidades[:5]

        print(f"\n{'Reporte financiero':^80}")
        print("-"*50)
        print(f"\nEl total facturado fue de ${total_gral}.\nSe realizaron en total {ventas} ventas.\nLo que arroja un promedio por venta de ${total_gral/ventas:.2f}.\n")
        print("="*50)
        print("Top 5 de productos con más rendimiento")
        print("="*50)
        print(f"{'Puesto':<8}{'Producto':<25}{'Total ($)':>15}")
        print("-"*50)
        puesto = 1 #INICIO LA VARIABLE PUESTO
        for id, total in top_5_plata:
            nombre = productos_dict[id]["nombre"] #TRAIGO EL NOMBRE DEL PRODUCTO CORRESPONDIENTE CON EL ID
            print(f"{puesto:<8}{nombre[:24]:<25}{total:>15,.2f}") #IMPRIMO LA LINEA
            puesto += 1 #INCREMENTO EL PUESTO
        print(f"\n{'Reporte cuantitativo':^80}")
        print("-"*80)
        print(f"\nSe vendieron en total {total_items} items, correspondientes a {prod} productos diferentes.\nEl promedio de items por factura es de {total_items/ventas:.2f}")
        print("="*50)
        print("Top 5 de productos con más vendidos")
        print("="*50)
        print(f"{'Puesto':<8}{'Producto':<25}{'Total (U)':>15}")
        print("-"*50)
        puesto = 1 #INICIO LA VARIABLE PUESTO
        for id, total in top_5_unidades:
            nombre = productos_dict[id]["nombre"] #TRAIGO EL NOMBRE DEL PRODUCTO CORRESPONDIENTE CON EL ID
            print(f"{puesto:<8}{nombre[:24]:<25}{total:>15}") #IMPRIMO LA LINEA
            puesto += 1 #INCREMENTO EL PUESTO
    else:
        print("\nAun no se registran ventas\n")

def menu_user():
    """MENU CON ACCESO PARCIAL AL PROGRAMA (interfaz)"""
    print("="*80)
    print(f"{'Menu del Sistema':^80}")
    print("="*80)
    print("1. Realizar venta de producto") 
    print("2. Buscar producto, proveedor o categoria") 
    print("0. Salir")

def menu_admin():
    """MENU CON ACCESO COMPLETO AL PROGRAMA (interfaz)"""
    print("="*80)
    print(f"{'Menu del Sistema':^80}")
    print("="*80)
    print("1. Cargar nuevo producto en el inventario") # OK
    print("2. Buscar producto, proveedor o categoria") # OK
    print("3. Modificar producto o proveedor") # OK
    print("4. Eliminar producto") # OK
    print("5. Realizar venta de producto") 
    print("6. Estadisticas") # OK, FALTA REPORTE DE VENTAS
    print("0. Salir")

def main(login_account):
    """FUNCION QUE DETERMINA EL NIVEL DE ACCESO AL PROGRAMA, USUARIO O ADMIN"""
    login = 0
    print("\n" + "=" * 30)
    print("         LOG IN")
    print("=" * 30)
    print("  1. Usuario")
    print("  2. Administrador")
    print("-" * 30)
    
    opcion = int(input("  Ingrese opcion: "))
    while opcion <= 0 or opcion > 2:
        print("\n  [!] Opcion invalida. Vuelva a intentarlo")
        opcion = int(input("  Ingrese opcion: "))
    
    if opcion == 1:
        while opcion != "0":
            menu_user() # Muestra menu de admin
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                cargar_venta()
            elif opcion == "2":
                buscar_producto()
            elif opcion == "0":
                print("\nPrograma Finalizado correctamente. Muchas gracias")
            else:
                print("\nOpción no válida. Intente de nuevo.")
    else:
        while login != 1:
            print("\n" + "=" * 30)
            print("      ACCESO ADMINISTRADOR")
            print("=" * 30)
            user = input(" Ingrese usuario: ").strip()
            if user in login_account:
                clave = input("  Ingrese clave: ").strip()
                while login != 1:
                    if login_account[user] == clave:
                        print("\n" + "=" * 20)
                        print(f"\nBienvenido {user}")
                        print("\n" + "=" * 20+"\n")
                        login = 1
                        while opcion != "0":
                            menu_admin() # Muestra menu de admin
                            opcion = input("Seleccione una opción: ")

                            if opcion == "1":
                                carga_producto()
                            elif opcion == "2":
                                buscar_producto()
                            elif opcion == "3":
                                modificar_producto()
                            elif opcion == "4":
                                eliminar_producto()
                            elif opcion == "5":
                                cargar_venta()
                            elif opcion == "6":
                                estadisticas()
                            elif opcion == "0":
                                print("\nPrograma Finalizado correctamente. Muchas gracias")
                            else:
                                print("\nOpción no válida. Intente de nuevo.")
                    else:
                        print("\nContraseña incorrecta, Intente nuevamente.")
                        clave = input("  Ingrese clave: ").strip()
            else:
                print("\nUsuario invalido. Intente nuevamente.")

opcion = "" #Inicializa la variable del menú vacía
main(login_account)