import re
import menus
import json
#========================================
# HELPERS INTERNOS
#========================================
 
def _imprimir_productos(productos):
    """Imprime todos los productos en formato tabla"""
    print(f"{'ID':<6}{'PRODUCTO':<22}{'PRECIO':<12}{'STOCK':<10}{'CATEGORIA':<18}{'PROVEEDOR':<28}{'ACTIVO'}")
    print("-" * 100)
    for p in productos:
        print(f"{p['id']:<6}{p['producto']:<22}${p['precio']:<11}{p['stock']:<10}{p['categoria']:<18}{p['proveedor']:<28}{p['activo']:^6}")
 
def _imprimir_producto_resaltado(productos, id_sel):
    """Imprime todos los productos resaltando el que tiene el id indicado"""
    print(f"{'ID':<6}{'PRODUCTO':<22}{'PRECIO':<12}{'STOCK':<10}{'CATEGORIA':<18}{'PROVEEDOR':<28}{'ACTIVO'}")
    print("-" * 100)
    for p in productos:
        linea = f"{p['id']:<6}{p['producto']:<22}${p['precio']:<11}{p['stock']:<10}{p['categoria']:<18}{p['proveedor']:<28}{p['activo']:^6}"
        if p["id"] == id_sel:
            print(f"\033[41;37m{linea}\033[0m")
        else:
            print(linea)
 
def _buscar_por_id(lista, id_buscado, indice=0):
    # Caso base
    if indice >= len(lista):
        return None

    if lista[indice]["id"] == id_buscado:
        return lista[indice]

    # Caso recursivo
    return _buscar_por_id(lista, id_buscado, indice + 1)
 
def _max_id(lista):
    """Devuelve el id mas alto de una lista de diccionarios"""
    if not lista:
        return 0
    return max(item["id"] for item in lista)
 
 
#========================================
# CRUD - PRODUCTOS
#========================================
 
