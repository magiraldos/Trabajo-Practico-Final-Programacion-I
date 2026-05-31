import re
import menus
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
        menus.submenu_busqueda_productos()
        opcion = int(input("Ingrese opcion: "))
        while opcion < 0 and opcion > 5:
            print("Opcion invalida, vuelva a intentarlo")
            menus.submenu_busqueda_productos()
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