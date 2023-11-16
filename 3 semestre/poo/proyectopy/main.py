from model import Aeropuerto
from view import View
from controller import Controller
from model import Pasajero

def main():
    airport = Aeropuerto.obtenerInstancia()
    view = View()
    passenger = Pasajero
    controlador = Controller(view, airport, passenger) 
    controlador.ejecutar()  
main()