def cargar_nuevo_producto(productos, categorias, proveedores):
    """Agrega un nuevo producto al sistema"""
    nombre = input("Ingrese nombre del nuevo producto: ").upper()
 
    # Buscar coincidencias antes de cargar
    coincidencias = [p for p in productos if re.search(nombre, p["producto"])]
    if coincidencias:
        print(f"\nSe encontraron productos similares a '{nombre}':")
        print(f"{'ID':<4}| {'PRODUCTO':<20}")
        print("-" * 26)
        for p in coincidencias:
            print(f"{p['id']:<4}| {p['producto']:<20}")
    else:
        print("\nNo se encontraron coincidencias\n")
 
    while True:
        try:
            eleccion = input("\n¿Desea cargar nuevo producto (Y / N)? ").upper()
            while eleccion not in ("Y", "N"):
                print("Opcion invalida, vuelva a intentar")
                eleccion = input("Ingrese Y o N: ").upper()
 
            if eleccion == "Y":
                nuevo_id = _max_id(productos) + 1
                print("\nCARGA DE PRODUCTO NUEVO")
                nombre = input("Ingrese nombre del producto: ").upper()
 
                precio = int(input("Ingrese el precio: "))
                while precio <= 0:
                    print("Error, el precio debe ser mayor a 0")
                    precio = int(input("Ingrese precio: "))
 
                stock = int(input("Ingrese el stock inicial: "))
                while stock < 0:
                    print("Error, el stock debe ser mayor o igual a 0")
                    stock = int(input("Ingrese stock: "))
 
                # --- Seleccion de categoria ---
                print("\n--- CATEGORIA ---")
                print("Categorias existentes:")
                print("=" * 26)
                print(f"{'ID':<4}| {'CATEGORIA':<20}")
                print("-" * 26)
                for cat in categorias:
                    print(f"{cat['id']:<4}| {cat['categoria']:<20}")
                sel = int(input("Ingrese el ID de la categoria deseada (0 para nueva): "))
                max_id_cat = _max_id(categorias)
                while sel < 0 or sel > max_id_cat:
                    sel = int(input("SELECCION INCORRECTA, INTENTE NUEVAMENTE: "))
                if sel != 0:
                    cat_encontrada = _buscar_por_id(categorias, sel)
                    categoria = cat_encontrada["categoria"]
                else:
                    categoria = cargar_nueva_categoria(categorias)
 
                # --- Seleccion de proveedor ---
                print("\n--- PROVEEDOR ---")
                print("Proveedores existentes:")
                print("=" * 26)
                print(f"{'ID':<4}| {'PROVEEDOR':<20}")
                print("-" * 26)
                for prov in proveedores:
                    print(f"{prov['id']:<4}| {prov['proveedor']:<20}")
                sel = int(input("Ingrese el ID del proveedor deseado (0 para nuevo): "))
                max_id_prov = _max_id(proveedores)
                while sel < 0 or sel > max_id_prov:
                    sel = int(input("SELECCION INCORRECTA, INTENTE NUEVAMENTE: "))
                if sel != 0:
                    prov_encontrado = _buscar_por_id(proveedores, sel)
                    proveedor = prov_encontrado["proveedor"]
                else:
                    proveedor = cargar_nuevo_proveedor(proveedores)
 
                # --- Confirmacion ---
                print(f"\n{'PRODUCTO':<22}{'PRECIO':<12}{'STOCK':<10}{'CATEGORIA':<18}{'PROVEEDOR':<28}{'ACTIVO'}")
                print("-" * 95)
                print(f"{nombre:<22}${precio:<11}{stock:<10}{categoria:<18}{proveedor:<28}{'Y':^6}")
                confirmar = input(f"\n¿Confirma la carga de {nombre}? (Y / N): ").upper()
                while confirmar not in ("Y", "N"):
                    print("Opcion invalida, vuelva a intentarlo")
                    confirmar = input(f"¿Confirma la carga de {nombre}? (Y / N): ").upper()
 
                if confirmar == "Y":
                    nuevo_producto = {
                        "id": nuevo_id,
                        "producto": nombre,
                        "precio": precio,
                        "stock": stock,
                        "categoria": categoria,
                        "proveedor": proveedor,
                        "activo": "Y"
                    }
                    productos.append(nuevo_producto)
                    print(f"\nProducto '{nombre}' cargado con exito con ID {nuevo_id}.")
                else:
                    print(f"Carga del producto '{nombre}' cancelada.")
            break
        except ValueError:
            print("Valor no valido, vuelva a intentar")
 
