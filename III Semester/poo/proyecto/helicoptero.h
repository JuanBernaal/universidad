#ifndef HELICOPTERO
#define HELICOPTERO

#include <iostream>
#include "aeronave.h"
using namespace std;

class Aeronave;

class Helicoptero : public Aeronave
{
private:
    int numRotores, maxElevacion;
    string uso;

public:
    Helicoptero(const string &marca, int capacidad, MediadorTrafico *mediator);
    int getNumRotores();
    int getMaxElevacion();
    string getUso();

    void printInfo() override;

    void obtenerDatos() override;
};

#endif