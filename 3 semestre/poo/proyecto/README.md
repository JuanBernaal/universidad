# Proyecto Programación Orientada a Objetos
Este proyecto tiene como objetivo desarrollar un sistema de gestión para el aeropuerto Alfonso Bonilla Aragón de la ciudad de Cali. Los estudiantes de la Universidad Javeriana deben proporcionar una solución completa para administrar diversos aspectos del funcionamiento del aeropuerto. 

## Funcionalidades Destacadas

- **Registro de Aeronaves**: En este proyecto se tienen en cuenta 3 alternativas de transporte aereo como lo son los helicopteros, aviones y jets privados. 

- **Torre de Control**: Garantiza la seguridad en el espacio aéreo del aeropuerto mediante el seguimiento en tiempo real de la ubicación de las aeronaves y la prevención de colisiones. Además aporta jerarquía y determina que avión puede despegar o aterrizar según las condiciones dadas.

- **Registro de Vuelos**: Los vuelos programados pueden ser registrados y administrados por el aeropuerto, incluyendo diferentes datos que permiten llevar un registro mas preciso de cada vuelo.

- **Gestión de Pasajeros**: El sistema permite registrar pasajeros en los vuelos, de esta manera se lleva registro de cuantos pasajeros pueden entrar en un vuelo teniendo en cuenta la cantidad de espacios disponibles que haya en la respectiva aeronave.

- **Registro de Tripulación**: Los tripulantes de los vuelos tienen su sistema de identificación, en los cuales se puede obtener el cargo que ocupan dentro de la aeronave.

- **Asignación de Puertas de Embarque**: El sistema es capaz de asignar puertas de embarque para los vuelos, lo que permite un mayor orden dentro del aeropuerto.

## Requisito

El sistema del aeropuerto está escrito en el lenguaje de programación c++, asegurate de tenerlo instalado correctamente en el dispositivo que desees usar para ejecutar el programa.

## ¿Cómo comenzar a usarlo?

El proyecto proporciona un ejemplo en el archivo _"main.cpp"_. A partir de este ejemplo el usuario puede construir nuevos objetos. Si desea utilizar algún metodo implementado, puede visitar la sección _Metodos_ para ver su implementación.

## Metodos

## Persona
La clase `Persona` representa a una persona en el sistema y cuenta con un constructor y un método `getInformacion()`.
#### Constructor
- `Persona()`: Recibe 9 parámetros en el siguiente orden:
    1. `Nombre`: string.
    2. `Apellido`: string.
    3. `Edad`: int.
    4. `Cédula`: string.
    5. `Fecha de Nacimiento`: string.
    6. `Género`: string.
    7. `Dirección`: string.
    8. `Número de Teléfono`: string.
    9. `Correo`: string.

#### Método

- `getInformacion()`: Esta función imprime todos los datos de la persona.

## Clase Pasajero

La clase `Pasajero` hereda todos los atributos de la clase `Persona` y añade 3 nuevos atributos.

#### Constructor

El constructor de la clase `Pasajero` es el mismo que el de `Persona`. Al final se le añaden los siguientes datos en orden:

- `Nacionalidad`: string.
- `Información Médica`: string.
- `Número de Maletas`: int.

#### Método

- `getInformacion()`: Este método proporciona todos los datos de la persona y los atributos adicionales de `Pasajero`.

## Clase Tripulante

La clase `Tripulante` también hereda todos los atributos de la clase `Persona` y añade 3 nuevos atributos.

#### Constructor

El constructor de la clase `Tripulante` es el mismo que el de `Persona`. Al final se le añaden los siguientes datos en orden:

- `Cargo`: string.
- `Experiencia`: int.
- `Horas Diarias`: int.

#### Método

- `getInformacion()`: Proporciona todos los datos de la persona y los atributos adicionales de `Tripulante`.
## Aeronave
La clase `Aeronave` representa una aeronave en el sistema de gestión del aeropuerto. Esta clase incluye atributos y métodos para administrar información relacionada con las aeronaves y sus operaciones.

#### Atributos
- `marca`.
- `modelo`.
- `nombre`.
- `capacidad`.
- `Autonomía`.
- `Año de fabricación`.
- `Velocidad maxima`.
- `sillas disponibles`.
- `id`.
- `vuelos`: Vector que almacena los vuelos programados para la aeronave.
- `estado`: Indica si la aeronave está en servicio, totalmente asignada o en mantenimiento.

#### Constructor
La clase `Aeronave` tiene dos constructores:
- `Aeronave()`: Constructor por defecto.
- `Aeronave(const string &marca, int capacidad, MediadorTrafico *mediator)`: Constructor que recibe la marca, la capacidad y un objeto `MediadorTrafico`.

#### Métodos

La clase `Aeronave` cuenta con los siguientes métodos:

