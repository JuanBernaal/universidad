#include "vuelos.h"

/**
 * El constructor de Vuelos inicializa la variable ciudadOrigen a Colombia y la variable estado a
 * verdadero.
 */
Vuelos::Vuelos()
{
    ciudadOrigen = "CLO";
    estado = true;
}

/**
 * El constructor Vuelos inicializa el objeto Vuelos con los parámetros dados.
 *
 * @param id El parámetro id es un número entero que representa la identificación del vuelo.
 * @param fecha El parámetro "fecha" es una cadena que representa la fecha del vuelo.
 * @param ciudadDestino El parámetro "ciudadDestino" representa la ciudad de destino del vuelo.
 * @param hora El parámetro "hora" representa la hora del vuelo.
 */
Vuelos::Vuelos(int id, const string &fecha, const string &ciudadDestino, const string &hora)
    : identificacion(id), fecha(fecha),
      ciudadDestino(ciudadDestino), hora(hora),
      numPasajeros(0)
{
    ciudadOrigen = "CLO";
    estado = true;
}

/**
 * La función "agregarPasajero" agrega un pasajero a un vuelo si aún hay capacidad, en caso contrario
 * imprime "Vuelo lleno" (Vuelo lleno).
 */
void Vuelos::agregarPasajero()
{
    if (numPasajeros < capacidad)
        numPasajeros++;
    else
        printf("Vuelo lleno\n");
    if (numPasajeros == capacidad)
        estado = false;
}

/**
 * La función "printVuelo" imprime los detalles de un vuelo, incluyendo la fecha, hora, ciudad de origen y
 * Ciudad de destino.
 */
void Vuelos::printVuelo()
{
    cout << "Fecha: " << fecha << endl
         << "Hora " << hora << endl
         << "Ciudad de origen: " << ciudadOrigen << endl
         << "Ciudad de destino " << ciudadDestino << endl;
}

/**
 * La función "disponible" devuelve el valor de la variable "estado".
 *
 * @return el valor de la variable "estado".
 */
bool Vuelos::disponible()
{
    return estado;
}
/*
Vuelos obtenerDatosVuelo()
{
    int id, capacidad, numPasajeros;
    string fecha, ciudadOrigen, ciudadDestino, hora, ej;

    try
    {
        cout << "Ingrese la identificacion del vuelo: ";
        cin >> ej;
        id = stoi(ej);
    }
    catch (const invalid_argument &e)
    {
        cerr << "Error argumento invalido " << e.what() << "Ingrese un numero entero" << endl;
        cin >> id;
    }

    cin.ignore(); // Limpiar el buffer de entrada

    cout << "Ingrese la fecha del vuelo (YYYY-MM-DD): ";
    getline(cin, fecha);

    cout << "Ingrese la ciudad de destino: ";
    getline(cin, ciudadDestino);

    cout << "Ingrese la hora del vuelo (HH:MM): ";
    getline(cin, hora);

    // Crear y devolver un objeto Vuelos con los datos ingresados
    Vuelos tmp(id, fecha, ciudadDestino, hora);
    return tmp;
} */