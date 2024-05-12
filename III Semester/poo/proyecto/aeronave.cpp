#include "aeronave.h"

/**
 * La función "enviarMensaje" de la clase "Aeronave" envía un mensaje utilizando un objeto mediador.
 *
 * @param mensaje El parámetro "mensaje" es una referencia constante a una cadena.
 */
void Aeronave::enviarMensaje(const string &mensaje)
{
    mediador->enviarMensaje(mensaje, this);
}

/**
 * El constructor Aeronave inicializa el objeto Aeronave con una marca, capacidad y
 * Objeto MediadorTrafico, y registra la Aeronave ante el MediadorTrafico.
 *
 * @param m El parámetro "m" es una cadena que representa la marca de la aeronave.
 * @param c El parámetro "c" representa la capacidad de la aeronave, que indica la capacidad máxima
 * número de pasajeros que puede acomodar.
 * @param mediator El parámetro mediador es un puntero a un objeto de tipo MediadorTrafico. Esta usado
 * para establecer comunicación entre el objeto Aeronave y el objeto MediadorTrafico.
 */
Aeronave::Aeronave(const string &m, int c, MediadorTrafico *mediator)
{
    mediador = mediator;
    mediador->registrarAeronave(this);
    marca = m;
    modelo = "2019";
    capacidad = c;
    vuelos = {};
    estado = true;
    sillasDispo = 0;
}

Aeronave::Aeronave()
{
}

/**
 * La función "tieneVuelos" comprueba si el vector "vuelos" tiene algún elemento y devuelve verdadero si
 * lo hace; de ​​lo contrario, devuelve falso.
 *
 * @return un valor booleano. Si el tamaño del vector "vuelos" es mayor que 0 devolverá verdadero.
 * De lo contrario devolverá falso.
 */
bool Aeronave::tieneVuelos()
{
    if (vuelos.size() > 0)
        return true;
    else
        return false;
}
/**
 * La función "eliminarVuelo" elimina el último elemento del vector "vuelos".
 */
void Aeronave::eliminarVuelo()
{
    vuelos.pop_back();
}
/**
 * La función "despegar" imprime un mensaje indicando que el avión está despegando y envía un
 *mensaje con la misma información.
 */
void Aeronave::despegar()
{
    cout << marca << ": Despegando." << endl;
    enviarMensaje("Despegando " + marca);
}

/**
 * La función "aterrizar" imprime un mensaje indicando que una aeronave está aterrizando y envía un mensaje
 *con la misma información.
 */
void Aeronave::aterrizar()
{
    cout << marca << ": Aterrizando." << endl;
    enviarMensaje("Aterrizando " + marca);
}

/**
 * La función "actualizarPosicion" actualiza la posición de una aeronave y envía un mensaje con la
 * nueva posición.
 *
 * @param mensaje El parámetro "mensaje" es una referencia constante a una cadena.
 */
void Aeronave::actualizarPosicion(const string &mensaje)
{
    cout << marca << ": Actualizando posicion a " << mensaje << endl;
    enviarMensaje("Nueva posicion: " + marca + mensaje);
}

/**
 * La función "recibirMensaje" en la clase "Aeronave" imprime un mensaje indicando que la aeronave
 *recibí un mensaje.
 *
 * @param mensaje El parámetro "mensaje" es una referencia constante a una cadena.
 */
void Aeronave::recibirMensaje(const string &mensaje)
{
    cout << marca << " recibio mensaje: " << mensaje << endl;
}

/**
 * La función asigna un número de puerta, código de vuelo y hora a un objeto de aeronave.
 *
 * @param puerta El parámetro "puerta" es un número entero que representa el número de puerta de embarque
 * proceso.
 * @param cod El parámetro "cod" es un número entero que representa el código de vuelo.
 * @param hora El parámetro "hora" es una referencia constante a una cadena. Representa el tiempo en
 * que la aeronave está asignada a la puerta de embarque.
 */
void Aeronave::asignarPuertaDeEmbarque(int puerta, int cod, const string &hora)
{
    cout << marca << " se dirige a la puerta de embarque: " << puerta << " Para el vuelo #" << cod << " Hora: " << hora << endl;
    puerta_de_embarque = puerta;
}

/**
 * La función "agregarVuelo" añade un vuelo a un vector de vuelos si el estado de la aeronave es verdadero y
 * el vuelo aún no está en el vector.
 *
 * @param v Un puntero a un objeto de tipo Vuelos.
 */
