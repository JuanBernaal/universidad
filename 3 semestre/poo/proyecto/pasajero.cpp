#include "pasajero.h"
Pasajero::Pasajero() {}

/**
 * El constructor Pasajero inicializa un objeto Pasajero con los parámetros dados.
 *
 * @param nombre El nombre del pasajero.
 * @param apellido El parámetro "apellido" es una cadena que representa el apellido del pasajero.
 * @param edad edad es un número entero que representa la edad del pasajero.
 * @param cedula El parámetro "cédula" se refiere al número de identificación o número de cédula del
 * pasajero.
 * @param fechaNacimiento El parámetro "fechaNacimiento" representa la fecha de nacimiento del
 * pasajero.
 * @param genero El parámetro "genero" representa el sexo del pasajero.
 * @param direccion El parámetro "direccion" representa la dirección del pasajero.
 * @param numTel El parámetro "numTel" representa el número de teléfono del pasajero.
 * @param correo correo es una cadena que representa la dirección de correo electrónico del pasajero.
 * @param nacionalidad El parámetro "nacionalidad" representa la nacionalidad del pasajero.
 * @param infoMedica El parámetro "infoMedica" es una cadena que representa la información médica de
 * el pasajero. Puede incluir detalles como alergias, condiciones médicas o cualquier otra información relevante.
 * información médica que puede ser importante que la aerolínea o el personal médico conozcan.
 * @param numMaletasBodega El número de maletas que tiene el pasajero en la bodega de carga.
 */
Pasajero::Pasajero(const string &nombre, string &apellido, int edad, string &cedula, string &fechaNacimiento, string &genero, string &direccion, string &numTel, string &correo, string &nacionalidad, string &infoMedica, int numMaletasBodega)
    : Persona(nombre, apellido, edad, cedula, fechaNacimiento, genero, direccion, numTel, correo)
{
    this->numMaletasBodega = numMaletasBodega;
    this->nacionalidad = nacionalidad;
    this->infoMedica = infoMedica;
}
/**
 * La función "obtenerDatosPasajero" solicita al usuario ingresar varios detalles sobre un pasajero y
 * devuelve un objeto "Pasajero" con la información ingresada.
 *
 * @return un objeto de tipo "Pasajero".
 */
Pasajero Pasajero::obtenerDatosPasajero()
{
    string nombre, apellido, cedula, fechaNacimiento, genero, direccion, numTel, correo, nacionalidad, infoMedica;
    int edad, numMaletasBodega;
    cin.ignore();
    cout << "Ingrese el nombre del pasajero: ";
    getline(cin, nombre);

    cout << "Ingrese el apellido del pasajero: ";
    getline(cin, apellido);

    cout << "Ingrese la edad del pasajero: ";
    cin >> edad;

    cin.ignore(); // Limpiar el buffer de entrada

    cout << "Ingrese la cedula del pasajero: ";
    getline(cin, cedula);

    cout << "Ingrese la fecha de nacimiento del pasajero: ";
    getline(cin, fechaNacimiento);

    cout << "Ingrese el genero del pasajero: ";
    getline(cin, genero);

    cout << "Ingrese la direccion del pasajero: ";
    getline(cin, direccion);

    cout << "Ingrese el numero de telefono del pasajero: ";
    getline(cin, numTel);

    cout << "Ingrese el correo del pasajero: ";
    getline(cin, correo);

    cout << "Ingrese la nacionalidad del pasajero: ";
    getline(cin, nacionalidad);

    cout << "Ingrese la informacion medica del pasajero: ";
    getline(cin, infoMedica);

    cout << "Ingrese el numero de maletas de bodega del pasajero: ";
    cin >> numMaletasBodega;

    Pasajero pasajero(nombre, apellido, edad, cedula, fechaNacimiento, genero, direccion, numTel, correo, nacionalidad, infoMedica, numMaletasBodega);
    *this = pasajero;
    return pasajero;
}

/**
 * La función "getNumMaletas" devuelve el número de maletas que tiene un pasajero en la bodega de carga.
 *
 * @return el valor de la variable miembro "numMaletasBodega" del objeto.
 */
int Pasajero::getNumMaletas()
{
    return this->numMaletasBodega;
}

/**
 * La función "asignarVuelo" asigna un vuelo a un pasajero si el vuelo está disponible.
 *
 * @param v Un puntero a un objeto de tipo "Vuelos".
 */
void Pasajero::asignarVuelo(Vuelos *v)
{
    if (v->disponible())
    {
        vuelo = v;
        printf("El vuelo se asigno de manera correcta\n");
    }
    else
        printf("El vuelo no se encuentra disponible\n");
}

/**
 * La función "getInformacion" imprime la información de un pasajero, incluyendo su número de
 * maletas en bodega de carga, nacionalidad e información médica.
 */
void Pasajero::getInformacion()
{
    Persona::getInformacion();
    cout << "Numero de Maletas en Bodega: " << numMaletasBodega << endl;
    cout << "Nacionalidad: " << nacionalidad << endl;
    cout << "Informacion Medica: " << infoMedica << endl;
}
