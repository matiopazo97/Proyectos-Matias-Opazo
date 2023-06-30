
import numpy as np

desarrollo_residencial = [[' ' for _ in range(5)] for _ in range(4)]



lotes = [
    {'numero': '1', 'tamaño': '100 m2', 'precio': '$300,000'},
    {'numero': '2', 'tamaño': '150 m2', 'precio': '$400,000'},
    {'numero': '3', 'tamaño': '120 m2', 'precio': '$330,000'},
    {'numero': '4', 'tamaño': '200 m2', 'precio': '$600,000'}
]


clientes = []


def mostrar_disponibilidad_lotes():
    print("Lotes Disponibles:")
    for fila in desarrollo_residencial:
        for lote in fila:
            if lote == 0:
                print("[1,2,3,4]", end= "")
        else:
            print("[ ]", end=" ")
        print()


def seleccionar_lote():
    rut = input("Ingrese su RUT: ")
    nombre = input("Ingrese su nombre completo: ")
    telefono = input("Ingrese su número de teléfono: ")
    email = input("Ingrese su dirección de correo electrónico: ")

    fila = int(input("Ingrese el número de fila del lote: "))
    columna = int(input("Ingrese el número de columna del lote: "))

    if fila < 0 or fila >= len(desarrollo_residencial) or columna < 0 or columna >= len(desarrollo_residencial[0]):
        print("Las coordenadas no son validas, intente nuevamente.")
        return

    if desarrollo_residencial[fila][columna] == ' ':
        desarrollo_residencial[fila][columna] = 'X'
        clientes.append({'RUT': rut, 'Nombre': nombre, 'Teléfono': telefono, 'Email': email})
        print("Lote seleccionado!")
    else:
        print("El lote seleccionado no está disponible. Por favor, elija otro lote.")


def mostrar_detalles_lote():
    if len(clientes) == 0:
        print("No se han seleccionado lotes, porfavor seleccione uno.")
        return

    cliente = clientes[-1]  
    lote = lotes[len(clientes) - 1]  

    print("Detalles del lote seleccionado:")
    print(f"Número de lote: {lote['numero']}")
    print(f"Tamaño del terreno: {lote['tamaño']}")
    print(f"Precio: {lote['precio']}")
    print(f"Cliente: {cliente['Nombre']}")
    print(f"RUT: {cliente['RUT']}")
    print(f"Teléfono: {cliente['Teléfono']}")
    print(f"Email: {cliente['Email']}")


def mostrar_clientes():
    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return

    print("Clientes:")
    for cliente in clientes:
        print(f"Nombre: {cliente['Nombre']}")
        print(f"RUT: {cliente['RUT']}")
        print(f"Teléfono: {cliente['Teléfono']}")
        print(f"Email: {cliente['Email']}")
        print()


def main():
    while True:
        print("\n--- Menú ---")
        print("1. Ver disponibilidad de lotes")
        print("2. Seleccionar un lote")
        print("3. Ver detalles del lote seleccionado")
        print("4. Ver clientes")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            mostrar_disponibilidad_lotes()
        elif opcion == '2':
            seleccionar_lote()
        elif opcion == '3':
            mostrar_detalles_lote()
        elif opcion == '4':
            mostrar_clientes()
        elif opcion == '5':
            print("Muchas Gracias! Vuelva Pronto.")
            break
        else:
            print("Opción incorrecta. Por favor, ingrese una opción correcta.")

main()