from view import View
import streamlit as st
from model import Vuelos

class Controller:
    def __init__(self, view, aeropuerto):
        self.view = view
        self.aeropuerto = aeropuerto

    def ejecutar(self):
        option = self.view.mainMenu()

        if option == 2:
            dic = self.view.createFlight()
            if not dic == 0:
                self.aeropuerto.agregarDestino(dic)

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