class Vuelos:
    def __init__(self, id, fecha, ciudadDestino, hora, capacidad=100):
        self.identificacion = id
        self.fecha = fecha
        self.ciudadOrigen = "CLO"
        self.ciudadDestino = ciudadDestino
        self.hora = hora
        self.capacidad = capacidad
        self.numPasajeros = 0
        self.estado = True

    def agregarPasajero(self):
        if self.numPasajeros < self.capacidad:
            self.numPasajeros += 1
        else:
            print("Vuelo lleno")

    def printVuelo(self):
        print(f"Fecha: {self.fecha}")
        print(f"Hora: {self.hora}")
        print(f"Ciudad de origen: {self.ciudadOrigen}")
        print(f"Ciudad de destino: {self.ciudadDestino}")

    def disponible(self):
        return self.estado
