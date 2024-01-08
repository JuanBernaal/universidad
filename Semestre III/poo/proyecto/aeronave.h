#ifndef AERONAVE
#define AERONAVE

#include <iostream>
#include <vector>
#include "vuelos.h"
#include "mediadorTrafico.h"
#include "puertaEmbarque.h"
class Helicoptero;
class Avion;
class JetPrivado;

using namespace std;
class MediatorDeTrafico; // Declaración previa de MediatorDeTrafico
class Vuelos;

class Aeronave
{
private:
    MediadorTrafico *mediador;
    string puerta_de_embarque;

    void enviarMensaje(const string &mensaje);

public:
    string marca, modelo, nombre;
    int capacidad, autonomia, fabricacion, velMax, sillasDispo, id;
    vector<Vuelos *> vuelos;
    bool estado;

    Aeronave();
    Aeronave(const string &marca, int capacidad, MediadorTrafico *mediator);
    void despegar();

    void aterrizar();

    void actualizarPosicion(const string &mensaje);

    void recibirMensaje(const string &mensaje);

    void asignarPuertaDeEmbarque(int puerta, int cod, const string &hora);

    void agregarVuelo(Vuelos *v);

    virtual void printInfo();

    virtual void obtenerDatos() = 0;

    void eliminarVuelo();

    bool tieneVuelos();

    int getCapacidad();

    void setModelo(const string s);

    void setNombre(const string s);

    void setAutonomia(int i);

    void setFabricacion(int i);

    void setVelMax(int i);

    void setSillasDispo(int i);

    void setEstado(bool b);

    string getMarca();

    string getModelo();

    string getNombre();

    int getAutonomia();

    int getFabricacion();

    int getVelMax();

    int getSillasDispo();

    bool getEstado();
};

#endif