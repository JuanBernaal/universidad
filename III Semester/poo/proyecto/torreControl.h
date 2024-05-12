#ifndef TORRE_CONTROL
#define TORRE_CONTROL

#include <iostream>
#include <cstdlib> // Necesario para la función rand
#include <ctime>   // Necesario para la función time
#include "mediadorTrafico.h"
#include "puertaEmbarque.h"
#include "aeronave.h"
using namespace std;

class MediatorDeTrafico; // Declaración previa de MediatorDeTrafico
class Aeronave;          // Declaración previa de Aeronave
class PuertaEmbarque;

class TorreControl : public MediadorTrafico
{
private:
    vector<Aeronave *> aeronaves;
    vector<Aeronave *> aviones;
    vector<PuertaEmbarque> puertas;

public:
    TorreControl();

    void registrarAeronave(Aeronave *aeronave) override;

    void enviarMensaje(const string &mensaje, Aeronave *emisor) override;

    void asignarPuertaDeEmbarque(Aeronave *aeronave, int puerta, int cod, const string &hora) override;

    bool disponibilidadNaves();

    void registrarAvion(Aeronave *aeronave);

    void mostrarAviones();

    void seleccionarAeronave(Vuelos *v);

    void simulacion();

    void mostrarPuertas();
};

#endif