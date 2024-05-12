from aeronave import Aeronave

class Helicoptero(Aeronave):
    def __init__(self, marca, capacidad, mediator):
        super().__init__(marca, capacidad, mediator)
        self.numRotores = 0
        self.maxElevacion = 0
        self.uso = ""

    def getNumRotores(self):
        return self.numRotores

    def getMaxElevacion(self):
        return self.maxElevacion

    def getUso(self):
        return self.uso

    def printInfo(self):
        super().printInfo()

    def obtenerDatos(self):
        try:
            self.numRotores = int(input("Ingrese el numero de rotores: "))
            if self.numRotores <= 0:
                raise ValueError("Entrada no valida para numero de rotores.")
            
            self.maxElevacion = int(input("Ingrese la maxima elevacion: "))
            if self.maxElevacion <= 0:
                raise ValueError("Entrada no valida para maxima elevacion.")
            
            self.uso = input("Ingrese el tipo de uso: ")
        except ValueError as e:
            print("Error:", e)
