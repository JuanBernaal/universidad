#ifndef TRIPULANTE
#define TRIPULANTE

#include <iostream>
#include "persona.h"
using namespace std;

class Tripulante : public Persona
{
private:
    string cargo;
    int xp, hrsDiarias;

public:
    Tripulante(string &nombre, string &apellido, int edad, string &cedula, string &fechaNacimiento, string &genero, string &direccion, string &numTel, string &correo, string &cargo, int xp, int hrsDiarias);

    void getInformacion() override;
};

#endif