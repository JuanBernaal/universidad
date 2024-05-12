#ifndef Huesped_H
#define Huesped_H

#include <iostream>
#include <vector>
#include <list>

using namespace std;

class Huesped
{
private:
    string nombre;  // Nombre del huesped.
    int tel;        // Numero telefonico del huesped.
    int dinero;     // Dinero disponible del huesped.

public:
    Huesped();      // Constructor predeterminado.
    Huesped(string &n, int t); // Constructor con parametros.
    void setDinero(int n); // Establece el dinero disponible del huesped.
    void setTel(int n); // Establece el numero telefonico del huesped.
    string getName(); // Obtiene el nombre del huesped.
    int getTel(); // Obtiene el numero telefonico del huesped.
    int getDinero(); // Obtiene el dinero disponible del huesped.
    void checkOutHuesped(); // Realiza el checkout del huesped, reiniciando los atributos del huesped.
};

#endif
