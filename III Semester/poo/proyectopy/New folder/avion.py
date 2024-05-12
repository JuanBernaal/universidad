from aeronave import Aeronave

class Avion(Aeronave):
    def __init__(self, marca, capacidad, mediator):
        super().__init__(marca, capacidad, mediator)
        self.altitudMax = 0
        self.categoria = 0
        self.numMotores = 0

    def getAltitudMax(self):
        return self.altitudMax

    def getCategoria(self):
        return self.categoria

    def getNumMotores(self):
        return self.numMotores

    def printInfo(self):
        super().printInfo()

    def obtenerDatos(self):
        try:
            self.numMotores = int(input("Ingrese el numero de motores: "))
            self.categoria = int(input("Ingrese la categoria: "))
            self.altitudMax = int(input("Ingrese la altitud maxima: "))
        except ValueError:
            print("Error: Entrada no valida. Debe ingresar un numero entero.")
