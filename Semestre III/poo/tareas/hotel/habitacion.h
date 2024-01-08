#ifndef Habitacion_h
#define Habitacion_h

#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>

using namespace std;

class Habitacion
{
private:
    int precio;        // Precio de la habitación
    bool estado;       // Estado de ocupación de la habitación true = ocupada, false = desocupada
    int numeroHab;     // Número de la habitación
    string nombreHuesp; // Nombre del huésped actual (si la habitación está ocupada)

public:
    // Constructor: Crea una habitación con un número específico (n).
    // Asigna un precio aleatorio entre 100 y 600 a la habitación.
    // Inicializa la habitación como desocupada y sin huésped.
    Habitacion(int n);

    // Marca la habitación como ocupada.
    void setOcupado();

    // Marca la habitación como desocupada.
    void setDesocupado();

    // Asigna el nombre del huésped actual a la habitación.
    void setHuesped(string &n);

    // Obtiene el precio de la habitación.
    int getPrecio();

    // Obtiene el estado de ocupación de la habitación.
    bool getEstado();

    // Obtiene el número de la habitación.
    int getNumero();

    // Obtiene el nombre del huésped actual en la habitación (si está ocupada).
    string getHuesped();
};

#endif 
