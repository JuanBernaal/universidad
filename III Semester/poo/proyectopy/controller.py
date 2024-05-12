from view import View
import streamlit as st
from model import Vuelos, Avion, JetPrivado, Helicoptero, Pasajero

class Controller:
    def __init__(self, view, aeropuerto, pasajero):
        self.view = view
        self.aeropuerto = aeropuerto
        self.pasajero = pasajero

    "Funcion que recibe las elecciones del view y hace todas las operaciones necesarias"

    def ejecutar(self):
        option = self.view.mainMenu()

        if option == 2:         ## Crear Vuelo ##
            dic = self.view.createFlight()

            if not dic == 0:
                vuelo = Vuelos(dic["ID"], dic["Date"], dic["Destination"], dic["Time"], dic["Airline"])
                self.aeropuerto.agregarDestino(vuelo)
                self.aeropuerto.destinationsTab(dic)

        elif option == 3:       ## Crear Aeronave ##
            choice = self.view.createAircraft()

            if choice == 1:
                airplaneDic = self.view.createAirplane()   

                if not airplaneDic == 0:
                    Avion(airplaneDic["Brand"], airplaneDic["Capacity"], self.aeropuerto.torreControl, airplaneDic["Engine Count"], 
                          airplaneDic["Category"], airplaneDic["Autonomy"])
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

        elif option == 4:       ## Reservar vuelo ##
            opt = self.view.registerPassenger(self.aeropuerto)
            if opt == 1:
                passDic = self.view.passengerData()
                if passDic != 0:
                    self.pasajero = Pasajero(passDic["Name"], passDic["Last Name"], passDic["Age"], passDic["id"], passDic["Birth Day"],
                                        passDic["Gender"], passDic["Address"], passDic["Phone Number"], passDic["Email"], 
                                        passDic["Nationality"], passDic["Medical Info"], passDic["Checked bags"])
                indice = self.view.bookFlight(self.aeropuerto)
                if not indice == -1:
                    tmp = self.aeropuerto.obtenerVuelo(indice)
                    self.pasajero.asignarVueloPass(self.pasajero, tmp)
                    st.success("El vuelo ha sido reservado")
                        

        elif option == 5:       ## Consultar Informacion ##       
            selct = self.view.showInfo()

            if selct == 1:
                self.view.showFlights(self.aeropuerto)
                
            elif selct == 2:
                self.aeropuerto.torreControl.mostrarPuertas()
                
            elif selct == 3:
                opti = self.view.showAircraft()

                if opti == 1:
                    self.view.showAirplanes(self.aeropuerto)
                    x = self.view.manageAirplanes(self.aeropuerto)
                    if x != 0:
                        if x[0] == 1:
                            self.aeropuerto.avionesAeropuerto[x[1]]["Available"] = False
                        elif x[0] == 2:
                            self.aeropuerto.avionesAeropuerto[x[1]]["Available"] = True
                
                elif opti == 2:
                    self.view.showJets(self.aeropuerto)

                elif opti == 3:
                    self.view.showHelicopters(self.aeropuerto)
                    
        elif option == 6:       ## Simular ##
            self.view.sim(self.aeropuerto)     
            
        elif option == 7:       ## API Consulta externa ##
            self.view.getCountryInfo()     