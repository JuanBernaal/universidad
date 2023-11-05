import streamlit as st
import os
from model import Vuelos
from model import Avion

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
        choice = st.selectbox("Seleccione un tipo de aeronave", ["Avion", "Jet Privado", "Helicoptero"])

        if choice == "Avion":
            ans = 1

        return ans

    def createAirplane(self):

        brand = st.selectbox("Marca del avion", ["Boeing", "Airbus", "Sukhoi Superjet 100"])

        if brand == "Boeing":
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Boeing_full_logo.svg/1200px-Boeing_full_logo.svg.png", caption="Boeing, United States")
            select = st.selectbox("Linea", ["737", "747", "777", "787"])

            if select == "737":
                st.image("https://media.cnn.com/api/v1/images/stellar/prod/201221165638-boeing-737-crisis-boeing-debuts-first-737-max-boeing.jpg?q=w_1600,h_900,x_0,y_0,c_fill/h_618", caption= "Boeing 737 max")
                capacity = st.number_input("Capacidad del avion", step=1, value=180)
                st.info("La capacidad recomendada esta relacionada con la linea del avion")

            elif select == "747":
                st.image("https://aircharterservice-globalcontent-live.cphostaccess.com/images/aircraft-guide-images/group/boeing-747-400-large_tcm36-3689.jpg", caption="Boeing 747-400")
                capacity = st.number_input("Capacidad del avion", step=1, value=550)
                st.info("La capacidad recomendada esta relacionada con la linea del avion")

            elif select == "777":
                st.image("https://i0.wp.com/www.transponder1200.com/wp-content/uploads/2023/04/BOEING-777-ROLLOUT.jpg?fit=1050%2C600&ssl=1", caption="Boeing 777 premium comfort")
                capacity = st.number_input("Capacidad del avion", step=1, value=288)
                st.info("La capacidad recomendada esta relacionada con la linea del avion")

            elif select == "787":
                st.image("https://easbcn.com/wp-content/uploads/2020/07/256409_1-1000x423.jpg", caption="Boeing 787 dreamliner")
                capacity = st.number_input("Capacidad del avion", step=1, value=250)
                st.info("La capacidad recomendada esta relacionada con la linea del avion")

        engineCount = 2
        category = "Comercial"
        weightElevation = 100
        advance = st.button("Configuracion avanzada")

        if advance:
            with st.form("Advance configuration"):
                newEngineCount = st.number_input("Cantidad de motores", step=1, value=2)
                newCategory = st.text_input("Categoria del avion", value="Comercial")
                newWeightElevation = st.number_input("Peso que puede levantar el avion", step=1, value=100)
                submitted = st.form_submit_button("Guardar", type="primary")
                if submitted:
                    engineCount = newEngineCount
                    category = newCategory
                    advance = newWeightElevation

            if st.button("Cerrar"):
                advance = False

       
        if st.button("Crear avion", type="primary"):
            airplane = Avion(brand, capacity, self.aeropuerto.torreControl, engineCount, category, weightElevation)
            return airplane