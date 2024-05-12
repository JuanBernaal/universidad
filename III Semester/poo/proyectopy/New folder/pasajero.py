from persona import Persona
import os

class Pasajero(Persona):
    def __init__(self, nombre = "", apellido="", edad=0, cedula="", fechaNacimiento="", genero="", direccion="", numTel="", correo="", nacionalidad="", infoMedica="", numMaletasBodega=""):
        super().__init__(nombre="", apellido="", edad="", cedula="", fechaNacimiento="", genero="", direccion="", numTel="", correo="")
        self.numMaletasBodega = numMaletasBodega
        self.nacionalidad = nacionalidad
        self.infoMedica = infoMedica
        self.vuelo = None

    def obtenerDatosPasajero(self):
        self.nombre = input("Ingrese el nombre del pasajero: ")
        self.apellido = input("Ingrese el apellido del pasajero: ")
        self.edad = int(input("Ingrese la edad del pasajero: "))
        self.cedula = input("Ingrese la cedula del pasajero: ")
        self.fechaNacimiento = input("Ingrese la fecha de nacimiento del pasajero: ")
        self.genero = input("Ingrese el genero del pasajero: ")
        self.direccion = input("Ingrese la direccion del pasajero: ")
        self.numTel = input("Ingrese el numero de telefono del pasajero: ")
        self.correo = input("Ingrese el correo del pasajero: ")
        self.nacionalidad = input("Ingrese la nacionalidad del pasajero: ")
        self.infoMedica = input("Ingrese la informacion medica del pasajero: ")
        self.numMaletasBodega = int(input("Ingrese el numero de maletas de bodega del pasajero: "))
        os.system("cls")

    def getNumMaletas(self):
        return self.numMaletasBodega

    def asignarVuelo(self, v):
        if v.disponible():
            self.vuelo = v
            print("El vuelo se asignó correctamente.")
        else:
            print("El vuelo no está disponible.")

    def getInformacion(self):
        super().getInformacion()
        print("Numero de Maletas en Bodega:", self.numMaletasBodega)
        print("Nacionalidad:", self.nacionalidad)
        print("Informacion Medica:", self.infoMedica)
