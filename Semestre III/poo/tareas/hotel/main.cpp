#include "hotel.h"

/* Funcion que muestra el menu de reserva del hotel. Recibe una referencia al objeto Hotel. */
void menuReserva(Hotel &h)
{
    int opc = 0;
    while (opc != 4)
    {
        cout << "Menu de reserva \n1.Crear reserva \n2.Ver info hotel \n3.Check Out \n4.Salir \n>>";
        cin >> opc;
        switch (opc)
        {
            case 1:
                h.reserva(); // Llama al metodo de reserva del hotel.
                break;
            case 2:
                h.printInfoHotel(); // Llama al metodo que imprime la informacion del hotel.
                break;
            case 3:
                h.checkOut(); // Llama al metodo de check-out del hotel.
                break;
            case 4:
                cout << "Saliendo del menu" << endl;
                break;
            default:
                cout << "Opcion invalida, seleccione otra opcion" << endl;
                break;
        }
    }
}

int main()
{
    int opcion = 0;
    string n;
    Hotel hotel;
    srand(static_cast<unsigned int>(time(nullptr)));
    while (opcion != 2)
    {
        cout << "Seleccione una opcion\n1.Crear Hotel\n2.Salir\n>> " << endl;
        cin >> opcion;
        switch (opcion)
        {
            case 1:
                cout << "Ingrese el nombre" << endl;
                cin >> n;
                hotel.setNombre(n); // Establece el nombre del hotel.
                hotel.printInfoHotel(); // Imprime la informacion del hotel.
                menuReserva(hotel); // Llama al menu de reserva del hotel.
                break;
            case 2:
                cout << "Saliendo..." << endl;
                break;
            default:
                cout << "Opcion invalida, seleccione otra opcion" << endl;
                break;
        }
    }
    return 0;
}
