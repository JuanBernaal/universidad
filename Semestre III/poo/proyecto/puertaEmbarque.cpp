#include "puertaEmbarque.h"

/**
 * El constructor PuertaEmbarque inicializa la variable de identificación con el nombre dado y
 * establece la disponibilidad en verdadero.
 *
 * @param nombre El parámetro "nombre" es un número entero que representa el número de identificación del
 * puerta de embarque.
 */
PuertaEmbarque::PuertaEmbarque(int nombre) : identificacion(nombre)
{
    disponibilidad = true;
}

/**
 * La función "anunciarEmbarque" anuncia el embarque en una puerta específica.
 *
 * @param puerta El parámetro "puerta" es una referencia a una cadena constante. Representa la puerta
 * número para el que se realiza el anuncio de embarque.
 */
void PuertaEmbarque::anunciarEmbarque(const string &puerta)
{
    cout << "Anuncio de embarque en " << identificacion << " - Puerta " << puerta << endl;
}