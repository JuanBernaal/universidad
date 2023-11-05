from model import Aeropuerto
from view import View
from controller import Controller

def main():
    aeropuerto = Aeropuerto.obtenerInstancia()
    vista = View()
    controlador = Controller(vista, aeropuerto)
    controlador.ejecutar()    
main()  