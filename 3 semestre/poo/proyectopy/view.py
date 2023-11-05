import streamlit as st
import os
from vuelos import Vuelos

class View:
        
    st.title("Alfonso Bonilla Aragan")
    st.write("")

    def mainMenu(self):
        ans = 0
        
        option = st.sidebar.selectbox("Selecciona una opcion", ["Menu principal", "Crear vuelos", "Crear aeronave", "Reservar vuelo", "Consultar informacion", "Simular"])
        if option == "Menu principal":
            ans = 1
        if option == "Crear vuelos":
            ans = 2
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
        st.info("Crea un vuelo ✈️")
        id = st.number_input("Ingrese la identificacion del vuelo", min_value=1)
        destination = st.text_input("Ingrese la ciudad de destino")
        date = st.date_input("Fecha del vuelo (MM/DD/YYYY)")
        st.info("Format MM/DD/YYYY")
        time = st.time_input("Hora del vuelo")
        st.info("Format HH:MM")
        flight = Vuelos(id, date, destination, time)
        return flight