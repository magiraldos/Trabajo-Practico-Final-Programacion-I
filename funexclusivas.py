import json
import crud

# Datos de la empresa para el encabezado de factura
_EMPRESA     = ["Kiosco 'La Puerta Lijada'", "30787654321", "Saraza 6247", "caba", 2026, 4, "WWW.LAPUERTALIJADA.COM", "contacto@lapuertalijada.com"]
_ENC_DETALLE = ["Codigo", "Descripcion", "P. Unitario", "Cant.", "Subtotal"]

# Lista en memoria que acumula las ventas de la sesion
_facturas_sesion = []

#========================================
# ELEMENTOS DE FACTURA
#========================================

def _imprimir_encabezado():
    """Imprime el encabezado de la factura y retorna el numero de factura"""
    nro_factura = max((f["nro"] for f in _facturas_sesion), default=0) + 1
    empresa     = _EMPRESA
    cuit       = empresa[1]
    cuit_texto = f"CUIT {cuit[:2]}-{cuit[2:10]}-{cuit[-1]}"
    print("=" * 80)
    print(f"Factura B N 0002-{str(nro_factura).zfill(8)}".rjust(80))
    print()
    print(empresa[0].title().ljust(39), cuit_texto.rjust(40))
    print(f"Domicilio fiscal: {empresa[2]}, {empresa[3].upper()}")
    print(f"Web: {empresa[6].lower()}")
    print(f"Soporte: {empresa[7]}".ljust(39), f"Periodo: {empresa[4]}-{str(empresa[5]).zfill(2)}".rjust(40))
    print("=" * 80)
    return nro_factura

def _agregar_producto(productos):
    """Permite al usuario seleccionar productos para la factura.
    Retorna lista de tuplas (id, nombre, precio, cant, subtotal)."""
    lineas_fact = []
    continuar   = "SI"
    while continuar == "SI":
        crud._imprimir_productos([p for p in productos if p["activo"] == "Y"])
        try:
            sel = int(input("Ingrese el ID del producto a vender: "))
        except ValueError:
            print("Error: ingrese un numero entero valido")
            continue
        prod = crud._buscar_por_id(productos, sel)
        if not prod or prod["activo"] != "Y":
            print("ID no valido o producto inactivo. Intente nuevamente.")
            continue
        try:
            cant = int(input("\nIngrese la cantidad de productos vendidos: "))
        except ValueError:
            print("Error: ingrese un numero entero valido")
            continue
        if cant < 1 or cant > prod["stock"]:
            print(f"Cantidad invalida o supera el stock actual ({prod['stock']}). Intente nuevamente.")
            continue
        subtotal = prod["precio"] * cant
        prod["stock"] -= cant
        lineas_fact.append((sel, prod["producto"], prod["precio"], cant, subtotal))
        print("\nProducto annadido correctamente.")
        continuar = input("Desea agregar otro producto? (SI / NO): ").strip().upper()
        while continuar not in ("SI", "NO"):
            print("Opcion incorrecta.")
            continuar = input("Ingrese SI o NO: ").strip().upper()
        if continuar == "SI":
            print("\n--- AGREGAR NUEVO PRODUCTO ---\n")
    return lineas_fact

def _mostrar_productos(lineas_fact):
    """Imprime el detalle de la factura"""
    enc = _ENC_DETALLE
    print(f"{enc[0]:<8}{enc[1]:<40}{enc[2]}{enc[3]:>8}{enc[4]:>12}")
    print("-" * 80)
    for prod in lineas_fact:
        desc = prod[1][:36] + "..." if len(prod[1]) > 39 else prod[1]
        print(f"{prod[0]:<8}{desc:<40}{prod[2]:>12.2f}{prod[3]:>8}{prod[4]:>12.2f}")
    print("-" * 80)

def _mostrar_totales(lineas_fact):
    """Imprime el total y lo retorna"""
    total = sum(p[4] for p in lineas_fact)
    print(f"{'TOTAL:':>68}{total:>12.2f}")
    print("=" * 80)
    return total

#========================================
# FUNCION EXCLUSIVA DE VENDEDOR
#========================================

