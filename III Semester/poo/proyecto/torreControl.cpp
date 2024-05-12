#include "torreControl.h"

/**
 * El constructor TorreControl inicializa seis objetos PuertaEmbarque y los agrega a las puertas
 *vectorial.
 */
TorreControl::TorreControl()
{
    PuertaEmbarque puerta1(1);
    PuertaEmbarque puerta2(2);
    PuertaEmbarque puerta3(3);
    PuertaEmbarque puerta4(4);
    PuertaEmbarque puerta5(5);
    PuertaEmbarque puerta6(6);

    puertas.push_back(puerta1);
    puertas.push_back(puerta2);
    puertas.push_back(puerta3);
    puertas.push_back(puerta4);
    puertas.push_back(puerta5);
    puertas.push_back(puerta6);
}

/**
 * La función "registrarAeronave" agrega un nuevo objeto "Aeronave" al vector "aeronaves".
 *
 * @param aeronave Un puntero a un objeto de tipo Aeronave.
 */
void TorreControl::registrarAeronave(Aeronave *aeronave)
{
    aeronaves.push_back(aeronave);
}
/**
 * La función "registrarAvion" agrega una nueva aeronave al vector "aviones".
 *
 * @param aeronave Un puntero a un objeto de tipo Aeronave.
 */
void TorreControl::registrarAvion(Aeronave *aeronave)
{
    aviones.push_back(aeronave);
}

/**
 * La función `enviarMensaje` de la clase `TorreControl` envía un mensaje a todas las aeronaves excepto a la
 *uno que es el remitente.
 *
 * @param mensaje Una referencia a un objeto de cadena que representa el mensaje a enviar.
 * @param emisor Un puntero a un objeto de tipo Aeronave, que representa el remitente del mensaje.
 */
void TorreControl::enviarMensaje(const string &mensaje, Aeronave *emisor)
{
    for (auto &aeronave : aeronaves)
    {
        if (aeronave != emisor)
        {
            aeronave->recibirMensaje(mensaje);
        }
    }
}

/**
 * La función asigna una puerta a una aeronave y actualiza la disponibilidad de la puerta.
 *
 * @param aeronave Un puntero a un objeto de tipo Aeronave.
 * @param puerta El parámetro "puerta" representa el número de puerta donde será asignada la aeronave
 *para embarque.
 * @param cod El parámetro "cod" probablemente sea un identificador o código para la puerta asignada. Podría ser
 * utilizado para rastrear o hacer referencia a la puerta de alguna manera.
 * @param hora El parámetro "hora" es una referencia constante a una cadena. Se utiliza para pasar el rato.
 * la asignación de la puerta de embarque.
 */
void TorreControl::asignarPuertaDeEmbarque(Aeronave *aeronave, int puerta, int cod, const string &hora)
{
    aeronave->asignarPuertaDeEmbarque(puerta, cod, hora);
    puertas[puerta - 1].disponibilidad = false;
}

/**
 * La función "disponibilidadNaves" comprueba si hay algún avión disponible en las "aeronaves"
 *vectorial.
 *
 * @return un valor booleano. Si el tamaño del vector "aeronaves" es 0, devolverá falso.
 * De lo contrario, devolverá verdadero.
 */
bool TorreControl::disponibilidadNaves()
{
    if (aeronaves.size() == 0)
        return false;
    else
        return true;
}

/**
 * La función "mostrarAviones" imprime información sobre los aviones almacenados en las "aeronaves"
 *vectorial.
 */
void TorreControl::mostrarAviones()
{
    if (aeronaves.size() == 0)
        printf("No hay aeronaves\n");
    for (int i = 0; i < aeronaves.size(); i++)
    {
        printf("%d.\n", i + 1);
        aeronaves[i]->printInfo();
    }
}

/**
 * La función "seleccionarAeronave" selecciona una aeronave disponible, le agrega un vuelo y le asigna un
 * puerta de embarque del vuelo.
 *
 * @param v El parámetro "v" es un puntero a un objeto de tipo "Vuelos".
 */
void TorreControl::seleccionarAeronave(Vuelos *v)
{
    for (auto &aeronave : aeronaves)
    {
        if (aeronave->estado)
        {
            aeronave->agregarVuelo(v);
            bool flag = true;
            for (int i = 0; i < puertas.size() && flag; i++)
            {
                if (puertas[i].disponibilidad)
                {
                    this->asignarPuertaDeEmbarque(aeronave, puertas[i].identificacion, v->identificacion, v->hora);
                    flag = false;
                }
            }
            break;
        }
    }
}

/**
 * La función "generarNumeroAleatorio" genera un número aleatorio entre 10.000 y 100.000.
 *
 * @return un número generado aleatoriamente entre 10.000 y 100.000.
 */
int generarNumeroAleatorio()
{
    // Inicializa la semilla del generador de números aleatorios
    std::srand(static_cast<unsigned int>(std::time(nullptr)));

    int num1 = rand() % 90001 + 10000;
    int num2 = rand() % 90001 + 10000;
    // Genera un número aleatorio entre 10,000 y 100,000
    int numeroAleatorio = std::rand() % num1 + num2; // [0, 90000] + 10000 = [10000, 100000]

    return numeroAleatorio;
}

/**
 * La función `simulación` simula los vuelos de las aeronaves, generando posiciones aleatorias y
 * actualizar sus posiciones en consecuencia.
 */
void TorreControl::simulacion()
{
    int pos1, pos2;

    for (auto &aeronave : aeronaves)
    {
        if (aeronave->tieneVuelos())
        {
            for (int i = 0; i < aeronave->vuelos.size(); i++)
            {
                aeronave->despegar();
                pos1 = generarNumeroAleatorio();
                pos2 = generarNumeroAleatorio();
                string n = "Lat: ";
                string m = " Lon: ";
                string tmp = to_string(pos1);
                n += tmp;
                n += m;
                tmp = to_string(pos2);
                n += tmp;
                aeronave->actualizarPosicion(n);
                aeronave->aterrizar();
            }
            for (int i = 0; i < aeronave->vuelos.size(); i++)
                aeronave->eliminarVuelo();
        }
    }

    for (int i = 0; i < puertas.size(); i++)
    {
        puertas[i].disponibilidad = true;
    }
}

/**
 * La función "mostrarPuertas" en la clase "TorreControl" muestra el estado de disponibilidad de cada
 * puerta.
 */
void TorreControl::mostrarPuertas()
{
    for (int i = 0; i < puertas.size(); i++)
    {
        cout << "Puerta #" << puertas[i].identificacion;
        if (puertas[i].disponibilidad)
            cout << " disponible ";
        else
            cout << "no disponible " << endl
                 << endl;
        printf("\n");
    }
}