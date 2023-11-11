from view import View
import streamlit as st
from model import Vuelos, Avion, JetPrivado, Helicoptero

class Controller:
    def __init__(self, view, aeropuerto, pasajero):
        self.view = view
        self.aeropuerto = aeropuerto
        self.pasajero = pasajero

    def ejecutar(self):
        option = self.view.mainMenu()

        if option == 2:
            dic = self.view.createFlight()

            if not dic == 0:
                vuelo = Vuelos(dic["ID"], dic["Date"], dic["Destination"], dic["Time"])
                self.aeropuerto.agregarDestino(vuelo)
                self.aeropuerto.destinationsTab(dic)

        elif option == 3:
            choice = self.view.createAircraft()

            if choice == 1:
                airplaneDic = self.view.createAirplane()   

                if not airplaneDic == 0:
                    Avion(airplaneDic["Brand"], airplaneDic["Capacity"], self.aeropuerto.torreControl, airplaneDic["Engine Count"], 
                          airplaneDic["Category"], airplaneDic["Weight Elevation"])
                    self.aeropuerto.avionesAeropuerto.append(airplaneDic)
                    
            elif choice == 2:
                jetDic = self.view.createJet()

                if not jetDic == 0:
                    JetPrivado(jetDic["Brand"], jetDic["Capacity"], self.aeropuerto.torreControl, jetDic["Owner"])
                    self.aeropuerto.jetsAeropuerto.append(jetDic)

            elif choice == 3:
                helicopterDic = self.view.createHelicopter()

                if not helicopterDic == 0:
                    Helicoptero(helicopterDic["Brand"], helicopterDic["Capacity"], self.aeropuerto.torreControl,
                                helicopterDic["Number of Rotors"], helicopterDic["Max Height"], helicopterDic["Use"])
                    self.aeropuerto.helicopterosAeropuerto.append(helicopterDic)

        elif option == 4:
            opt = self.view.bookFlight(self.aeropuerto)

        elif option == 5:
            selct = self.view.showInfo()

            if selct == 1:
                self.view.showFlights(self.aeropuerto)

            elif selct == 3:
                opti = self.view.showAircraft()

                if opti == 1:
                    self.view.showAirplanes(self.aeropuerto)
                
                elif opti == 2:
                    self.view.showJets(self.aeropuerto)

                elif opti == 3:
                    self.view.showHelicopters(self.aeropuerto)
                    