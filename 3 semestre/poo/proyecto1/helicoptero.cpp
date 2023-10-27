#include "helicoptero.h"
#include <limits>
/**
 * Este es el constructor de la clase Helicóptero, que toma como marca, capacidad y mediador.
 * parámetros.
 *
 * @param marca El parámetro "marca" es una cadena que representa la marca o fabricante del
 * helicóptero.
 * @param capacidad El parámetro "capacidad" representa el número máximo de pasajeros o el
 * capacidad máxima de peso del helicóptero. Determina el número máximo de personas o cantidad de
 * carga que puede transportar el helicóptero.
 * @param mediator El parámetro "mediador" es un puntero a un objeto de tipo "MediadorTrafico". Es
 * utilizado para establecer comunicación entre el objeto helicóptero y el objeto mediador de tráfico.
 */
Helicoptero::Helicoptero(const string &marca, int capacidad, MediadorTrafico *mediator) : Aeronave(marca, capacidad, mediator)
{
}

/**
 * La función "getNumRotores" devuelve el número de rotores de un helicóptero.
 *
 * @return El número de rotores del helicóptero.
 */
int Helicoptero::getNumRotores()
{
    return this->numRotores;
}
/**
 * La función getMaxElevacion devuelve la elevación máxima de un helicóptero.
 *
 * @return La elevación máxima del helicóptero.
 */
int Helicoptero::getMaxElevacion()
{
    return this->maxElevacion;
}
/**
 * La función "getUso" devuelve el valor de la variable "uso" en la clase "Helicoptero".
 *
 * @return el valor de la variable "uso", que es una cadena.
 */
string Helicoptero::getUso()
{
    return this->uso;
}

/**
 * La función "printInfo" en la clase "Helicoptero" llama a la función "printInfo" en la clase "Aeronave"
 * clase.
 */
void Helicoptero::printInfo()
{
    Aeronave::printInfo();
}

/**
 * La función "obtenerDatos" solicita al usuario ingresar el número de rotores, elevación máxima y
 * tipo de uso de un objeto helicóptero.
 */
void Helicoptero::obtenerDatos()
{
    try {
        cout << "Ingrese el numero de rotores: ";
        cin >> this->numRotores;
        if (cin.fail()) {
            cin.clear(); 
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); 
            throw invalid_argument("Entrada no valida para numero de rotores.");
        }
        
        cout << endl;
        cout << "Ingrese la maxima elevacion: ";
        cin >> this->maxElevacion;
        if (cin.fail()) {
            cin.clear(); // Restaurar el estado de cin
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); 
            throw invalid_argument("Entrada no valida para maxima elevacion.");
        }
        
        cout << endl;
        cout << "Ingrese el tipo de uso: ";
        cin >> this->uso;
        cout << endl;
    } catch (const invalid_argument& e) {
        cerr << "Error: " << e.what() << endl;
    }
}
