class Aeronave:
    def __init__(self, m, c, mediator):
        self.mediador = mediator
        self.mediador.registrarAeronave(self)
        self.marca = m
        self.modelo = "2019"
        self.capacidad = c
        self.vuelos = []
        self.estado = True
        self.sillasDispo = 0
        self.puertaDeEmbarque = None

    def enviarMensaje(self, mensaje):
        self.mediador.enviarMensaje(mensaje, self)

    def tieneVuelos(self):
        return len(self.vuelos) > 0

    def eliminarVuelo(self):
        if self.vuelos:
            self.vuelos.pop()

    def despegar(self):
        print(f"{self.marca}: Despegando.")
        self.enviarMensaje(f"Despegando {self.marca}")

    def aterrizar(self):
        print(f"{self.marca}: Aterrizando.")
        self.enviarMensaje(f"Aterrizando {self.marca}")

    def actualizarPosicion(self, mensaje):
        print(f"{self.marca}: Actualizando posicion a {mensaje}")
        self.enviarMensaje(f"Nueva posicion: {self.marca} {mensaje}")

    def recibirMensaje(self, mensaje):
        print(f"{self.marca} recibio mensaje: {mensaje}")

    def asignarPuertaDeEmbarque(self, puerta, cod, hora):
        print(f"{self.marca} se dirige a la puerta de embarque: {puerta} Para el vuelo #{cod} Hora: {hora}")

    def agregarVuelo(self, vuelo):
        flag = self.estado

        for v in self.vuelos:
            if vuelo.identificacion == v.identificacion:
                flag = False

        if len(self.vuelos) < 3 and flag:
            self.vuelos.append(vuelo)
        else:
            self.estado = False

        if len(self.vuelos) == 3:
            self.estado = False

    def printInfo(self):
        print(f"Marca: {self.marca}")
        print(f"Capacidad: {self.capacidad}")

    def getCapacidad(self):
        return self.capacidad

    def setModelo(self, s):
        self.modelo = s

    def setNombre(self, s):
        self.nombre = s

    def setAutonomia(self, i):
        self.autonomia = i

    def setFabricacion(self, i):
        self.fabricacion = i

    def setVelMax(self, i):
        self.velMax = i

    def setSillasDispo(self, i):
        self.sillasDispo = i

    def setEstado(self, b):
        self.estado = b

    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo

    def getNombre(self):
        return self.nombre

    def getAutonomia(self):
        return self.autonomia

    def getFabricacion(self):
        return self.fabricacion

    def getVelMax(self):
        return self.velMax

    def getSillasDispo(self):
        return self.sillasDispo

    def getEstado(self):
        return self.estado