#ifndef Hotel_H
#define Hotel_H

#include <iostream>
#include <vector>
#include <list>
#include "habitacion.h"  // Incluye la definición de la clase Habitacion
#include "huesped.h"     // Incluye la definición de la clase Huesped

using namespace std;

class Hotel{

    private:
        string nombre;                    // Nombre del hotel
        vector<Habitacion> habitaciones;  // Vector de objetos Habitacion para almacenar las habitaciones del hotel
        vector<Huesped> huespedes;        // Vector de objetos Huesped para almacenar los huéspedes del hotel

    public:
        Hotel();                          // Constructor que inicializa el hotel con 10 habitaciones vacías
        void setNombre(string &n);        // Asigna el nombre del hotel
        void printInfoHotel();            // Imprime la información de todas las habitaciones del hotel
        void reserva();                   // Realiza el proceso de reserva de una habitación para un huésped
        void checkOut();                  // Realiza el proceso de check-out de un huésped de una habitación
    };

#endif
