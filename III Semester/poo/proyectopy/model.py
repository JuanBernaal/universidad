from random import randint
import time
import os
from random import randint
import time
import streamlit as st

class PuertaEmbarque:
    def __init__(self, nombre):
        self.identificacion = nombre
        self.disponibilidad = True

    def anunciarEmbarque(self, puerta):
        st.write(f"Anuncio de embarque en {self.identificacion} - Puerta {puerta}")

class TorreControl:
    def __init__(self):
        self.puertas = [PuertaEmbarque(1), PuertaEmbarque(2), PuertaEmbarque(3), PuertaEmbarque(4), PuertaEmbarque(5), PuertaEmbarque(6)]
        self.aeronaves = []

    def registrarAeronave(self, aeronave):
        self.aeronaves.append(aeronave)

    def enviarMensaje(self, mensaje, emisor):
        for aeronave in self.aeronaves:
            if aeronave != emisor:
                aeronave.recibirMensaje(mensaje)

    def asignarPuertaDeEmbarque(self, aeronave, puerta, cod, hora, airline):
        aeronave.asignarPuertaDeEmbarque(puerta, cod, hora, airline)
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
                for puerta in self.puertas:
                    if puerta.disponibilidad:
                        self.asignarPuertaDeEmbarque(aeronave, puerta.identificacion, vuelo.identificacion, vuelo.hora, vuelo.airline)
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
                for _ in aeronave.vuelos:
                    aeronave.despegar()
                    pos1 = self.generarNumeroAleatorio()
                    pos2 = self.generarNumeroAleatorio()
                    posicion = f"Lat: {pos1} Lon: {pos2}"
                    aeronave.actualizarPosicion(posicion)
                    aeronave.aterrizar()
                for _ in aeronave.vuelos:
                    aeronave.eliminarVuelo()

        for puerta in self.puertas:
            puerta.disponibilidad = True

    def mostrarPuertas(self):
        for puerta in self.puertas:
            st.write(f"Puerta #{puerta.identificacion}", "disponible" if puerta.disponibilidad else "no disponible", "\n")

    def generarHoraActual(self):
        return time.strftime("%H:%M:%S")

class Vuelos:
    def __init__(self, id, fecha, ciudadDestino, hora, airline, capacidad=100):
        self.identificacion = id
        self.fecha = fecha
        self.ciudadOrigen = "CLO 🟡🔵🔴"
        self.ciudadDestino = ciudadDestino
        self.hora = hora
        self.capacidad = capacidad
        self.numPasajeros = 0
        self.estado = True
        self.airline = airline

    def agregarPasajero(self):
        if self.numPasajeros < self.capacidad:
            self.numPasajeros += 1
        else:
            print("Vuelo lleno")

    def printVuelo(self):
        return {"ID" : self.identificacion, "Fecha" : self.fecha, "Hora" : self.hora, "Ciudad de origen" : self.ciudadOrigen, "Ciudad de destino" : self.ciudadDestino}

    def disponible(self):
        return self.estado
    
class Aeropuerto:
    instancia = None

    def __init__(self):
        self.vuelos = []
        self.destinations = []
        self.avionesAeropuerto = []
        self.helicopterosAeropuerto = []
        self.jetsAeropuerto = []
        self.torreControl = TorreControl()  # Crear una instancia de TorreControl

    @classmethod
    def obtenerInstancia(cls):
        if not cls.instancia:
            cls.instancia = cls()
        return cls.instancia

    def agregarDestino(self, vuelo):
        self.vuelos.append(vuelo)

    def destinationsTab(self, dic):
        self.destinations.append(dic)

    def printDestinos(self):
        if not self.vuelos:
            st.warning("No hay vuelos")
        else:
            for vuelo in self.vuelos:
                st.table(vuelo.printVuelo())

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
    
    def emptyAirplanes(self):
        return not self.avionesAeropuerto
    
    def emptyJets(self):
        return not self.jetsAeropuerto
    
    def emptyHelicopters(self):
        return not self.helicopterosAeropuerto

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
        st.write(f"{self.marca}: Despegando.")
        self.enviarMensaje(f"Despegando {self.marca}")

    def aterrizar(self):
        st.write(f"{self.marca}: Aterrizando.")
        self.enviarMensaje(f"Aterrizando {self.marca}")

    def actualizarPosicion(self, mensaje):
        st.write(f"{self.marca}: Actualizando posicion a {mensaje}")
        self.enviarMensaje(f"Nueva posicion: {self.marca} {mensaje}")

    def recibirMensaje(self, mensaje):
        st.write(f"{self.marca} recibio mensaje: {mensaje}")

    def asignarPuertaDeEmbarque(self, puerta, cod, hora, airline):
        st.write(f"{self.marca} se dirige a la puerta de embarque: {puerta} Para el vuelo #{cod} de {airline}. Hora: {hora}")

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