def buscar_producto(productos, categorias, proveedores):
    """Submenu para buscar productos, proveedores o categorias"""
    opcion = 100
    while opcion != 0:
        try:
            menus.submenu_busqueda_productos()
            opcion = int(input("Ingrese opcion: "))
            while opcion < 0 or opcion > 5:
                print("Opcion invalida, vuelva a intentarlo")
                menus.submenu_busqueda_productos()
                opcion = int(input("Ingrese opcion: "))
 
            if opcion == 1:
                # Busqueda por coincidencia de texto
                nombre = input("Ingrese nombre del producto a buscar: ").upper()
                coincidencias = [p for p in productos if re.search(nombre, p["producto"])]
                if coincidencias:
                    print(f"\nSe encontraron {len(coincidencias)} resultado(s) para '{nombre}':")
                    _imprimir_productos(coincidencias)
                    sel = int(input("\nIngrese el ID del producto a ver en detalle (0 para volver): "))
                    if sel != 0:
                        prod = _buscar_por_id(productos, sel)
                        if prod:
                            print("\n---- PRODUCTO EN DETALLE ----")
                            _imprimir_producto_resaltado(productos, sel)
                else:
                    print("\nNo se encontraron resultados para la busqueda\n")
 
            elif opcion == 2:
                # Busqueda por rango de precios
                try:
                    precio_min = int(input("Ingrese precio MINIMO: "))
                    precio_max = int(input("Ingrese precio MAXIMO: "))
                    filtrados = [p for p in productos if precio_min <= p["precio"] <= precio_max]
                    if filtrados:
                        print(f"\n--- Productos entre ${precio_min} y ${precio_max} ---")
                        _imprimir_productos(filtrados)
                    else:
                        print("\nNo se encontraron productos en ese rango de precios\n")
                except ValueError:
                    print("Valor invalido, ingrese numeros enteros")
 
            elif opcion == 3:
                # Busqueda por estado (activo / inactivo)
                estado = input("Ingrese estado a filtrar (Y = activo / N = inactivo): ").upper()
                while estado not in ("Y", "N"):
                    estado = input("Opcion invalida. Ingrese Y o N: ").upper()
                filtrados = [p for p in productos if p["activo"] == estado]
                etiqueta = "ACTIVOS" if estado == "Y" else "INACTIVOS"
                if filtrados:
                    print(f"\n--- Productos {etiqueta} ---")
                    _imprimir_productos(filtrados)
                else:
                    print(f"\nNo se encontraron productos {etiqueta}\n")
 
            elif opcion == 4:
                # Productos sin categoria (categoria = SINCATEGORIA)
                filtrados = [p for p in productos if p["categoria"] == "SINCATEGORIA"]
                if filtrados:
                    print("\n--- Productos sin categoria ---")
                    _imprimir_productos(filtrados)
                else:
                    print("\nTodos los productos tienen categoria asignada\n")
 
            elif opcion == 5:
                # Productos sin proveedor (proveedor = SINPROVEEDOR)
                filtrados = [p for p in productos if p["proveedor"] == "SINPROVEEDOR"]
                if filtrados:
                    print("\n--- Productos sin proveedor ---")
                    _imprimir_productos(filtrados)
                else:
                    print("\nTodos los productos tienen proveedor asignado\n")
 
            elif opcion == 0:
                print("Volviendo al menu anterior...")
 
        except ValueError:
            print("ERROR, opcion invalida")
 
 
