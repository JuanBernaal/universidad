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
            if not flight == 0:
                self.aeropuerto.agregarDestino(flight)       

        elif option == 3:
            choice = self.view.createAircraft(self.aeropuerto)

            if choice == 1:
                self.view.createAirplane(self.aeropuerto)

            elif choice == 2:
                self.view.createJet(self.aeropuerto)

            elif choice == 3:
                self.view.createHelicopter(self.aeropuerto)    

        elif option == 4:
            self.view.bookFlight(self.aeropuerto)

        elif option == 5:
            selct = self.view.showInfo()
            if selct == 1:
                self.view.showFlights(self.aeropuerto)