#ifndef AEROPUERTO
#define AEROPUERTO

#include <iostream>
#include <vector>
#include "torreControl.h"
#include "jet.h"
#include "helicoptero.h"
#include "avion.h"
#include "pasajero.h"

using namespace std;

class Aeropuerto
{
private:
    static Aeropuerto *instancia; // Instancia única del aeropuerto
    vector<Vuelos *> vuelos;
    // Constructor privado para evitar instancias externas
    Aeropuerto();

public:
    static Aeropuerto &obtenerInstancia();

    TorreControl torreControl;

    void agregarDestino(Vuelos *v);
    void printDestinos();
    bool disponibilidadVuelos();
    bool disponibilidadAeronaves();
    void asignarVuelo();
    Vuelos *obtenerVuelo(int pos);
};

#endif