def realizar_venta(productos):
    """Genera una venta: muestra factura por consola y registra en memoria de sesion"""
    print("=" * 80)
    print(f"\033[36m{'Realizar Venta':^80}\033[0m")
    print("=" * 80)
    lineas = _agregar_producto(productos)
    if not lineas:
        print("No se agrego ningun producto. Venta cancelada.")
        return
    id_cant  = {l[0]: l[3] for l in lineas}
    n_fac    = _imprimir_encabezado()
    _mostrar_productos(lineas)
    total    = _mostrar_totales(lineas)
    print(f"\nFactura {n_fac} impresa y emitida con exito. Stocks actualizados.\n")
    _facturas_sesion.append({"nro": n_fac, "items": id_cant, "total": total})

#========================================
# FUNCIONES EXCLUSIVAS DE ADMINISTRADOR
#========================================

def estadisticas(productos):
    """Submenu principal de estadisticas"""
    opcion = 100
    while opcion != 0:
        try:
            print("=" * 80)
            print(f"\033[36m{'Menu de Estadisticas':^80}\033[0m")
            print("=" * 80)
            print("1. Listado de productos")
            print("2. Reporte de ventas")
            print("3. Estadisticas por categoria")
            print("0. Regresar al menu anterior")
            opcion = int(input("Ingrese opcion deseada: "))
            while opcion < 0 or opcion > 3:
                print("Opcion invalida")
                opcion = int(input("Ingrese opcion deseada: "))
            if opcion == 1:
                _listado_de_productos(productos)
            elif opcion == 2:
                _reporte_ventas(productos)
            elif opcion == 3:
                _estadisticas_por_categoria(productos)
        except ValueError:
            print("Error: ingrese un numero valido")


# -----------------------------------------------
# LISTADO DE PRODUCTOS
# -----------------------------------------------

def _listado_de_productos(productos):
    """Submenu para listar y filtrar productos"""
    opcion = 100
    while opcion != 0:
        try:
            print("=" * 80)
            print(f"\033[36m{'Listado de Productos':^80}\033[0m")
            print("=" * 80)
            print("1. Ver todos los productos ordenados")
            print("2. Ver productos filtrados por actividad")
            print("3. Ver productos filtrados por cantidad de stock")
            print("4. Ver productos filtrados por precio")
            print("0. Regresar al menu anterior\n")
            opcion = int(input("Ingrese opcion deseada: "))
            while opcion < 0 or opcion > 4:
                opcion = int(input("Opcion invalida, ingrese nuevamente: "))
            if opcion == 1:
                print("\nComo quiere ordenar los productos?\n1. Por nombre\n2. Por stock\n3. Por precio")
                try:
                    sel = int(input("Seleccione una opcion: "))
                    while sel < 1 or sel > 3:
                        sel = int(input("Opcion invalida, ingrese nuevamente: "))
                    claves = {1: "producto", 2: "stock", 3: "precio"}
                    clave = claves[sel]
                    if sel == 1:
                        asc = int(input("Ingrese 1 para A-Z o 2 para Z-A: "))
                    else:
                        asc = int(input("Ingrese 1 para ascendente o 2 para descendente: "))
                    while asc not in (1, 2):
                        asc = int(input("Opcion invalida, ingrese nuevamente: "))
                    ordenados = sorted(productos, key=lambda p: p[clave], reverse=(asc == 2))
                    crud._imprimir_productos(ordenados)
                except ValueError:
                    print("Error: ingrese un numero valido")
            elif opcion == 2:
                sel = input("Ingrese Y para activos o N para inactivos: ").strip().upper()
                while sel not in ("Y", "N"):
                    sel = input("Opcion invalida, ingrese Y o N: ").strip().upper()
                etiqueta = "ACTIVO" if sel == "Y" else "INACTIVO"
                filtrados = [p for p in productos if p["activo"] == sel]
                print(f"\n--- Productos con status {etiqueta} ---")
                crud._imprimir_productos(filtrados) if filtrados else print("No se encontraron productos")
            elif opcion == 3:
                try:
                    sel = int(input("\n1. Stock MAYOR a X\n2. Stock MENOR a X\nIngrese opcion: "))
                    while sel not in (1, 2):
                        sel = int(input("Opcion incorrecta, intente nuevamente: "))
                    lim = int(input("Ingrese limite: "))
                    if sel == 1:
                        filtrados = [p for p in productos if p["stock"] > lim]
                        print(f"\n--- Productos con stock mayor a {lim} ---")
                    else:
                        filtrados = [p for p in productos if p["stock"] < lim]
                        print(f"\n--- Productos con stock menor a {lim} ---")
                    crud._imprimir_productos(filtrados) if filtrados else print("No se encontraron productos")
                except ValueError:
                    print("Error: ingrese un numero valido")
            elif opcion == 4:
                try:
                    sel = int(input("\n1. Precio MAYOR a X\n2. Precio MENOR a X\nIngrese opcion: "))
                    while sel not in (1, 2):
                        sel = int(input("Opcion incorrecta, intente nuevamente: "))
                    lim = int(input("Ingrese limite: "))
                    if sel == 1:
                        filtrados = [p for p in productos if p["precio"] > lim]
                        print(f"\n--- Productos con precio mayor a ${lim} ---")
                    else:
                        filtrados = [p for p in productos if p["precio"] < lim]
                        print(f"\n--- Productos con precio menor a ${lim} ---")
                    crud._imprimir_productos(filtrados) if filtrados else print("No se encontraron productos")
                except ValueError:
                    print("Error: ingrese un numero valido")
        except ValueError:
            print("Error: ingrese un numero valido")


