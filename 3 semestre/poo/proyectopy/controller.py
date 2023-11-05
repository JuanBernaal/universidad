from view import View
import streamlit as st


class Controller:
    def __init__(self, view, aeropuerto):
        self.view = view
        self.aeropuerto = aeropuerto

    def ejecutar(self):
        option = self.view.mainMenu()

        if option == 2:
            flight = self.view.createFlight()
            self.aeropuerto.agregarDestino(flight)       

        if option == 3:
            self.view.createAircraft(self.aeropuerto)