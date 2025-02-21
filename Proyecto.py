import datetime

movimientos= []
saldo = 0

def registrar_movimiento():
    global saldo
    movimiento = input("Es un ingreso o egreso: ").capitalize()
    descripcion = input("Descripción: ")
    precio = input("Monto ($): ")
    precio = float(precio.replace('$', '').replace(',', ''))

    fecha = datetime.datetime.now()
    movimientos.append((movimiento, descripcion, precio, fecha))

    print(f"{movimiento} realizado el {fecha}, con un valor de ${precio}, descripción: {descripcion}")

    if movimiento == "Ingreso":
        saldo += precio
    elif movimiento == "Egreso":
        saldo -= precio
    else:
        print("Movimiento no válido")

def registrar_saldo():
    global saldo
    print(f"Saldo actual: ${saldo}")

def mostrar_historial():
    print("\nHistorial de movimientos:")
    for movimiento, descripcion, precio, fecha in movimientos:
        print(f"{movimiento} el {fecha}, con un precio de ${precio}, Descripción: {descripcion}")


def mostrar_mes_actual():
    mes_actual = datetime.datetime.now().month
    ingreso_total = 0
    egreso_total = 0

    for movimiento, descripcion, precio, fecha in movimientos:
        if fecha.month == mes_actual:
            if movimiento == "Ingreso":
                ingreso_total += precio
            elif movimiento == "Egreso":
                egreso_total += precio

    print(f"\nTotal de ingresos en el mes: ${ingreso_total}")
    print(f"Total de egresos en el mes: ${egreso_total}")
    print(f"Saldo neto en el mes: ${ingreso_total - egreso_total}")

while True:
    print("\nOpciones:")
    print("1. Registrar movimiento")
    print("2. Ver historial de movimientos")
    print("3. Ver saldo actual")
    print("4. Ver resumen del mes actual")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        registrar_movimiento()
    elif opcion == '2':
        mostrar_historial()
    elif opcion == '3':
        registrar_saldo()
    elif opcion == '4':
        mostrar_mes_actual()
    elif opcion == '5':
        break