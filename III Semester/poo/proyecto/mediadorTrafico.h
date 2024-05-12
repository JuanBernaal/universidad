#ifndef MEDIADOR_TRAFICO
#define MEDIADOR_TRAFICO

#include <iostream>

using namespace std;
class Aeronave; // Declaración previa de Aeronave

class MediadorTrafico
{
public:
    virtual void registrarAeronave(Aeronave *aeronave) = 0;
    virtual void enviarMensaje(const string &mensaje, Aeronave *emisor) = 0;
    virtual void asignarPuertaDeEmbarque(Aeronave *aeronave, int puerta, int cod, const string &hora) = 0;
};

#endif