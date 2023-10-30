class Aeropuerto:
    instancia = None

    def __init__(self):
        self.vuelos = []

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
        return torreControl.disponibilidadNaves()

    def asignarVuelo(self):
        for vuelo in self.vuelos:
            torreControl.seleccionarAeronave(vuelo)

    def obtenerVuelo(self, pos):
        return self.vuelos[pos]
