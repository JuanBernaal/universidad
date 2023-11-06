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
            choice = self.view.createAircraft(self.aeropuerto)

            if choice == 1:
                self.view.createAirplane(self.aeropuerto)

            elif choice == 2:
                self.view.createJet(self.aeropuerto)

            elif choice == 3:
                self.view.createHelicopter(self.aeropuerto)            