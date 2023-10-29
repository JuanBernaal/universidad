#ifndef VUELOS
#define VUELOS

#include <iostream>

#include "tripulante.h"
#include "pasajero.h"
#include <vector>
using namespace std;

class Persona;
class Tripulante;

class Vuelos
{
public:
    int identificacion, capacidad, numPasajeros;
    string fecha, ciudadOrigen, ciudadDestino, hora;
    vector<Tripulante> tripulantes;
    bool estado;

    Vuelos();
    Vuelos(int id, const string &fecha, const string &ciudadDestino, const string &hora);

    void agregarPasajero();

    void printVuelo();

    bool disponible();

    // void obtenerDatosVuelo();
};

#endif