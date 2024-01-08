#ifndef AVION
#define AVION

#include <iostream>
#include "aeronave.h"
using namespace std;

class Aeronave;

class Avion : public Aeronave
{
private:
    int altitudMax, numMotores, categoria;

public:
    Avion(const string &marca, int capacidad, MediadorTrafico *mediator);
    int getAltitudMax(), getNumMotores(), getCategoria();
    void printInfo() override;
    void obtenerDatos() override;
};

#endif