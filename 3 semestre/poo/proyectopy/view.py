import streamlit as st
from model import Vuelos
from model import Avion
from model import JetPrivado
from model import Helicoptero

class View:

    def mainMenu(self):
        ans = 1
        
        option = st.sidebar.selectbox("Selecciona una opcion", ["Inicio", "Crear vuelos", "Crear aeronave", "Reservar vuelo", "Consultar informacion", "Simular"])
        if option == "Inicio":
            st.title("Alfonso Bonilla Aragan")
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
        ans = None
        id = st.number_input("Ingrese la identificacion del vuelo", step=1)
        destination = st.text_input("Ingrese la ciudad de destino", value=None)
        date = st.date_input("Fecha del vuelo", format="YYYY/MM/DD", value=None)
        st.write(date)
        time = st.time_input("Hora del vuelo", step=1800, value=None)
        st.write(time)
        if st.button("Crear vuelo", type="primary"):
            ans = {"id" : id, "date" : date, "destination" : destination, "time" : time}
            st.info("Su vuelo fue creado con exito")
        else: ans = 0
        return ans
        
    def createAircraft(self, aeropuerto):
        self.aeropuerto = aeropuerto
        st.title("Creacion de aeronaves")
        choice = st.selectbox("Seleccione un tipo de aeronave", ["Avion", "Jet Privado", "Helicoptero"])

        if choice == "Avion":
            ans = 1

        elif choice == "Jet Privado":
            ans = 2

        elif choice == "Helicoptero":
            ans = 3

        return ans

    def createAirplane(self, aeropuerto):

        brand = st.selectbox("Marca del avion", ["Boeing", "Airbus"])

        if brand == "Boeing":
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Boeing_full_logo.svg/1200px-Boeing_full_logo.svg.png", caption="Seattle, United States")
            select = st.selectbox("Linea", ["Boeing 737", "Boeing 747", "Boeing 777", "Boeing 787"])

            if select == "Boeing 737":
                st.image("https://i.blogs.es/30c172/7372/1366_521.jpg", caption= "Boeing 737 max")
                capacity = st.number_input("Capacidad del avion", step=1, value=180)
                st.info("La capacidad recomendada esta relacionada con la linea del avion")

            elif select == "Boeing 747":
                st.image("https://aircharterservice-globalcontent-live.cphostaccess.com/images/aircraft-guide-images/group/boeing-747-400-large_tcm36-3689.jpg", caption="Boeing 747-400")
                capacity = st.number_input("Capacidad del avion", step=1, value=550)
                st.info("La capacidad recomendada esta relacionada con la linea del avion")

            elif select == "Boeing 777":
                st.image("https://i0.wp.com/www.transponder1200.com/wp-content/uploads/2023/04/BOEING-777-ROLLOUT.jpg?fit=1050%2C600&ssl=1", caption="Boeing 777 premium comfort")
                capacity = st.number_input("Capacidad del avion", step=1, value=288)
                st.info("La capacidad recomendada esta relacionada con la linea del avion")

            elif select == "Boeing 787":
                st.image("https://easbcn.com/wp-content/uploads/2020/07/256409_1-1000x423.jpg", caption="Boeing 787 dreamliner")
                capacity = st.number_input("Capacidad del avion", step=1, value=250)
                st.info("La capacidad recomendada esta relacionada con la linea del avion")

        elif brand == "Airbus":
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Airbus_Group_Logo_2014.svg/2560px-Airbus_Group_Logo_2014.svg.png", caption="Blagnac, France")
            select = st.selectbox("Linea", ["Airbus A320", "Airbus A330", "Airbus A350", "Airbus A380", "Beluga Airbus"])

            if select == "Airbus A320":
                st.image("https://aircharterservice-globalcontent-live.cphostaccess.com/images/aircraft-guide-images/group/airbus-a320-large_tcm36-3644.jpg", caption= "Airbus A320")
                capacity = st.number_input("Capacidad del avion", step=1, value=180)
                st.info("La capacidad recomendada esta relacionada con la linea del avion")

            elif select == "Airbus A330":
                st.image("https://aircharterservice-globalcontent-live.cphostaccess.com/images/aircraft-guide-images/group/airbus-a330-200-large_tcm36-3653.jpg", caption="Airbus A330-200")
                capacity = st.number_input("Capacidad del avion", step=1, value=268)
                st.info("La capacidad recomendada esta relacionada con la linea del avion")

            elif select == "Airbus A350":
                st.image("https://aeroaffaires.es/wp-content/uploads/2021/07/1200px-a350_first_flight_-_low_pass_03-800x430-c-center.jpg", caption="Airbus A350")
                capacity = st.number_input("Capacidad del avion", step=1, value=410)
                st.info("La capacidad recomendada esta relacionada con la linea del avion")

            elif select == "Airbus A380":
                st.image("https://images.theconversation.com/files/259828/original/file-20190219-43267-sw50kg.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1356&h=668&fit=crop", caption="Airbus A380")
                capacity = st.number_input("Capacidad del avion", step=1, value=853)
                st.info("La capacidad recomendada esta relacionada con la linea del avion")

            elif select == "Beluga Airbus":
                st.image("https://upload.wikimedia.org/wikipedia/commons/7/72/%22Beluga_XL%22_A330-743L_%28cropped%29.jpg", caption="Beluga Airbus")
                capacity = st.number_input("Capacidad del avion", step=1)
                st.info("Este es un avion de carga, por lo tanto se recomienda que la capacidad sea la cantidad de miembros para la tripulacion")

        engineCount = 2
        category = "Comercial"
        weightElevation = 100
        advance = st.button("Configuracion avanzada")

        if advance:
            with st.form("Airplane advance configuration"):
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
            airplane = Avion(brand, capacity, aeropuerto.torreControl, engineCount, category, weightElevation)
            return airplane
        
    def createJet(self, aeropuerto):
        brand = st.selectbox("Marca del Jet", ["Boeing Business Jets", "Airbus Corporate Jets", "Sukhoi Superjet", "Embraer Executive Jets", "Bombardier"])

        if brand == "Boeing Business Jets":
            st.image("https://fokkertechniek.com/vip/wp-content/uploads/BBJ-Logo-Gold-2015-RGB.png", caption="Seattle, United States", width=700)
            st.subheader("Boeing Business Jet 777-X")
            st.image("https://aerocorner.com/wp-content/uploads/2020/07/Boeing-BBJ-777X-1090x500.jpg")

        elif brand == "Airbus Corporate Jets":
            st.image("https://www.corporatejetinvestor.com/wp-content/uploads/2016/07/ACJ-logo-V2-copper-2.png", caption="Blagnac, France", width=700)
            st.subheader("Airbus ACJ350-XWB")
            st.image("https://cdn.sanity.io/images/vxy259ii/production/d61ff9f7aa677690a3e64293e52ae150404396db-3626x2418.jpg")

        elif brand == "Sukhoi Superjet":
            st.image("https://upload.wikimedia.org/wikipedia/commons/f/f7/Logo_comercial_del_Superjet_100.jpg", caption="Москва, Россия")
            st.subheader("Sukhoi Superjet 100")
            st.image("https://vortexxmag.com/wp-content/uploads/2019/07/5096752790_ed24d0aae1_o.jpg")

        elif brand == "Embraer Executive Jets":
            st.image("https://www.marris-consulting.com/medias/comp/images/logo_embraer_noir.jpg?v=56", caption="São José dos Campos, Brasil")
            st.subheader("Embraer Praetor 600")
            st.image("https://aeroaffaires.es/wp-content/uploads/2019/07/praetor-600-aeroaffaires-e1564659513355.jpg")

        elif brand == "Bombardier":
            st.image("https://www.newunitedgoderich.com/app/uploads/2020/11/bombardier-logo.png", caption="Valcourt, Canada")
            st.subheader("Bombardier Challenger 3500")
            st.image("https://aeronauticapy.com/wp-content/uploads/2021/09/Challenger-3500-Exterior-Bronze-Livery.jpeg")

        capacityJet = st.number_input("Capacidad del Jet", step=1)
        owner = st.text_input("Nombre del propietario del Jet")
        if st.button("Crear Jet", type="primary"):
            jet = JetPrivado(brand, capacityJet, aeropuerto.torreControl, owner)
            return jet
        
    def createHelicopter(self, aeropuerto):
        brand = st.selectbox("Marca del Helicopter", ["Airbus Helicopters", "Bell"])

        if brand == "Airbus Helicopters":
            st.image("https://logovectordl.com/wp-content/uploads/2020/10/airbus-helicopters-logo-vector.png", caption="Blagnac, France")
            select = st.selectbox("Serie", ["Airbus H175M", "Airbus ACH160"])

            if select == "Airbus H175M":
                st.image("https://www.airforce-technology.com/wp-content/uploads/sites/6/2023/07/Featured-Image-H175M-helicopter.jpg", caption="Airbus x Boeing")

            else:
                st.image("https://www.airbus.com/sites/g/files/jlcbta136/files/styles/airbus_608x608/public/2023-03/ACH160%20Exclusive%20-%20Copy.jpg?itok=hnOYYt3h", caption="Airbus ACH160", width=700)
        
        elif brand == "Bell":
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Bell_Helicopter_Logo.svg/2560px-Bell_Helicopter_Logo.svg.png", caption="New York, United States")
            select = st.selectbox("Serie", ["Bell 427", "Bell 429"])

            if select == "Bell 427":
                st.image("https://flight-way.com/upload/resize_cache/webp/iblock/f99/709_545_1/f99be5cfc693dab6666665efee185adf.webp", caption="Bell 427")

            else:
                st.image("https://d21buns5ku92am.cloudfront.net/67992/images/365357-ESGBell_429Rendering-d5a7cc-large-1600878707.jpg", caption="Bell 429", width=700)
        
        capacityHelicopter = st.number_input("Capacidad del Helicoptero", step=1)
        numRotores = 4
        elevation = 1000
        use = "Servicio de rescate"
        advance = st.button("Configuracion avanzada")

        if advance:
            with st.form("Helicopter Advanced Settings"):
                newNumRotores = st.number_input("Numero de rotores", step=1, value=4)
                newElevation = st.number_input("Altitud maxima", step=1, value=1000)
                newUse = st.text_input("Uso", value="Servicio de rescate")
                st.info("Los valores que se muestran son parametros predeterminados y pueden ser modificados")
                if st.form_submit_button("Guardar", type="primary"):
                    numRotores = newNumRotores
                    elevation = newElevation
                    use = newUse
                
            if st.button("Cerrar"):
                advance = False
        if st.button("Crear helicoptero", type="primary"):
            helicoptero = Helicoptero(brand, capacityHelicopter, aeropuerto.torreControl, numRotores, elevation, use)
            return helicoptero
            
    def bookFlight(self, aeropuerto):
        st.title("Reservar Vuelo")
        if aeropuerto.empty():
            st.warning("No hay vuelos creados")
            
    def showInfo(self):
        ans = 1
        st.write("Sistema de consulta")
        select = st.selectbox("Seleccione el tipo de consulta", ["Consultar vuelos", "Consultar puertas", "Consultar aeronaves"])
        if select == "Consultar puertas":
            ans = 2
        elif select == "Consultar aeronaves":
            ans = 3
        return ans

    def showFlights(self, aeropuerto):
        st.write(aeropuerto.printDestinos())