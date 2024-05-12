#include "avion.h"
#include <limits>
/**
 * El constructor Avion inicializa un objeto Avion con una marca, capacidad y mediador determinados.
 *
 * @param marca El parámetro "marca" es una cadena que representa la marca o marca del avión. Él
 * se pasa por referencia al constructor de la clase Avion.
 * @param capacidad El parámetro "capacidad" representa la capacidad de la aeronave, que es un
 * valor entero que indica el número máximo de pasajeros o carga que puede transportar la aeronave.
 * @param mediator El parámetro "mediador" es un puntero a un objeto de tipo "MediadorTrafico". Es
 * utilizado para establecer comunicación entre el objeto "Avion" y el objeto "MediadorTrafico". Este
 * permite que el objeto "Avion" interactúe con el tráfico
 */
Avion::Avion(const string &marca, int capacidad, MediadorTrafico *mediator) : Aeronave(marca, capacidad, mediator)
{
}

/**
 * La función "getAltitudMax" devuelve la altitud máxima de un avión.
 *
 * @return el valor de la variable miembro "altitudMax".
 */
int Avion::getAltitudMax()
{
    return this->altitudMax;
}

/**
 * La función "getCategoria" devuelve el valor de la variable miembro "categoria".
 *
 * @return el valor de la variable "categoria" en el objeto Avion.
 */
int Avion::getCategoria()
{
    return this->categoria;
}

/**
 * La función "getNumMotores" devuelve el número de motores de un objeto Avion.
 *
 * @return El número de motores del objeto Avion.
 */
int Avion::getNumMotores()
{
    return this->numMotores;
}

/**
 * La función "printInfo" en la clase "Avion" llama a la función "printInfo" en la clase "Aeronave"
 * clase.
 */
void Avion::printInfo()
{
    Aeronave::printInfo();
}
/**
 * La función "obtenerDatos" solicita al usuario ingresar el número de motores, categoría y máximo
 * altitud de un avión.
 */
void Avion::obtenerDatos()
{
    try
    {
        cout << "Ingrese el numero de motores: ";
        cin >> this->numMotores;
        if(cin.fail()) 
        {
            throw runtime_error("Entrada no valida. Debe ingresar un numero entero.");
        }
        cout << endl;

        cout << "Ingrese la categoria: ";
        cin >> this->categoria;
        if(cin.fail())  
        {
            throw runtime_error("Entrada no valida. Debe ingresar un numero entero.");
        }
        cout << endl;

        cout << "Ingrese la altitud maxima: ";
        cin >> this->altitudMax;
        if (cin.fail()) 
        {
            throw runtime_error("Entrada no valida. Debe ingresar un número entero.");
        }
        cout << endl;
    }
    catch (const runtime_error &e)
    {
        cerr << "Error: " << e.what() << endl;
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }
}

