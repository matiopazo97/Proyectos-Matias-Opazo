import numpy as np
import datetime 


pisos = 10
departamentos_por_piso = 4
precios = {'A': 3800, 'B': 3000, 'C': 2800, 'D': 3500}
departamentos_disponibles = [[True] * departamentos_por_piso for _ in range(pisos)]
compradores = []


def mostrar_menu():
    print("----- MENÚ -----")
    print("1. Comprar departamento")
    print("2. Mostrar departamentos disponibles")
    print("3. Ver listado de compradores")
    print("4. Mostrar ganancias totales")
    print("5. Salir")

def comprar_departamento():
    print("Departamentos disponibles:")
    for piso in range(pisos):
        for i, disponible in enumerate(departamentos_disponibles[piso]):
            if disponible:
                print(f"Piso {piso + 1} - Departamento {chr(65 + i)}")
            else:
                print(f"Piso {piso + 1} - Departamento {chr(65 + i)} (Vendido)")
    piso = int(input("Ingrese el número del piso: "))
    tipo = input("Ingrese el tipo de departamento (A, B, C o D): ").upper()
    
    if not (1 <= piso <= pisos) or tipo not in precios:
        print("Opción incorrecta.")
        return
    
    departamento_index = ord(tipo) - ord('A')
    
    if not departamentos_disponibles[piso - 1][departamento_index]:
        print("Departamento vendido, no está disponible.")
        return
    
    run = input("Ingrese el RUN sin puntos ni guión: ")
    
    
    
    compradores.append({'piso': piso, 'tipo': tipo, 'run': run})
    departamentos_disponibles[piso - 1][departamento_index] = False
    print("Departamento comprado correctamente.")

def mostrar_departamentos_disponibles():
    print("Departamentos disponibles:")
    for piso in range(pisos):
        for i, disponible in enumerate(departamentos_disponibles[piso]):
            if disponible:
                print(f"Piso {piso + 1} - Departamento {chr(65 + i)}")
            else:
                print(f"Piso {piso + 1} - Departamento {chr(65 + i)} (Vendido)")

def mostrar_listado_compradores():
    compradores_ordenados = sorted(compradores, key=lambda c: c['run'])
    print("Lista de compradores:")
    for comprador in compradores_ordenados:
        print(f"Piso {comprador['piso']} - Departamento {comprador['tipo']}: {comprador['run']}")

def mostrar_ganancias_totales():
    total_ventas = {tipo: 0 for tipo in precios}
    for comprador in compradores:
        tipo = comprador['tipo']
        total_ventas[tipo] += precios[tipo]
    
    print("Ventas totales:")
    print("Tipo de Departamento   Cantidad   Total")
    total_general = 0
    for tipo, total_venta in total_ventas.items():
        cantidad = total_venta // precios[tipo]
        total_general += total_venta
        print(f"Tipo {tipo}           {cantidad}        {total_venta} UF")
    
    print(f"TOTAL                  {len(compradores)}       {total_general} UF")


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        comprar_departamento()
    elif opcion == "2":
        mostrar_departamentos_disponibles()
    elif opcion == "3":
        mostrar_listado_compradores()
    elif opcion == "4":
        mostrar_ganancias_totales()
    elif opcion == "5":
        nombre = input("Ingrese su Nombre: ")
        apellido = input("Ingrese su apellido: ")
        fecha_actual = datetime.datetime.now().strftime("%d-%m-%Y")
        print(f"¡Hasta luego {nombre} {apellido}! Fecha: {fecha_actual}")
        break
    else:
        print("Opción incorrecta, ingresa una opción valida.")