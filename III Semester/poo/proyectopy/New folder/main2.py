from aeropuerto import Aeropuerto
from aeronave import Aeronave
from avion import Avion
from jet import JetPrivado
from helicoptero import Helicoptero
from pasajero import Pasajero
from torreControl import TorreControl
from vuelos import Vuelos


def agregarNaves(aeropuerto):
    while True:
        printLinea()
        print("Agregar:\n1. Avión\n2. JetPrivado\n3. Helicóptero\n4. Salir")
        cases = int(input())
        if cases == 1:
            printLinea()
            n = input("Ingrese la marca del avión: ")
            capacidad = int(input("Ingrese la capacidad del avión: "))
            tmp = Avion(n, capacidad, aeropuerto.torreControl)
            num = int(input("¿Desea especificar más detalles?\n1. Sí\n2. No\n"))
            if num == 1:
                tmp.obtenerDatos()
        elif cases == 2:
            printLinea()
            n = input("Ingrese la marca del JetPrivado: ")
            capacidad = int(input("Ingrese la capacidad del JetPrivado: "))
            tmp = JetPrivado(n, capacidad, aeropuerto.torreControl)
            num = int(input("¿Desea especificar más detalles?\n1. Sí\n2. No\n"))
            if num == 1:
                tmp.obtenerDatos()
        elif cases == 3:
            printLinea()
            n = input("Ingrese la marca del Helicóptero: ")
            capacidad = int(input("Ingrese la capacidad del Helicóptero: "))
            tmp = Helicoptero(n, capacidad, aeropuerto.torreControl)
            num = int(input("¿Desea especificar más detalles?\n1. Sí\n2. No\n"))
            if num == 1:
                tmp.obtenerDatos()
        elif cases == 4:
            print("Saliendo")
            break
        else:
            print("Selección errónea, seleccione una opción válida...")

        aeropuerto.torreControl.mostrarAviones()
        printLinea()


def reserva(aeropuerto):
    if aeropuerto.empty():
        print("No hay vuelos")
    else:
        pasajero = Pasajero()
        pasajero.obtenerDatosPasajero()
        printLinea()
        flag = True 
        while flag:
            pasajero.getInformacion()
            s = int(input("¿Los datos son correctos?\n1. Sí\n2. No\n"))
            if s == 2:
                pasajero.obtenerDatosPasajero()
            else:
                flag = False

        print("Seleccione su vuelo")
        aeropuerto.printDestinos()
        selec = int(input())
        selec -= 1
        tmp = aeropuerto.obtenerVuelo(selec)
        pasajero.asignarVuelo(tmp)
        print("El vuelo ha sido reservado, ¿desea consultarlo?\n1. Sí\n2. No\n")
        selec = int(input())
        if selec == 1:
            tmp.printVuelo()
            nxy = int(input("¿Desea continuar?\n1. Sí\n"))


def printLinea():
    print(
        "===========================================================================================\n"
    )


def main():
    aeropuerto = Aeropuerto.obtenerInstancia()
    flag = True
    printLinea()
    npas = ""

    while flag:
        print(
            "Bienvenido\n1. Modificar vuelos\n2. Agregar naves\n3. Simular\n4. Reservar vuelo\n5. Consultar información\n6. Salir"
        )
        cases = int(input())
        print()
        flag2 = True

        if cases == 1:
            while flag2:
                print("Agregue vuelos")
                try:
                    id = int(input("Ingrese la identificación del vuelo: "))
                except ValueError:
                    print("Error: Argumento inválido. Ingrese un número entero.")
                    id = int(input())

                fecha = input("Ingrese la fecha del vuelo (YYYY-MM-DD): ")
                ciudadDestino = input("Ingrese la ciudad de destino: ")
                hora = input("Ingrese la hora del vuelo (HH:MM): ")

                tmp = Vuelos(id, fecha, ciudadDestino, hora)
                aeropuerto.agregarDestino(tmp)

                num = int(input("¿Salir?\n1. Sí\n2. No\n"))
                if num == 1:
                    flag2 = False

        elif cases == 2:
            agregarNaves(aeropuerto)

        elif cases == 3:
            aeropuerto.asignarVuelo()
            aeropuerto.torreControl.simulacion()
            print("¿Desea continuar?\n1. Sí")
            npas = input()

        elif cases == 4:
            reserva(aeropuerto)

        elif cases == 5:
            printLinea()
            while flag2:
                print(
                    "1. Consultar Vuelos\n2. Consultar Puertas\n3. Consultar Aeronaves\n4. Salir"
                )
                num = int(input())
                if num == 1:
                    aeropuerto.printDestinos()
                elif num == 2:
                    aeropuerto.torreControl.mostrarPuertas()
                elif num == 3:
                    aeropuerto.torreControl.mostrarAviones()
                else:
                    flag2 = False
                printLinea()

        elif cases == 6:
            flag = False

    return 0


main()
