#include "aeropuerto.h"

/**
 * El constructor Aeropuerto inicializa la variable vuelos como una lista vacía.
 */
Aeropuerto::Aeropuerto()
{
    vuelos = {};
}

/**
 * La función "agregarDestino" agrega un destino de vuelo a la lista de vuelos de un aeropuerto.
 *
 * @param v El parámetro "v" es un puntero a un objeto de tipo "Vuelos".
 */
void Aeropuerto::agregarDestino(Vuelos *v)
{
    vuelos.push_back(v);
}

/**
 * La función "printDestinos" imprime el detalle de todos los vuelos en el vector "vuelos".
 */
void Aeropuerto::printDestinos()
{
    if (vuelos.size() == 0)
        printf("No hay vuelos\n");
    else
    {
        for (int i = 0; i < vuelos.size(); i++)
        {
            cout << i + 1 << "." << endl;
            vuelos[i]->printVuelo();
        }
    }
}


Aeropuerto *Aeropuerto::instancia = nullptr;

/**
 * La función "obtenerInstancia" devuelve una referencia a la instancia singleton del "Aeropuerto"
 * clase.
 *
 * @return una instancia de la clase "Aeropuerto".
 */
Aeropuerto &Aeropuerto::obtenerInstancia()
{
    if (!instancia)
    {
        instancia = new Aeropuerto();
    }
    return *instancia;
}

/**
 * La función comprueba si hay vuelos disponibles en el aeropuerto.
 *
 * @return un valor booleano. Si el tamaño del vector "vuelos" es 0 devolverá falso. De lo contrario,
 * volverá verdadero.
 */
bool Aeropuerto::disponibilidadVuelos()
{
    if (vuelos.size() == 0)
        return false;
    else
        return true;
}

/**
 * La función "disponibilidadAeronaves" comprueba la disponibilidad de aeronaves en el control del aeropuerto
 * torre.
 *
 * @return un valor booleano.
 */
bool Aeropuerto::disponibilidadAeronaves()
{
    return torreControl.disponibilidadNaves();
}

/**
 * La función "asignarVuelo" itera a través de una lista de vuelos y selecciona una aeronave para cada uno
 * vuelo utilizando la función "seleccionarAeronave" del objeto "torreControl".
 */
void Aeropuerto::asignarVuelo()
{
    for (int i = 0; i < vuelos.size(); i++)
    {
        torreControl.seleccionarAeronave(vuelos[i]);
    }
}

/**
 * La función "obtenerVuelo" devuelve un puntero a un objeto "Vuelos" en una posición determinada.
 *
 * @param pos El parámetro "pos" es un número entero que representa la posición del vuelo en la matriz
 * de vuelos.
 *
 * @return un objeto de vuelo de la matriz "vuelos" en la posición especificada "pos".
 */
Vuelos *Aeropuerto::obtenerVuelo(int pos)
{
    return vuelos[pos];
}
