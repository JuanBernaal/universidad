from random import randint
import time

class PuertaEmbarque:
    def __init__(self, nombre):
        self.identificacion = nombre
        self.disponibilidad = True

    def anunciarEmbarque(self, puerta):
        print(f"Anuncio de embarque en {self.identificacion} - Puerta {puerta}")

class TorreControl:
    def __init__(self):
        self.puertas = [PuertaEmbarque(1), PuertaEmbarque(2), PuertaEmbarque(3), PuertaEmbarque(4), PuertaEmbarque(5), PuertaEmbarque(6)]
        self.aeronaves = []

    def registrarAeronave(self, aeronave):
        self.aeronaves.append(aeronave)

    def registrarAvion(self, aeronave):
        self.aviones.append(aeronave)

    def enviarMensaje(self, mensaje, emisor):
        for aeronave in self.aeronaves:
            if aeronave != emisor:
                aeronave.recibirMensaje(mensaje)

    def asignarPuertaDeEmbarque(self, aeronave, puerta, cod, hora):
        aeronave.asignarPuertaDeEmbarque(puerta, cod, hora)
        self.puertas[puerta - 1].disponibilidad = False

    def disponibilidadNaves(self):
        return len(self.aeronaves) > 0

    def mostrarAviones(self):
        if not self.aeronaves:
            print("No hay aeronaves")
        for i, aeronave in enumerate(self.aeronaves, 1):
            print(f"{i}.")
            aeronave.printInfo()

    def seleccionarAeronave(self, vuelo):
        for aeronave in self.aeronaves:
            if aeronave.estado:
                aeronave.agregarVuelo(vuelo)
                flag = True
                for i, puerta in enumerate(self.puertas):
                    if puerta.disponibilidad:
                        self.asignarPuertaDeEmbarque(aeronave, puerta.identificacion, vuelo.identificacion, vuelo.hora)
                        flag = False
                        break
                break

    def generarNumeroAleatorio(self):
        num1 = randint(10000, 99999)
        num2 = randint(10000, 99999)
        if num1 > num2:
            num1, num2 = num2, num1  # Intercambiar valores si num1 > num2
        numeroAleatorio = randint(num1, num2)
        return numeroAleatorio


    def simulacion(self):
        for aeronave in self.aeronaves:
            if aeronave.tieneVuelos():
                for vuelo in aeronave.vuelos:
                    aeronave.despegar()
                    pos1 = self.generarNumeroAleatorio()
                    pos2 = self.generarNumeroAleatorio()
                    posicion = f"Lat: {pos1} Lon: {pos2}"
                    aeronave.actualizarPosicion(posicion)
                    aeronave.aterrizar()
                for vuelo in aeronave.vuelos:
                    aeronave.eliminarVuelo()

        for puerta in self.puertas:
            puerta.disponibilidad = True

    def mostrarPuertas(self):
        for puerta in self.puertas:
            print(f"Puerta #{puerta.identificacion}", "disponible" if puerta.disponibilidad else "no disponible", "\n")

    def generarHoraActual(self):
        return time.strftime("%H:%M:%S")

class Vuelos:
    def __init__(self, identificacion, hora):
        self.identificacion = identificacion
        self.hora = hora
