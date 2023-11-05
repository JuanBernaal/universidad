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
        return self.torreControl.disponibilidadNaves()  # Utiliza la instancia de TorreControl

    def asignarVuelo(self):
        for vuelo in self.vuelos:
            self.torreControl.seleccionarAeronave(vuelo)  # Utiliza la instancia de TorreControl

    def obtenerVuelo(self, pos):
        return self.vuelos[pos]

    def empty(self):
        return not self.vuelos
    
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
        os.system("cls")

    def getNumMaletas(self):
        return self.numMaletasBodega

    def asignarVuelo(self, v):
        if v.disponible():
            self.vuelo = v
            print("El vuelo se asignó correctamente.")
        else:
            print("El vuelo no está disponible.")

    def getInformacion(self):
        super().getInformacion()
        print("Numero de Maletas en Bodega:", self.numMaletasBodega)
        print("Nacionalidad:", self.nacionalidad)
        print("Informacion Medica:", self.infoMedica)

