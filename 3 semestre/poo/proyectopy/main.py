from model import Aeropuerto, Controller, View

aeropuerto = Aeropuerto.obtenerInstancia()

vista = View()
controlador = Controller(aeropuerto, vista)