#include "habitacion.h"

Habitacion::Habitacion(int n)
{
    precio = rand() % 501 + 100; // Genera un número aleatorio entre 100 y 600
    estado = false;              // Inicializa la habitación como desocupada
    numeroHab = n;               // Asigna el número de habitación especificado
    nombreHuesp = "";            // Inicializa el nombre del huésped como una cadena vacía
}

// Marca la habitación como ocupada.
void Habitacion::setOcupado()
{
    estado = true;
}

// Marca la habitación como desocupada.
void Habitacion::setDesocupado()
{
    estado = false;
}

// Asigna el nombre del huésped actual a la habitación.
void Habitacion::setHuesped(string &n)
{
    nombreHuesp = n;
}

// Obtiene el precio de la habitación.
int Habitacion::getPrecio()
{
    return precio;
}

// Obtiene el estado de ocupación de la habitación.
bool Habitacion::getEstado()
{
    return estado;
}

// Obtiene el número de la habitación.
int Habitacion::getNumero()
{
    return numeroHab;
}
