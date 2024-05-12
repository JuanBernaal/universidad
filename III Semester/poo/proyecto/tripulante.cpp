#include "tripulante.h"

/**
 * El constructor Tripulante inicializa el objeto Tripulante con los parámetros dados.
 *
 * @param nombre El nombre del tripulante.
 * @param apellido El parámetro "apellido" es una cadena que representa el apellido de la tripulación
 * miembro.
 * @param edad El parámetro "edad" representa la edad del "Tripulante" (tripulante).
 * @param cedula El parámetro cedula es una cadena que representa el número de identificación de la tripulación
 * miembro.
 * @param fechaNacimiento El parámetro "fechaNacimiento" representa la fecha de nacimiento del
 * Objeto "Tripulante".
 * @param genero género del tripulante
 * @param direccion El parámetro "direccion" es una cadena que representa la dirección de la tripulación
 * miembro.
 * @param numTel El parámetro "numTel" representa el número de teléfono del miembro de la tripulación.
 * @param correo El parámetro "correo" es una cadena que representa la dirección de correo electrónico del equipo
 * miembro.
 * @param cargo El parámetro "cargo" representa el puesto de trabajo o rol del miembro de la tripulación. Podria
 * ser algo así como "capitán", "ingeniero", "navegante", etc.
 * @param xp El parámetro "xp" representa el nivel de experiencia del miembro de la tripulación. es un numero entero
 *valor que indica el número de años de experiencia que tienen en su ramo.
 * @param hrsDiarias El parámetro "hrsDiarias" representa el número de horas que trabaja el tripulante
 * por día.
 */
Tripulante::Tripulante(string &nombre, string &apellido, int edad, string &cedula, string &fechaNacimiento, string &genero, string &direccion, string &numTel, string &correo, string &cargo, int xp, int hrsDiarias)
    : Persona(nombre, apellido, edad, cedula, fechaNacimiento, genero, direccion, numTel, correo)
{
    this->cargo = cargo;
    this->xp = xp;
    this->hrsDiarias = hrsDiarias;
}

/**
 * La función "getInformacion" imprime la información de un tripulante, incluyendo su carga,
 *años de experiencia, y horario diario.
 */
void Tripulante::getInformacion()
{
    Persona::getInformacion();
    cout << "Cargo en el avion: " << cargo << endl;
    cout << "Años de experiencia: " << xp << endl;
    cout << "Horas diarias: " << hrsDiarias << endl;
}