def modificar_producto(productos, categorias, proveedores):
    """Submenu para modificar un producto existente"""
    opcion = 100
    while opcion != 0:
        try:
            menus.submenu_modificar_productos()
            opcion = int(input("Ingrese opcion: "))
            while opcion < 0 or opcion > 6:
                print("Opcion invalida, vuelva a intentarlo")
                menus.submenu_modificar_productos()
                opcion = int(input("Ingrese opcion: "))
 
            if opcion == 0:
                print("Volviendo al menu anterior...")
                break
 
            # Buscar el producto a modificar
            nombre = input("Ingrese nombre del producto a modificar: ").upper()
            coincidencias = [p for p in productos if re.search(nombre, p["producto"])]
            if not coincidencias:
                print("\nNo se encontraron productos con ese nombre\n")
                continue
 
            print(f"\nSe encontraron {len(coincidencias)} resultado(s):")
            _imprimir_productos(coincidencias)
            sel = int(input("\nIngrese el ID del producto a modificar: "))
            prod = _buscar_por_id(productos, sel)
            if not prod:
                print("ID no encontrado")
                continue
 
            if opcion == 1:
                # Modificar nombre
                nuevo_nombre = input(f"Nombre actual: '{prod['producto']}'. Ingrese nuevo nombre: ").upper()
                confirmar = input(f"¿Confirma cambiar nombre a '{nuevo_nombre}'? (Y / N): ").upper()
                if confirmar == "Y":
                    prod["producto"] = nuevo_nombre
                    print("Nombre actualizado con exito")
                    _imprimir_producto_resaltado(productos, sel)
 
            elif opcion == 2:
                # Modificar precio
                try:
                    nuevo_precio = int(input(f"Precio actual: ${prod['precio']}. Ingrese nuevo precio: "))
                    while nuevo_precio <= 0:
                        print("El precio debe ser mayor a 0")
                        nuevo_precio = int(input("Ingrese nuevo precio: "))
                    confirmar = input(f"¿Confirma cambiar precio a ${nuevo_precio}? (Y / N): ").upper()
                    if confirmar == "Y":
                        prod["precio"] = nuevo_precio
                        print("Precio actualizado con exito")
                        _imprimir_producto_resaltado(productos, sel)
                except ValueError:
                    print("Valor invalido, ingrese un numero entero")
 
            elif opcion == 3:
                # Modificar stock
                try:
                    print(f"Stock actual: {prod['stock']}.")
                    print("1. Aumentar stock")
                    print("2. Disminuir stock")
                    sub = int(input("Ingrese opcion: "))
                    if sub == 1:
                        cantidad = int(input("Ingrese unidades a agregar: "))
                        nuevo_stock = prod["stock"] + cantidad
                    elif sub == 2:
                        cantidad = int(input("Ingrese unidades a restar: "))
                        if cantidad > prod["stock"]:
                            print(f"La cantidad supera el stock actual. Se reducira a 0.")
                            cantidad = prod["stock"]
                        nuevo_stock = prod["stock"] - cantidad
                    else:
                        print("Opcion invalida")
                        continue
                    confirmar = input(f"¿Confirma nuevo stock de {nuevo_stock}? (Y / N): ").upper()
                    if confirmar == "Y":
                        prod["stock"] = nuevo_stock
                        print("Stock actualizado con exito")
                        _imprimir_producto_resaltado(productos, sel)
                except ValueError:
                    print("Valor invalido")
 
            elif opcion == 4:
                # Modificar categoria
                nueva_cat = modificar_categoria(categorias)
                confirmar = input(f"¿Confirma cambiar categoria a '{nueva_cat}'? (Y / N): ").upper()
                if confirmar == "Y":
                    prod["categoria"] = nueva_cat
                    print("Categoria actualizada con exito")
                    _imprimir_producto_resaltado(productos, sel)
 
            elif opcion == 5:
                # Modificar proveedor
                print("Proveedores existentes:")
                print(f"{'ID':<4}| {'PROVEEDOR':<25}| {'TELEFONO':<15}")
                print("-" * 48)
                for prov in proveedores:
                    print(f"{prov['id']:<4}| {prov['proveedor']:<25}| {prov['telefono']:<15}")
                sel_prov = int(input("Ingrese el ID del nuevo proveedor (0 para cargar nuevo): "))
                max_id_prov = _max_id(proveedores)
                while sel_prov < 0 or sel_prov > max_id_prov:
                    sel_prov = int(input("SELECCION INCORRECTA, INTENTE NUEVAMENTE: "))
                if sel_prov != 0:
                    prov_encontrado = _buscar_por_id(proveedores, sel_prov)
                    nuevo_prov = prov_encontrado["proveedor"]
                else:
                    nuevo_prov = cargar_nuevo_proveedor(proveedores)
                confirmar = input(f"¿Confirma cambiar proveedor a '{nuevo_prov}'? (Y / N): ").upper()
                if confirmar == "Y":
                    prod["proveedor"] = nuevo_prov
                    print("Proveedor actualizado con exito")
                    _imprimir_producto_resaltado(productos, sel)
 
            elif opcion == 6:
                # Modificar estado (activo / inactivo)
                estado_actual = prod["activo"]
                nuevo_estado = "N" if estado_actual == "Y" else "Y"
                etiqueta = "INACTIVO" if nuevo_estado == "N" else "ACTIVO"
                confirmar = input(f"El producto pasara a estado {etiqueta}. ¿Confirma? (Y / N): ").upper()
                if confirmar == "Y":
                    prod["activo"] = nuevo_estado
                    print(f"Estado actualizado a {etiqueta}")
                    _imprimir_producto_resaltado(productos, sel)
 
        except ValueError:
            print("Valor no valido, vuelva a intentar")
 
 
