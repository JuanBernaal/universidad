from view import View
import streamlit as st
from model import Vuelos
from model import Avion

class Controller:
    def __init__(self, view, aeropuerto):
        self.view = view
        self.aeropuerto = aeropuerto

    def ejecutar(self):
        option = self.view.mainMenu()

        if option == 2:
            dic = self.view.createFlight()
            if not dic == 0:
                id = dic["ID"]
                date = dic["Date"]
                destination = dic["Destination"]
                time = dic["Time"]
                vuelo = Vuelos(id, date, destination, time)
                self.aeropuerto.agregarDestino(vuelo)
                self.aeropuerto.destinationsTab(dic)

        elif option == 3:
            choice = self.view.createAircraft()

            if choice == 1:
                airplane = self.view.createAirplane(self.aeropuerto)
                if not airplane == 0:
                    brand = airplane["brand"]

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