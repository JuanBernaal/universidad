from torreControl import TorreControl

class Aeropuerto:
    instancia = None

    def __init__(self):
        self.vuelos = []
        self.torreControl = TorreControl()  # Crear una instancia de TorreControl

    @classmethod
    def obtenerInstancia(cls):
        if not cls.instancia:
            cls.instancia = cls()
        return cls.instancia

    def agregarDestino(self, vuelo):
        self.vuelos.append(vuelo)

    def printDestinos(self):
        if not self.vuelos:
            print("No hay vuelos")
        else:
            for i, vuelo in enumerate(self.vuelos, 1):
                print(f"{i}.")
                vuelo.printVuelo()

    def disponibilidadVuelos(self):
        return bool(self.vuelos)

    def disponibilidadAeronaves(self):
        return (self.torreControl.disponibilidadNaves())  # Utiliza la instancia de TorreControl

    def asignarVuelo(self):
        for vuelo in self.vuelos:
            self.torreControl.seleccionarAeronave(vuelo)  # Utiliza la instancia de TorreControl

    def obtenerVuelo(self, pos):
        return self.vuelos[pos]

    def empty(self):
        return not self.vuelos
