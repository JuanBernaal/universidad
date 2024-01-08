from aeronave import Aeronave

class JetPrivado(Aeronave):
    def __init__(self, marca, capacidad, mediator):
        super().__init__(marca, capacidad, mediator)
        self.propietario = ""

    def getPropietario(self):
        return self.propietario

    def printInfo(self):
        super().printInfo()

    def obtenerDatos(self):
        try:
            self.propietario = input("Ingrese el nombre del propietario: ")
        except Exception as e:
            print("Error:", e)
