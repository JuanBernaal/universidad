import streamlit as st
import os
from vuelos import Vuelos

class View:

    def mainMenu(self):
        ans = 1
        
        option = st.sidebar.selectbox("Selecciona una opcion", ["Inicio", "Crear vuelos", "Crear aeronave", "Reservar vuelo", "Consultar informacion", "Simular"])
        if option == "Inicio":
            st.title("Alfonso Bonilla Aragan")
            st.subheader("Cualquier cosa")
            ##Mas descripcion

        if option == "Crear vuelos":
            ans = 2
            st.title("Creacion de vuelos")
            
        elif option == "Crear aeronave":
            ans = 3
        elif option == "Reservar vuelo":
            ans = 4
        elif option == "Consultar informacion":
            ans = 5
        elif option == "Simular":
            ans = 6    

        return ans
    
    def createFlight(self):
        id = st.number_input("Ingrese la identificacion del vuelo", step=1, value=None)
        destination = st.text_input("Ingrese la ciudad de destino", value=None)
        date = st.date_input("Fecha del vuelo", format="YYYY/MM/DD", value=None)
        st.write(date)
        time = st.time_input("Hora del vuelo", step=1800, value=None)
        st.write(time)
        if st.button("Guardar vuelo"):
            flight = Vuelos(id, date, destination, time)
            return flight
        
    def createAircraft(self, aeropuerto):
        self.aeropuerto = aeropuerto
        st.title("Creacion de aeronaves")
        choice = st.selectbox("Seleccione un tipo de aeronave", ["None", "Avion", "Jet Privado", "Helicoptero"])
        back = st.button("Volver")