def eliminar_producto(productos):
    """Baja logica de un producto (activo = N). Si tiene stock, ofrece reducirlo a 0."""
    _imprimir_productos(productos)
    try:
        sel = int(input("\nIngrese el ID del producto a dar de baja: "))
        prod = _buscar_por_id(productos, sel)
        if not prod:
            print("ID no encontrado")
            return
 
        nombre = prod["producto"]
        stock  = prod["stock"]
 
        confirmar = input(f"\n¿Confirma la baja del producto '{nombre}'? (Y / N): ").upper()
        while confirmar not in ("Y", "N"):
            confirmar = input("Responda Y o N: ").upper()
 
        if confirmar == "Y":
            if stock > 0:
                reducir = input(f"El producto tiene stock actual de {stock}. ¿Desea reducirlo a 0? (Y / N): ").upper()
                while reducir not in ("Y", "N"):
                    reducir = input("Responda Y o N: ").upper()
                if reducir == "Y":
                    prod["stock"] = 0
            prod["activo"] = "N"
            print(f"\nEl producto '{nombre}' fue dado de baja correctamente.")
            _imprimir_producto_resaltado(productos, sel)
        else:
            print("\nOperacion cancelada con exito")
    except ValueError:
        print("ID invalido")
 
 
#========================================
# CRUD - CATEGORIAS
#========================================
 
def cargar_nueva_categoria(categorias):
    """Agrega una nueva categoria al sistema y la retorna"""
    nombre = input("Ingrese nombre de la categoria para buscar coincidencias: ").upper()
    coincidencias = [c for c in categorias if re.search(nombre, c["categoria"])]
    if coincidencias:
        print(f"\nSe encontraron categorias similares a '{nombre}':")
        print(f"{'ID':<4}| {'CATEGORIA':<20}")
        print("-" * 26)
        for c in coincidencias:
            print(f"{c['id']:<4}| {c['categoria']:<20}")
    else:
        print("\nNo se encontraron coincidencias\n")
 
    categoria = input("Ingrese nombre de la nueva categoria (0 para cancelar): ").upper()
    # Verificar que no exista ya
    nombres_existentes = [c["categoria"] for c in categorias]
    while categoria in nombres_existentes and categoria != "0":
        print(f"ERROR, la categoria '{categoria}' ya existe")
        categoria = input("Ingrese la nueva categoria (0 para cancelar): ").upper()
    if categoria != "0":
        nuevo_id = _max_id(categorias) + 1
        nueva_categoria = {"id": nuevo_id, "categoria": categoria}
        categorias.append(nueva_categoria)
        print(f"Categoria '{categoria}' cargada con exito con ID {nuevo_id}")
    else:
        print("Carga cancelada. Se asignara SINCATEGORIA")
        categoria = "SINCATEGORIA"
    return categoria
 
 
def buscar_categoria(productos, categorias):
    """Busca categorias por nombre y muestra los productos que contiene"""
    opcion = 100
    while opcion != 0:
        try:
            menus.submenu_busqueda_categorias()
            opcion = int(input("Ingrese opcion: "))
            while opcion < 0 or opcion > 2:
                print("Opcion invalida")
                opcion = int(input("Ingrese opcion: "))
 
            if opcion == 1:
                # Busqueda por texto
                nombre = input("Ingrese nombre de la categoria a buscar: ").upper()
                coincidencias = [c for c in categorias if re.search(nombre, c["categoria"])]
                if coincidencias:
                    print(f"\nSe encontraron {len(coincidencias)} resultado(s):")
                    print(f"{'ID':<4}| {'CATEGORIA':<20}")
                    print("-" * 26)
                    for c in coincidencias:
                        print(f"{c['id']:<4}| {c['categoria']:<20}")
                    sel = int(input("\nIngrese el ID para ver los productos de esa categoria (0 para volver): "))
                    if sel != 0:
                        cat = _buscar_por_id(categorias, sel)
                        if cat:
                            prods_cat = [p for p in productos if p["categoria"] == cat["categoria"]]
                            print(f"\n--- Productos en categoria '{cat['categoria']}' ---")
                            if prods_cat:
                                _imprimir_productos(prods_cat)
                            else:
                                print("Esta categoria no tiene productos asignados")
                else:
                    print("\nNo se encontraron categorias con ese nombre\n")
 
            elif opcion == 2:
                # Categorias ordenadas por volumen de productos
                conteo = []
                for cat in categorias:
                    cantidad = sum(1 for p in productos if p["categoria"] == cat["categoria"])
                    conteo.append((cat["id"], cat["categoria"], cantidad))
                conteo.sort(key=lambda x: x[2], reverse=True)
                print(f"\n--- Categorias por volumen de productos ---")
                print(f"{'ID':<4}| {'CATEGORIA':<20}| {'PRODUCTOS':>10}")
                print("-" * 40)
                for id_c, nombre_c, cant in conteo:
                    print(f"{id_c:<4}| {nombre_c:<20}| {cant:>10}")
 
            elif opcion == 0:
                print("Volviendo al menu anterior...")
 
        except ValueError:
            print("ERROR, opcion invalida")
 
 
