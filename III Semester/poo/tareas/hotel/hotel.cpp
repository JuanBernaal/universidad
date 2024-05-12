#include "hotel.h"


Hotel::Hotel()
{
    for (int i = 0; i < 10; i++)
    {
        Habitacion n(i);                 // Crea una nueva habitación con número 'i'
        habitaciones.push_back(n);       // Agrega la habitación a la lista de habitaciones del hotel
        Huesped h;                       // Crea un nuevo huésped vacío
        huespedes.push_back(h);          // Agrega el huésped a la lista de huéspedes del hotel
    }
}

// Asigna el nombre del hotel.
void Hotel::setNombre(string &n)
{
    nombre = n;
}

// Imprime la información de todas las habitaciones del hotel, incluyendo el número, precio, estado y datos del huésped si está ocupada.
void Hotel::printInfoHotel()
{
    for (vector<Habitacion>::iterator it = habitaciones.begin(); it != habitaciones.end(); it++)
    {
        printf("_____________________________\n");
        cout << "Habitacion: " << (*it).getNumero() << endl
             << "Precio: " << (*it).getPrecio() << endl;

        if ((*it).getEstado())
        {
            cout << "Estado: Ocupado\n"
                 << endl
                 << "Cliente: " << huespedes[(*it).getNumero()].getName() << endl
                 << "Tel: " << huespedes[(*it).getNumero()].getTel() << endl;
        }
        else
            cout << "Estado: Desocupado" << endl;
    }
    printf("_____________________________\n");
}

// Realiza el proceso de reserva de una habitación para un huésped.
void Hotel::reserva()
{
    string n;
    int t;
    // Ingresar datos
    cout << "\nIngrese su nombre: ";
    cin >> n;
    cout << "\nIngrese su numero telefonico: ";
    cin >> t;
    Huesped h(n, t);   // Crea un nuevo huésped con el nombre y número de teléfono ingresados
    cout << "Confirmacion de datos:" << endl
         << "Nombre: " << h.getName() << endl
         << "Tel: " << h.getTel() << endl
         << "Disponivilidad en tarjeta: " << h.getDinero() << endl;
    // Proceso de reserva
    bool flag = true;
    while (flag)
    {
        int num;
        cout << "\nSeleccione la habitacion que desea reservar: ";
        cin >> num;
        if (num > 10)
            cout << "Seleccione una habitacion entre la 0 y la 9" << endl;
        else if (habitaciones[num].getEstado())
            cout << "Esta habitacion esta reservada, seleccione otra opcion" << endl;
        else if (h.getDinero() < habitaciones[num].getPrecio())
            cout << "El precio de esta habitación supera el monto en su tarjeta, seleccione otra opcion" << endl;
        else
        {
            huespedes[num] = h;                       // Asigna al huésped a la habitación seleccionada
            habitaciones[num].setOcupado();           // Marca la habitación como ocupada
            h.setDinero(h.getDinero() - habitaciones[num].getPrecio());  // Actualiza el dinero del huésped después de pagar la habitación
            cout << "La reserva ha sido exitosa, disfrute su estadia" << endl;
            flag = false;
        }
    }
    cout << endl;
}

// Realiza el proceso de check-out de un huésped de una habitación.
void Hotel::checkOut()
{
    int opc;
    bool flag = true;
    while (flag)
    {
        cout << "Ingresar numero de la habitacion para checkout" << endl;
        cin >> opc;
        if (habitaciones[opc].getEstado())
        {
            huespedes[opc].checkOutHuesped();   // Realiza el check-out del huésped de la habitación seleccionada
            habitaciones[opc].setDesocupado();  // Marca la habitación como desocupada
            flag = false;
        }
        else
            cout << "Error: la habitacion seleccionada esta desocupada" << endl;
    }
}
