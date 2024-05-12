from persona import Persona

class Tripulante(Persona):
    def __init__(self, nombre, apellido, edad, cedula, fechaNacimiento, genero, direccion, numTel, correo, cargo, xp, hrsDiarias):
        super().__init__(nombre, apellido, edad, cedula, fechaNacimiento, genero, direccion, numTel, correo)
        self.cargo = cargo
        self.xp = xp
        self.hrsDiarias = hrsDiarias

    def getInformacion(self):
        super().getInformacion()
        print(f"Cargo en el avión: {self.cargo}")
        print(f"Años de experiencia: {self.xp}")
        print(f"Horas diarias: {self.hrsDiarias}")
