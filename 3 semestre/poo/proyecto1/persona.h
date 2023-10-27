#ifndef PERSONA
#define PERSONA

#include <iostream>
using namespace std;

class Persona
{
private:
    string nombre, apellido, cedula, fechaNacimiento, genero, direccion, numTel, correo;
    int edad;

public:
    Persona();
    Persona(const string &nombre, string &apellido, int edad, string &cedula, string &fechaNacimiento, string &genero, string &direccion, string &numTel, string &correo);
    string getNombre();
    int getEdad();
    virtual void getInformacion();
};

#endif