class Avion(Aeronave):
    def __init__(self, marca, capacidad, mediator, numMotores, categoria, cargaMax):
        super().__init__(marca, capacidad, mediator)
        self.altitudMax = numMotores
        self.categoria = categoria
        self.numMotores = cargaMax
        self.estado = True

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

class Helicoptero(Aeronave):
    def __init__(self, marca, capacidad, mediator, numRotores=1, maxElevacion=1000, uso="Servicio de rescate"):
        super().__init__(marca, capacidad, mediator)
        self.numRotores = numRotores
        self.maxElevacion = maxElevacion
        self.uso = uso

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

class JetPrivado(Aeronave):
    def __init__(self, marca, capacidad, mediator, propietario):
        super().__init__(marca, capacidad, mediator)
        self.propietario = propietario

    def getPropietario(self):
        return self.propietario

    def printInfo(self):
        super().printInfo()

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

class Pasajero(Persona):
    def __init__(self, nombre = "", apellido="", edad=0, cedula="", fechaNacimiento="", genero="", direccion="", numTel="", correo="", nacionalidad="", infoMedica="", numMaletasBodega=""):
        super().__init__(nombre="", apellido="", edad="", cedula="", fechaNacimiento="", genero="", direccion="", numTel="", correo="")
        self.numMaletasBodega = numMaletasBodega
        self.nacionalidad = nacionalidad
        self.infoMedica = infoMedica
        self.vuelo = None

    def obtenerDatosPasajero(self):
        self.nombre = input("Ingrese el nombre del pasajero: ")
        self.apellido = input("Ingrese el apellido del pasajero: ")
        self.edad = int(input("Ingrese la edad del pasajero: "))
        self.cedula = input("Ingrese la cedula del pasajero: ")
        self.fechaNacimiento = input("Ingrese la fecha de nacimiento del pasajero: ")
        self.genero = input("Ingrese el genero del pasajero: ")
        self.direccion = input("Ingrese la direccion del pasajero: ")
        self.numTel = input("Ingrese el numero de telefono del pasajero: ")
        self.correo = input("Ingrese el correo del pasajero: ")
        self.nacionalidad = input("Ingrese la nacionalidad del pasajero: ")
        self.infoMedica = input("Ingrese la informacion medica del pasajero: ")
        self.numMaletasBodega = int(input("Ingrese el numero de maletas de bodega del pasajero: "))

    def getNumMaletas(self):
        return self.numMaletasBodega

    def asignarVueloPass(self, vuelo):
        if vuelo.disponible():
            self.vuelo = vuelo
        else:
            st.error("El vuelo no está disponible")

    def getInformacion(self):
        super().getInformacion()
        print("Numero de Maletas en Bodega:", self.numMaletasBodega)
        print("Nacionalidad:", self.nacionalidad)
        print("Informacion Medica:", self.infoMedica)

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

class Airline():
    def __init__(self, name):
        self.nombre = name
        self.aviones = []

    def getAviones(self):
        st.header("Aviones")
        st.table(self.aviones)