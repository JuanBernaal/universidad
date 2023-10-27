#include "huesped.h"  // Incluye la definición de la clase Huesped

Huesped::Huesped(){   // COnstructor por defecto
}

Huesped::Huesped(string &n, int t)
{
    nombre = n;                              // Asigna el nombre del huésped
    dinero = rand() % 501 + 500;             // Asigna un valor aleatorio entre 500 y 1000 al atributo "dinero"
    tel = t;                                 // Asigna el número de teléfono del huésped
}

void Huesped::setTel(int n)
{
    tel = n;                                 // Asigna el número de teléfono
}

void Huesped::setDinero(int n)
{
    dinero = n;                              // Asigna la cantidad de dinero
}

string Huesped::getName()
{
     return nombre;                           // Retorna el nombre del huésped
}

int Huesped::getTel()
{
    return tel;                              // Retorna el número de teléfono
}

int Huesped::getDinero()
{
    return dinero;                           // Retorna la cantidad de dinero
}

void Huesped::checkOutHuesped()
{
    nombre = "";                             // Borra el nombre del huésped
    dinero = 0;                              // Establece el dinero en cero
    tel = 0;                                 // Establece el número de teléfono en cero
}
