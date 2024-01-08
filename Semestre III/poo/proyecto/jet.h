#ifndef JET
#define JET

#include <iostream>
#include "aeronave.h"
using namespace std;

class Aeronave;

class JetPrivado : public Aeronave
{
private:
    string propietario;
    vector<string> listaServicios, listaDestinos;

public:
    JetPrivado(const string &marca, int capacidad, MediadorTrafico *mediator);
    string getPropietario();
    void printInfo() override;
    void obtenerDatos() override;
};

#endif