def modificar_categoria(categorias):
    """Muestra categorias existentes y permite seleccionar/asignar una, o crear una nueva. Retorna el nombre."""
    print("\n--- CATEGORIA ---")
    print("Categorias existentes:")
    print("=" * 26)
    print(f"{'ID':<4}| {'CATEGORIA':<20}")
    print("-" * 26)
    for cat in categorias:
        print(f"{cat['id']:<4}| {cat['categoria']:<20}")
    try:
        sel = int(input("Ingrese el ID de la categoria deseada (0 para cargar nueva): "))
        max_id_cat = _max_id(categorias)
        while sel < 0 or sel > max_id_cat:
            sel = int(input("SELECCION INCORRECTA, INTENTE NUEVAMENTE: "))
        if sel != 0:
            cat = _buscar_por_id(categorias, sel)
            return cat["categoria"]
        else:
            return cargar_nueva_categoria(categorias)
    except ValueError:
        print("Valor invalido")
        return "SINCATEGORIA"
 
 
def eliminar_categoria(productos, categorias):
    """Elimina una categoria. Los productos asociados pasan a SINCATEGORIA."""
    print(f"{'ID':<4}| {'CATEGORIA':<20}")
    print("-" * 26)
    for cat in categorias:
        print(f"{cat['id']:<4}| {cat['categoria']:<20}")
    try:
        sel = int(input("\nIngrese el ID de la categoria a eliminar: "))
        cat = _buscar_por_id(categorias, sel)
        if not cat:
            print("ID no encontrado")
            return
 
        nombre_cat = cat["categoria"]
        afectados = [p for p in productos if p["categoria"] == nombre_cat]
        if afectados:
            print(f"\nAtencion: {len(afectados)} producto(s) tienen esta categoria asignada.")
            print("Al eliminarla pasaran a SINCATEGORIA.")
 
        confirmar = input(f"¿Confirma la eliminacion de '{nombre_cat}'? (Y / N): ").upper()
        while confirmar not in ("Y", "N"):
            confirmar = input("Responda Y o N: ").upper()
 
        if confirmar == "Y":
            for p in afectados:
                p["categoria"] = "SINCATEGORIA"
            categorias.remove(cat)
            print(f"Categoria '{nombre_cat}' eliminada. {len(afectados)} producto(s) actualizados a SINCATEGORIA.")
        else:
            print("Operacion cancelada")
    except ValueError:
        print("ID invalido")
 
 
#========================================
# CRUD - PROVEEDORES
#========================================
 
