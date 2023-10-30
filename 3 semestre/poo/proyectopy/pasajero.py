from persona import Persona

class Pasajero(Persona):
    def __init__(self, nombre, apellido, edad, cedula, fechaNacimiento, genero, direccion, numTel, correo, nacionalidad, infoMedica, numMaletasBodega):
        super().__init__(nombre, apellido, edad, cedula, fechaNacimiento, genero, direccion, numTel, correo)
        self.numMaletasBodega = numMaletasBodega
        self.nacionalidad = nacionalidad
        self.infoMedica = infoMedica
        self.vuelo = None

    @classmethod
    def obtenerDatosPasajero(cls):
        nombre = input("Ingrese el nombre del pasajero: ")
        apellido = input("Ingrese el apellido del pasajero: ")
        edad = int(input("Ingrese la edad del pasajero: "))
        cedula = input("Ingrese la cedula del pasajero: ")
        fechaNacimiento = input("Ingrese la fecha de nacimiento del pasajero: ")
        genero = input("Ingrese el genero del pasajero: ")
        direccion = input("Ingrese la direccion del pasajero: ")
        numTel = input("Ingrese el numero de telefono del pasajero: ")
        correo = input("Ingrese el correo del pasajero: ")
        nacionalidad = input("Ingrese la nacionalidad del pasajero: ")
        infoMedica = input("Ingrese la informacion medica del pasajero: ")
        numMaletasBodega = int(input("Ingrese el numero de maletas de bodega del pasajero: "))

        return cls(nombre, apellido, edad, cedula, fechaNacimiento, genero, direccion, numTel, correo, nacionalidad, infoMedica, numMaletasBodega)

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