- `despegar()`: Método que simula el despegue de la aeronave.
- `aterrizar()`: Método que simula el aterrizaje de la aeronave.
- `actualizarPosicion(const string &mensaje)`: Actualiza la posición de la aeronave con un mensaje.
- `recibirMensaje(const string &mensaje)`: Recibe un mensaje.
- `asignarPuertaDeEmbarque(const string &puerta)`: Asigna una puerta de embarque a la aeronave.
- `agregarVuelo(Vuelos &v)`: Agrega un vuelo a la lista de vuelos de la aeronave.
- `getCapacidad()`: Obtiene la capacidad de pasajeros de la aeronave.
- `setModelo(const string s)`: Establece el modelo de la aeronave.
- `setNombre(const string s)`: Establece el nombre de la aeronave.
- `setAutonomia(int i)`: Establece la autonomía de la aeronave.
- `setFabricacion(int i)`: Establece el año de fabricación de la aeronave.
- `setVelMax(int i)`: Establece la velocidad máxima de la aeronave.
- `setSillasDispo(int i)`: Establece la cantidad de sillas disponibles en la aeronave.
- `setEstado(bool b)`: Establece el estado de la aeronave.
- `getMarca()`: Obtiene la marca de la aeronave.
- `getModelo()`: Obtiene el modelo de la aeronave.
- `getNombre()`: Obtiene el nombre de la aeronave.
- `getAutonomia()`: Obtiene la autonomía de la aeronave.
- `getFabricacion()`: Obtiene el año de fabricación de la aeronave.
- `getVelMax()`: Obtiene la velocidad máxima de la aeronave.
- `getSillasDispo()`: Obtiene la cantidad de sillas disponibles en la aeronave.
- `getEstado()`: Obtiene el estado de la aeronave.

## Clase Helicóptero

La clase `Helicoptero` representa un helicóptero y hereda de la clase `Aeronave`. Agrega 3 atributos.

#### Constructor

- `Helicoptero(const string &marca, int capacidad, MediadorTrafico *mediator)`: Constructor que recibe la marca, la capacidad y un objeto `MediadorTrafico`. Llama al constructor de la clase base `Aeronave`.

#### Métodos

La clase `Helicoptero` cuenta con los siguientes métodos:

- `getNumRotores()`: Obtiene el número de rotores del helicóptero.
- `getMaxElevacion()`: Obtiene la máxima elevación alcanzada por el helicóptero.
- `getUso()`: Obtiene el uso específico del helicóptero (por ejemplo, rescate, turismo, transporte, etc.).

#### Atributos

Además de los atributos heredados de la clase `Aeronave`, la clase `Helicoptero` agrega los siguientes atributos:

- `numRotores`: El número de rotores del helicóptero.
- `maxElevacion`: La máxima elevación alcanzada por el helicóptero.
- `uso`: El uso específico del helicóptero.

## Clase Avión
La clase `Avion` representa un avion y hereda la clase `Aeronave` y añade 3 atributos más.

#### Constructor
- `Avion(const string &marca, int capacidad, MediadorTrafico *mediator, int altMax, int numMot, int categoria)`:  Constructor que recibe, Altitud maxima, numero de motores y la categoria del avion. Llama al constructor de la clase Aeronave.
#### Métodos
- `getAltitudMax()`.
- `getNumMotores()`.
- `getCategoria()`.
#### Atributos
- Hereda los atributos de Aeronave.
- `Altitud Maxima`.
- `Numero de motores`.
- `Categoria`.
## Clase JetPrivado

La clase `JetPrivado` representa un jet privado y hereda de la clase `Aeronave`. 

## Constructor

- `JetPrivado(const string &marca, int capacidad, MediadorTrafico *mediator)`: Constructor que recibe la marca, la capacidad y un objeto `MediadorTrafico`. Llama al constructor de la clase base `Aeronave` e inicializa los atributos adicionales.

## Métodos

La clase `JetPrivado` cuenta con los siguientes métodos:

- `getPropietario()`: Obtiene el nombre del propietario del jet privado.

## Atributos

Además de los atributos heredados de la clase `Aeronave`, la clase `JetPrivado` agrega los siguientes atributos:

- `propietario`: El nombre del propietario del jet privado.
- `listaServicios`: Una lista de servicios a bordo proporcionados por el jet privado.
- `listaDestinos`: Una lista de destinos frecuentes a los que viaja el jet privado.

# Clase TorreControl

La clase `TorreControl` se encarga de gestionar y coordinar las comunicaciones entre las diferentes aeronaves en el aeropuerto. Esta clase implementa la interfaz `MediadorTrafico`.

## Métodos

La clase `TorreControl` cuenta con los siguientes métodos:

- `registrarAeronave(Aeronave* aeronave)`: Permite registrar una aeronave en la torre de control para su seguimiento y comunicación.

- `enviarMensaje(const string& mensaje, Aeronave* emisor)`: Envía un mensaje a todas las aeronaves registradas, excepto al emisor.

- `asignarPuertaDeEmbarque(Aeronave* aeronave, const string& puerta)`: Asigna una puerta de embarque a una aeronave específica.

## Clase Abstracta: Mediador de Trafico

La clase abstracta `MediadorTrafico` define la interfaz que deben implementar las clases que actúan como mediadores de tráfico en el aeropuerto.

#### Métodos
- `registrarAeronave(Aeronave* aeronave) = 0`: Registra una aeronave en el mediador.
- `enviarMensaje(const string& mensaje, Aeronave* emisor) = 0`: Envia mensaje a las aeronaves registradas.
- `asignarPuertaDeEmbarque(Aeronave* aeronave, const string& puerta) = 0`: Asigna una puerta de embarque a una aeronave especifica. 

## Clase Aeropuerto.
Esta clase representa el aeropuerto Alfonso Bonilla Aragon, y está hecho con el patrón de diseño singletone para garantizar que solo exista una instancia de esta clase en el sistema.

#### Métodos
- `Aeropuerto()`: Se encarga iniciar la lista de vuelos.
- `agregarDestino(Vuelos *v)`: Se encarga de agregar destinos disponibles.
- `printDestinos()`: Muestra al usuario los destinos disponibles.

## Contacto
Si tienes alguna duda, comentario o sugerencia, puedes contactarnos a través de nuestro correo:
[juaanbernal'@'javerianacali.edu.co](https://outlook.live.com/mail/0/)
[judival30'@'javerianacali.edu.co](https://outlook.live.com/mail/0/)