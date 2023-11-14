class Persona:
    def __init__(self, nombre, apellido, edad, cedula, fechaNacimiento, genero, direccion, numTel, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cedula = cedula
        self.fechaNacimiento = fechaNacimiento
        self.genero = genero
        self.direccion = direccion
        self.numTel = numTel
        self.correo = correo

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getInformacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad} years")
        print(f"Cedula: {self.cedula}")
        print(f"Fecha de Nacimiento: {self.fechaNacimiento}")
        print(f"Genero: {self.genero}")
        print(f"Direccion: {self.direccion}")
        print(f"Numero de Telefono: {self.numTel}")
        print(f"Correo Electronico: {self.correo}")