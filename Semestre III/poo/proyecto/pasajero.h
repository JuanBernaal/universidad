#ifndef PASAJERO
#define PASAJERO

#include <iostream>
#include "persona.h"
#include "vuelos.h"

using namespace std;

class Vuelos;

class Pasajero : public Persona
{
private:
    string nacionalidad, infoMedica;
    int numMaletasBodega;
    Vuelos *vuelo;

public:
    Pasajero();
    Pasajero(const string &nombre, string &apellido, int edad, string &cedula, string &fechaNacimiento, string &genero, string &direccion, string &numTel, string &correo, string &nacionalidad, string &infoMedica, int NumMaletasBodega);
    int getNumMaletas();

    void asignarVuelo(Vuelos *v);
    Pasajero obtenerDatosPasajero();
    void getInformacion() override;
};

#endif