def cargar_nuevo_proveedor(proveedores):
    """Agrega un nuevo proveedor al sistema y lo retorna"""
    nombre = input("Ingrese nombre del proveedor para buscar coincidencias: ").upper()
    coincidencias = [prov for prov in proveedores if re.search(nombre, prov["proveedor"])]
    if coincidencias:
        print(f"\nSe encontraron proveedores similares a '{nombre}':")
        print(f"{'ID':<4}| {'PROVEEDOR':<25}")
        print("-" * 31)
        for prov in coincidencias:
            print(f"{prov['id']:<4}| {prov['proveedor']:<25}")
    else:
        print("\nNo se encontraron coincidencias\n")
 
    proveedor = input("Ingrese nombre del nuevo proveedor (0 para cancelar): ").upper()
    nombres_existentes = [prov["proveedor"] for prov in proveedores]
    while proveedor in nombres_existentes and proveedor != "0":
        print(f"ERROR, el proveedor '{proveedor}' ya existe")
        proveedor = input("Ingrese el nuevo proveedor (0 para cancelar): ").upper()
 
    if proveedor != "0":
        try:
            telefono = input("Ingrese telefono del proveedor (10 digitos, sin guiones): ")
            while len(telefono) != 10 or not telefono.isdigit():
                print("Error, telefono invalido. Debe tener exactamente 10 digitos.")
                telefono = input("Ingrese telefono: ")
            nuevo_id = _max_id(proveedores) + 1
            nuevo_proveedor = {
                "id": nuevo_id,
                "proveedor": proveedor,
                "telefono": telefono
            }
            proveedores.append(nuevo_proveedor)
            print(f"Proveedor '{proveedor}' cargado con exito con ID {nuevo_id}")
        except ValueError:
            print("Valor invalido")
            proveedor = "SINPROVEEDOR"
    else:
        print("Carga cancelada. Se asignara SINPROVEEDOR")
        proveedor = "SINPROVEEDOR"
    return proveedor
 
 
def buscar_proveedor(productos, proveedores):
    """Busca proveedores por nombre y muestra sus datos y productos asociados"""
    opcion = 100
    while opcion != 0:
        try:
            menus.submenu_busqueda_proveedores()
            opcion = int(input("Ingrese opcion: "))
            while opcion < 0 or opcion > 2:
                print("Opcion invalida")
                opcion = int(input("Ingrese opcion: "))
 
            if opcion == 1:
                # Busqueda por texto
                nombre = input("Ingrese nombre del proveedor a buscar: ").upper()
                coincidencias = [prov for prov in proveedores if re.search(nombre, prov["proveedor"])]
                if coincidencias:
                    print(f"\nSe encontraron {len(coincidencias)} resultado(s) para '{nombre}':")
                    print(f"{'ID':<4}| {'PROVEEDOR':<28}| {'TELEFONO':<15}")
                    print("-" * 50)
                    for prov in coincidencias:
                        print(f"{prov['id']:<4}| {prov['proveedor']:<28}| {prov['telefono']:<15}")
                    sel = int(input("\nIngrese el ID para ver los productos de ese proveedor (0 para volver): "))
                    if sel != 0:
                        prov = _buscar_por_id(proveedores, sel)
                        if prov:
                            prods_prov = [p for p in productos if p["proveedor"] == prov["proveedor"]]
                            print(f"\n--- Productos del proveedor '{prov['proveedor']}' ---")
                            if prods_prov:
                                _imprimir_productos(prods_prov)
                            else:
                                print("Este proveedor no tiene productos asignados")
                else:
                    print("\nNo se encontraron proveedores con ese nombre\n")
 
            elif opcion == 2:
                # Listar todos los proveedores
                print(f"\n--- Listado completo de proveedores ---")
                print(f"{'ID':<4}| {'PROVEEDOR':<28}| {'TELEFONO':<15}")
                print("-" * 50)
                for prov in proveedores:
                    print(f"{prov['id']:<4}| {prov['proveedor']:<28}| {prov['telefono']:<15}")
 
            elif opcion == 0:
                print("Volviendo al menu anterior...")
 
        except ValueError:
            print("ERROR, opcion invalida")
 
 