# -----------------------------------------------
# REPORTE DE VENTAS
# -----------------------------------------------

def _reporte_ventas(productos):
    """Reporte financiero y cuantitativo de las ventas de la sesion"""
    print("\n" + "=" * 80)
    print(f"\033[36m{'REPORTE DE VENTAS':^80}\033[0m")
    print("=" * 80)
    if not _facturas_sesion:
        print("\nAun no se registran ventas en esta sesion\n")
        return
    total_gral         = 0
    ventas             = 0
    total_items        = 0
    prod_unicos        = set()
    rendimiento_x_prod = {}
    unidades_x_prod    = {}
    for f in _facturas_sesion:
        total_gral += f["total"]
        ventas     += 1
        for id_p, cant in f["items"].items():
            total_items += cant
            prod_unicos.add(id_p)
            prod_encontrado = crud._buscar_por_id(productos, id_p)
            precio   = prod_encontrado["precio"] if prod_encontrado else 0
            subtotal = precio * cant
            if id_p in rendimiento_x_prod:
                rendimiento_x_prod[id_p] += subtotal
                unidades_x_prod[id_p]    += cant
            else:
                rendimiento_x_prod[id_p] = subtotal
                unidades_x_prod[id_p]    = cant
    top5_plata    = sorted(rendimiento_x_prod.items(), key=lambda x: x[1], reverse=True)[:5]
    top5_unidades = sorted(unidades_x_prod.items(),    key=lambda x: x[1], reverse=True)[:5]
    min_plata     = min(rendimiento_x_prod.items(),    key=lambda x: x[1])
    min_unidades  = min(unidades_x_prod.items(),       key=lambda x: x[1])
    print(f"\n{'Reporte financiero':^80}")
    print("-" * 50)
    print(f"\nTotal facturado: ${total_gral:,.2f}")
    print(f"Ventas realizadas: {ventas}")
    print(f"Promedio por venta: ${total_gral / ventas:,.2f}\n")
    print("=" * 58)
    print("Top 5 productos con mas rendimiento")
    print("=" * 58)
    print(f"{'Puesto':<8}{'Producto':<25}{'Total ($)':>13}{'% del total':>12}")
    print("-" * 58)
    for puesto, (id_p, total) in enumerate(top5_plata, start=1):
        prod   = crud._buscar_por_id(productos, id_p)
        nombre = prod["producto"][:24] if prod else f"ID {id_p}"
        pct    = (total / total_gral * 100) if total_gral else 0
        print(f"{puesto:<8}{nombre:<25}{total:>13,.2f}{pct:>11.1f}%")
    prod_min   = crud._buscar_por_id(productos, min_plata[0])
    nombre_min = prod_min["producto"] if prod_min else f"ID {min_plata[0]}"
    pct_min    = (min_plata[1] / total_gral * 100) if total_gral else 0
    print(f"\n  Menor rendimiento: {nombre_min} - ${min_plata[1]:,.2f} ({pct_min:.1f}% del total)")
    print(f"\n{'Reporte cuantitativo':^80}")
    print("-" * 80)
    print(f"\nItems vendidos: {total_items}, de {len(prod_unicos)} productos distintos.")
    print(f"Promedio de items por venta: {total_items / ventas:.2f}\n")
    print("=" * 55)
    print("Top 5 productos mas vendidos por unidad")
    print("=" * 55)
    print(f"{'Puesto':<8}{'Producto':<25}{'Unidades':>10}{'% del total':>12}")
    print("-" * 55)
    for puesto, (id_p, cant) in enumerate(top5_unidades, start=1):
        prod   = crud._buscar_por_id(productos, id_p)
        nombre = prod["producto"][:24] if prod else f"ID {id_p}"
        pct    = (cant / total_items * 100) if total_items else 0
        print(f"{puesto:<8}{nombre:<25}{cant:>10}{pct:>11.1f}%")
    prod_min_u   = crud._buscar_por_id(productos, min_unidades[0])
    nombre_min_u = prod_min_u["producto"] if prod_min_u else f"ID {min_unidades[0]}"
    pct_min_u    = (min_unidades[1] / total_items * 100) if total_items else 0
    print(f"\n  Menor volumen: {nombre_min_u} - {min_unidades[1]} unidades ({pct_min_u:.1f}% del total)\n")

