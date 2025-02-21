import datetime

movimientos=()
saldo=()

def registrar_movimiento():
      global saldo
movimiento= input("¿Es un ingreso o egreso?")
descripción= input("Descripción")
precio_str=input("Precio $: ")
precio=float()


fecha=datetime.datatime.now()
movimientos.append(precio_str.replace('$', '').replace(',', ''))

print(f"el movimiento{movimiento}, descripción{descripción},
      realizado el {fecha}, con un precio {precio}")


if movimiento== "Ingreso":
      saldo+=precio
if movimiento=="Egreso":
      saldo-=precio


def historial():
      print(f"Historial de tus movimientos")
      for movimientos in descripción, precio in fecha:
            print(f"el movimiento{movimientos}, con una descripción{descripción},
                   realizada el {fecha} con un precio de {precio}")


def registrar_misaldo():
      global saldo
      print(f"tu saldo actual es {saldo}")
    

def tu_historial():
      print(f"Historial de tus movimientos")
      for movimientos in descripción, precio in fecha:
            print(f"el movimiento{movimientos}, con una descripción{descripción},
                   realizada el {fecha} con un precio de {precio}")
        
def mostrar_mes():
    mes_actual = datetime.datetime.now().month
    ingreso_total = 0
    egreso_total = 0

    for movimiento, descripcion, precio, fecha in movimientos:
        if fecha.month == mes_actual:
            if movimiento == "Ingreso":
                ingreso_total += precio
            elif movimiento == "Egreso":
                egreso_total += precio


    print(f"Total de ingresos en el mes: ${ingreso_total}")
    print(f"Total de egresos en el mes: ${egreso_total}")
    print(f"Saldo neto en el mes: ${ingreso_total - egreso_total}")

while True:
    print("Tus Opciones:")
    print("1. Registrar tus movimientos")
    print("2. Ver historial de tus movimientos")
    print("3. Ver tu saldo actual")
    print("4. Ver el resumen del mes actual")
    print("5. Salir")

    opción=input("Elige la opción que necesites")
    if opción==1:
        registrar_movimiento
    elif opción==2:
         tu_historial
    elif opción==3:
         registrar_misaldo
    elif opción==4:
         mostrar_mes
    elif opción==5:
         break
    

  