def modificar_proveedor(productos, proveedores):
    """Submenu para modificar nombre o telefono de un proveedor"""
    opcion = 100
    while opcion != 0:
        try:
            menus.submenu_modificar_proveedores()
            opcion = int(input("Ingrese opcion: "))
            while opcion < 0 or opcion > 2:
                print("Opcion invalida")
                opcion = int(input("Ingrese opcion: "))
 
            if opcion == 0:
                print("Volviendo al menu anterior...")
                break
 
            # Buscar el proveedor
            nombre = input("Ingrese nombre del proveedor a modificar: ").upper()
            coincidencias = [prov for prov in proveedores if re.search(nombre, prov["proveedor"])]
            if not coincidencias:
                print("\nNo se encontraron proveedores con ese nombre\n")
                continue
 
            print(f"\nSe encontraron {len(coincidencias)} resultado(s):")
            print(f"{'ID':<4}| {'PROVEEDOR':<28}| {'TELEFONO':<15}")
            print("-" * 50)
            for prov in coincidencias:
                print(f"{prov['id']:<4}| {prov['proveedor']:<28}| {prov['telefono']:<15}")
 
            sel = int(input("\nIngrese el ID del proveedor a modificar: "))
            prov = _buscar_por_id(proveedores, sel)
            if not prov:
                print("ID no encontrado")
                continue
 
            if opcion == 1:
                # Modificar nombre
                nuevo_nombre = input(f"Nombre actual: '{prov['proveedor']}'. Ingrese nuevo nombre: ").upper()
                confirmar = input(f"¿Confirma cambiar nombre a '{nuevo_nombre}'? (Y / N): ").upper()
                if confirmar == "Y":
                    nombre_viejo = prov["proveedor"]
                    prov["proveedor"] = nuevo_nombre
                    # Actualizar el nombre en todos los productos asociados
                    for p in productos:
                        if p["proveedor"] == nombre_viejo:
                            p["proveedor"] = nuevo_nombre
                    print(f"Proveedor renombrado a '{nuevo_nombre}'. Productos actualizados.")
 
            elif opcion == 2:
                # Modificar telefono
                nuevo_tel = input(f"Telefono actual: {prov['telefono']}. Ingrese nuevo telefono (10 digitos): ")
                while len(nuevo_tel) != 10 or not nuevo_tel.isdigit():
                    print("Telefono invalido. Debe tener exactamente 10 digitos.")
                    nuevo_tel = input("Ingrese telefono: ")
                confirmar = input(f"¿Confirma cambiar telefono a {nuevo_tel}? (Y / N): ").upper()
                if confirmar == "Y":
                    prov["telefono"] = nuevo_tel
                    print("Telefono actualizado con exito")
 
        except ValueError:
            print("Valor no valido, vuelva a intentar")
 
 
def eliminar_proveedor(productos, proveedores):
    """Elimina un proveedor. Los productos asociados pasan a SINPROVEEDOR."""
    print(f"{'ID':<4}| {'PROVEEDOR':<28}| {'TELEFONO':<15}")
    print("-" * 50)
    for prov in proveedores:
        print(f"{prov['id']:<4}| {prov['proveedor']:<28}| {prov['telefono']:<15}")
    try:
        sel = int(input("\nIngrese el ID del proveedor a eliminar: "))
        prov = _buscar_por_id(proveedores, sel)
        if not prov:
            print("ID no encontrado")
            return
 
        nombre_prov = prov["proveedor"]
        afectados = [p for p in productos if p["proveedor"] == nombre_prov]
        if afectados:
            print(f"\nAtencion: {len(afectados)} producto(s) tienen este proveedor asignado.")
            print("Al eliminarlo pasaran a SINPROVEEDOR.")
 
        confirmar = input(f"¿Confirma la eliminacion de '{nombre_prov}'? (Y / N): ").upper()
        while confirmar not in ("Y", "N"):
            confirmar = input("Responda Y o N: ").upper()
 
        if confirmar == "Y":
            for p in afectados:
                p["proveedor"] = "SINPROVEEDOR"
            proveedores.remove(prov)
            print(f"Proveedor '{nombre_prov}' eliminado. {len(afectados)} producto(s) actualizados a SINPROVEEDOR.")
        else:
            print("Operacion cancelada")
    except ValueError:
        print("ID invalido")
 