# -----------------------------------------------
# ESTADISTICAS POR CATEGORIA
# -----------------------------------------------

def _estadisticas_por_categoria(productos):
    """Facturacion, unidades y porcentajes agrupados por categoria"""
    print("\n" + "=" * 80)
    print(f"\033[36m{'ESTADISTICAS POR CATEGORIA':^80}\033[0m")
    print("=" * 80)
    if not _facturas_sesion:
        print("\nAun no se registran ventas en esta sesion\n")
        return
    facturacion_cat = {}
    unidades_cat    = {}
    for f in _facturas_sesion:
        for id_p, cant in f["items"].items():
            prod = crud._buscar_por_id(productos, id_p)
            if not prod:
                continue
            cat      = prod["categoria"]
            subtotal = prod["precio"] * cant
            facturacion_cat[cat] = facturacion_cat.get(cat, 0) + subtotal
            unidades_cat[cat]    = unidades_cat.get(cat, 0)    + cant
    total_gral  = sum(facturacion_cat.values())
    total_items = sum(unidades_cat.values())
    ranking     = sorted(facturacion_cat.items(), key=lambda x: x[1], reverse=True)
    print(f"\n{'CATEGORIA':<20}{'FACTURACION ($)':>16}{'% FACTURACION':>14}{'UNIDADES':>10}{'% UNIDADES':>12}")
    print("-" * 74)
    for cat, total in ranking:
        pct_f = (total / total_gral * 100)                if total_gral  else 0
        pct_u = (unidades_cat[cat] / total_items * 100)   if total_items else 0
        print(f"{cat:<20}{total:>16,.2f}{pct_f:>13.1f}%{unidades_cat[cat]:>10}{pct_u:>11.1f}%")
    print("-" * 74)
    print(f"{'TOTAL':<20}{total_gral:>16,.2f}{'100.0%':>14}{total_items:>10}{'100.0%':>12}")
    cat_min_f = min(facturacion_cat.items(), key=lambda x: x[1])
    cat_min_u = min(unidades_cat.items(),    key=lambda x: x[1])
    print(f"\n  Categoria con menor facturacion: {cat_min_f[0]} - ${cat_min_f[1]:,.2f}")
    print(f"  Categoria con menor volumen    : {cat_min_u[0]} - {cat_min_u[1]} unidades\n")
