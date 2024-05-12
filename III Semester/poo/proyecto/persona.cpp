#include "persona.h"

Persona::Persona()
{
}

/**
 * La función "Persona" es un constructor que inicializa los atributos de un objeto persona.
 *
 * @param nombre El nombre de la persona.
 * @param apellido El parámetro "apellido" representa el apellido o apellido de la persona.
 * @param edad El parámetro "edad" representa la edad de la persona.
 * @param cedula El parámetro "cédula" hace referencia al número de identificación o número de cédula de la persona.
 * Generalmente es un número único asignado a individuos por el gobierno o las autoridades pertinentes.
 *para fines de identificación.
 * @param fechaNacimiento El parámetro "fechaNacimiento" representa la fecha de nacimiento de la persona.
 * @param genero El parámetro "genero" representa el género de la persona. Puede ser un valor de cadena
 * indicando el género, como "masculino" o "femenino".
 * @param direccion El parámetro "direccion" representa la dirección o ubicación de la persona. Es
 * una cadena que almacena la información de la dirección, como el nombre de la calle, el número de la casa, la ciudad y el país.
 * @param numTel El parámetro "numTel" representa el número de teléfono de la persona.
 * @param correo El parámetro "correo" es una cadena que representa la dirección de correo electrónico de la persona.
 */
Persona::Persona(const string &nombre, string &apellido, int edad, string &cedula, string &fechaNacimiento, string &genero, string &direccion, string &numTel, string &correo)
{
    this->nombre = nombre;
    this->apellido = apellido;
    this->edad = edad;
    this->cedula = cedula;
    this->fechaNacimiento = fechaNacimiento;
    this->genero = genero;
    this->direccion = direccion;
    this->numTel = numTel;
    this->correo = correo;
}

/**
 * La función "getNombre" devuelve el valor de la variable "nombre" en la clase "Persona".
 *
 * @return el valor de la variable "nombre", que es una cadena.
 */
string Persona::getNombre()
{
    return this->nombre;
}

/**
 * La función "getEdad" devuelve el valor de la variable miembro "edad" de la clase Persona.
 *
 * @return el valor de la variable "edad" del objeto de la clase "Persona".
 */
int Persona::getEdad()
{
    return this->edad;
}

/**
 * La función "getInformacion" imprime la información personal de una persona.
 */
void Persona::getInformacion()
{
    cout << "Nombre: " << nombre << endl;
    cout << "Apellido: " << apellido << endl;
    cout << "Edad: " << edad << " years" << endl;
    cout << "Cedula: " << cedula << endl;
    cout << "Fecha de Nacimiento: " << fechaNacimiento << endl;
    cout << "Genero: " << genero << endl;
    cout << "Direccion: " << direccion << endl;
    cout << "Numero de Telefono: " << numTel << endl;
    cout << "Correo Electronico: " << correo << endl;
}
