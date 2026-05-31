# Datos que deben estar en archivos
#========================================/s
#SE CREA LISTA CON DATOS DEL KIOSCO PARA EL ENCABEZADO DE LA FACTURA
empresa = ["Kiosco 'La Puerta Lijada'", "30787654321", "Saraza 6247", "caba", 2026, 4, "WWW.LAPUERTALIJADA.COM", "contacto@lapuertalijada.com"]
encabezados_detalle = ["Código", "Descripción", "P. Unitario", "Cant.", "Subtotal"]


# Lista de Diccionarios reemplazando a las Listas de listas, hay que transferir los datos hardcodeados a archivos
productos = [
    {"id": 1, "producto": "ALFAJOR OREO", "precio": 1100, "stock": 50, "categoria": "DULCE", "proveedor": "DISTRIBUIDORA DULCE SUR", "activo": "Y"},
    {"id": 2, "producto": "RED BULL", "precio": 2800, "stock": 24, "categoria": "BEBIDA", "proveedor": "ENERGIA TOTAL SA", "activo": "Y"},
    {"id": 3, "producto": "ALFAJOR JORGITO", "precio": 850, "stock": 100, "categoria": "DULCE","proveedor": "GOLOSINAS DEL PLATA", "activo": "Y"},
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
