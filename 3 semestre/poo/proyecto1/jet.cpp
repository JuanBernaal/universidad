#include "jet.h"

/**
 * El constructor JetPrivado inicializa el objeto JetPrivado con la marca, capacidad y
 *mediador.
 *
 * @param marca Una cadena que representa la marca o marca del jet privado.
 * @param capacidad El parámetro "capacidad" representa el número máximo de pasajeros que el
 * Se puede acomodar jet privado.
 * @param mediator El parámetro "mediador" es un puntero a un objeto de tipo "MediadorTrafico". Es
 * utilizado para establecer comunicación entre el objeto JetPrivado y el mediador de tráfico.
 */
JetPrivado::JetPrivado(const string &marca, int capacidad, MediadorTrafico *mediator) : Aeronave(marca, capacidad, mediator)
{
    propietario = "";
    listaServicios.clear();
    listaDestinos.clear();
    this->marca = marca;
    this->capacidad = capacidad;
}

/**
 * La función "getPropietario" devuelve el propietario de un jet privado.
 *
 * @return el valor de la variable "propietario", que es una cadena.
 */
string JetPrivado::getPropietario()
{
    return this->propietario;
}

/**
 * La función "printInfo" en la clase "JetPrivado" llama a la función "printInfo" desde la base
 * clase "Aeronave".
 */
void JetPrivado::printInfo()
{
    Aeronave::printInfo();
}

/**
 * La función "obtenerDatos" solicita al usuario ingresar el nombre del propietario de un jet privado y
 * lo almacena en la variable "propietario".
 */
void JetPrivado::obtenerDatos()
{
    try {
        cout << "Ingrese el nombre del propietario: ";
        cin >> this->propietario;
        cout << endl;
    } catch (const exception& e) {
        cerr << "Error: " << e.what() << endl;
    }
}