void Aeronave::agregarVuelo(Vuelos *v)
{
    bool flag = estado;

    for (int i = 0; i < vuelos.size() && flag; i++)
    {
        if (v->identificacion == vuelos[i]->identificacion)
            flag = false;
    }
    if (vuelos.size() < 3 && flag)
        vuelos.push_back(v);
    else
        estado = false;
    if (vuelos.size() == 3)
        estado = false;
}

/**
 * La función "printInfo" imprime la marca y capacidad de una aeronave.
 */
void Aeronave::printInfo()
{
    cout << "Marca: " << marca << endl
         << "Capacidad: " << capacidad << endl;
}

/**
 * La función "getCapacidad" devuelve la capacidad de una aeronave.
 *
 * @return La capacidad del avión.
 */
int Aeronave::getCapacidad()
{
    return this->capacidad;
}

/**
 * La función establece el valor de la variable "modelo" en la clase Aeronave.
 *
 * @param s El parámetro "s" es una cadena que representa el modelo de la aeronave.
 */
void Aeronave::setModelo(const string s)
{
    this->modelo = s;
}

/**
 * La función establece el nombre de una aeronave.
 *
 * @param s El parámetro "s" es una cadena que representa el nuevo nombre de la aeronave.
 */
void Aeronave::setNombre(const string s)
{
    this->nombre = s;
}

/**
 * La función establece el valor de la variable "autonomia" en la clase Aeronave.
 *
 * @param i El parámetro "i" es un valor entero que representa el nuevo valor para la "autonomía"
 * atributo del objeto Aeronave.
 */
void Aeronave::setAutonomia(int i)
{
    this->autonomia = i;
}

/**
 * La función establece el año de fabricación de un objeto aeronáutico.
 *
 * @param i El parámetro "i" es un valor entero que representa el año de fabricación de un
 * avión.
 */
void Aeronave::setFabricacion(int i)
{
    this->fabricacion = i;
}

/**
 * La función establece la velocidad máxima de un avión.
 *
 * @param i El parámetro "i" es un valor entero que representa la velocidad máxima de una aeronave.
 */
void Aeronave::setVelMax(int i)
{
    this->velMax = i;
}

/**
 * La función establece el número de asientos disponibles para un avión.
 *
 * @param i El parámetro "i" es un valor entero que representa el número de asientos disponibles en el
 * avión.
 */
void Aeronave::setSillasDispo(int i)
{
    this->sillasDispo = i;
}

/**
 * La función establece el estado de una aeronave.
 *
 * @param b El parámetro "b" es un valor booleano que representa el estado de la aeronave. Esta usado
 * para establecer el estado de la aeronave en verdadero o falso.
 */
void Aeronave::setEstado(bool b)
{
    this->estado = b;
}

/**
 * La función "getMarca" devuelve el valor del atributo "marca" de un objeto de la clase
 * "Aeronave".
 *
 * @return La función `getMarca()` devuelve el valor de la variable miembro `marca` del
 * Clase `Aeronave`.
 */
string Aeronave::getMarca()
{
    return this->marca;
}

/**
 * La función getModelo() devuelve el modelo de una aeronave.
 *
 * @return el valor de la variable "modelo".
 */
string Aeronave::getModelo()
{
    return this->modelo;
}

/**
 * La función "getNombre" devuelve el nombre de la aeronave.
 *
 * @return el valor de la variable "nombre".
 */
string Aeronave::getNombre()
{
    return this->nombre;
}

/**
 * La función "getAutonomia" devuelve el valor de la variable "autonomia" en la clase Aeronave.
 *
 * @return El método devuelve el valor de la variable "autonomia".
 */
int Aeronave::getAutonomia()
{
    return this->autonomia;
}

/**
 * La función "getFabricacion" devuelve el valor de la variable "fabricacion" en la clase Aeronave.
 *
 * @return el valor de la variable miembro "fabricacion" del objeto.
 */
int Aeronave::getFabricacion()
{
    return this->fabricacion;
}

/**
 * La función "getVelMax" devuelve la velocidad máxima de una aeronave.
 *
 * @return el valor de la variable miembro "velMax" del objeto.
 */
int Aeronave::getVelMax()
{
    return this->velMax;
}

/**
 * La función getSillasDispo devuelve el número de asientos disponibles en un avión.
 *
 * @return El método `getSillasDispo` devuelve el valor de la variable `sillasDispo`.
 */
int Aeronave::getSillasDispo()
{
    return this->sillasDispo;
}

/**
 * La función "getEstado" devuelve el estado de una aeronave.
 *
 * @return el valor de la variable "estado" del objeto "Aeronave".
 */
bool Aeronave::getEstado()
{
    return this->estado;
}