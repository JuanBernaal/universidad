import streamlit as st
import json
import requests

class View:
    
   
    ## Menu que retorna el valor de selección
    
    def mainMenu(self):
        ans = 1
        
        option = st.sidebar.selectbox("Selecciona una opcion", ["Inicio", "Crear vuelos", 
                                                                "Crear aeronave", "Reservar vuelo", 
                                                                "Consultar informacion", "Simular",
                                                                "Consultar pais"])
        if option == "Inicio":
            st.title("Alfonso Bonilla Aragon")
            st.header("Historia")
            st.markdown(""" Desde la década de los años 30 hasta nuestros días, el Valle del Cauca ha contado con tres aeropuertos, sin incluir las pistas privadas de Jamundí y “el Limonar”.

Durante el primer año de la presidencia de Enrique Olaya Herrera, se iniciaron las gestiones para adquirir los terrenos destinados a una base-escuela de aviación militar, en Cali. Estas gestiones se llevaron a cabo con un conocido hacendado de la región, Abraham Domínguez. Se negociaron 400 fanegadas de la propiedad “El Guabito” ubicada al norte la ciudad.

El 21 de septiembre de 1933 se dio inicio a vuelos comerciales y militares en la base de “El Guabito”. Ese día, aeronaves internacionales de Panagra y nacionales de Scadta unían a Cali con las principales ciudades colombianas y a Colombia con otros países.

El uso alterno de la pista de “El Guabito” no duró mucho tiempo, debido a que los vuelos mixtos de aeronaves comerciales y aeronaves de aprendizaje no eran aconsejables dentro de una base militar. Años después se produciría la separación de esos vuelos al tiempo que Avianca, nombre sustituto de la pionera Scadta, adquiriera los terrenos de la antigua hacienda “Guales”, sobre la carretera Cali-Candelaria, situada a 18 kilómetros al oriente de la capital vallecaucana.

En 1943 comienza a operar un nuevo aeropuerto, bautizado con el nombre de Calipuerto. Este aeropuerto daba a Colombia la imagen de un país “desordenado y folclórico”. La sala de recibo de los viajeros era estrecha, incomoda e inadecuada para el creciente movimiento de llegada y salida de gentes de distintas nacionalidades.

Por la década de 1950 surgieron rumores encaminados hacia la necesidad que tenía Cali de construir un moderno y funcional terminal aéreo. Estos rumores llevaron a que la sociedad propietaria de “Calipuerto” iniciara los trabajos de ampliación de sus instalaciones y pista. Estos trabajos hicieron posible que “Calipuerto” prolongara durante veintiocho años más su vida útil.

En 1954 se propuso la construcción para Cali de un nuevo aeropuerto de magnitud internacional. La localización técnica inicio ese mismo año y, un año después, se efectuaron estudios preliminares auspiciados por la ECA. La gestación del hoy Aeropuerto Internacional “Alfonso Bonilla Aragón” contó con un proceso largo y difícil. Tanto es así, que para obtener el informe favorable de la Misión de Transporte del Banco Mundial, que fue la que recomendó la construcción del aeropuerto de Cali, tuvieron que transcurrir siete años.

En el mes de noviembre de 1962 estaba abierta la licitación para financiación y diseño de los aeropuertos de Cali y Barranquilla, cuyos préstamos debían ofrecer un plazo mínimo de siete años. Al mismo tiempo se elevaron las propuestas para los terminales aéreos de las capitales del Valle y del Atlántico. Poco después la Junta Técnica del ministerio de Obras Publicas descartó las dos solicitudes.

La Unidad de Acción Vallecaucana, a pesar del rechazo, continuó en la lucha con ejemplar perseverancia. A ellos se les unió la clase política vallecaucana tanto en los órdenes, departamental como nacional. Se continúa adelantando las diligencias pertinentes ante los organismos competentes, se insiste en la factibilidad de la obra, la planeación de la misma, su necesidad y mil razones más. Todo con tal de conseguir el deseado fin, la aprobación del aeropuerto internacional de Cali.

Se presentaron dos proyectos arquitectónicos para el nuevo terminal aéreo. Uno de ellos, presentado por Ernesto Sarria y su grupo. Dicho proyecto recibió el premio nacional de ingeniería, premio que adjudica todos los años la Sociedad Colombiana de Ingenieros. Así mismo, fue llevado ante la Comisión del Grupo Internacional en Washington por Diego Calle, ministro de Hacienda de la época.

A finales de 1967, Bernardo Garcés Córdoba y Juan Berón del ministerio de obras públicas y de la agencia general de la ECA respectivamente, se unirán para resolver con la mayor brevedad posible el inconveniente que se vislumbraba para los Juegos Panamericanos de Cali.

Es mismo año se firmaría el primer contrato que fue adjudicado a la firma Conciviles S.A. para la construcción de las sub-bases, por un valor de $11’700.000=

En 1968, se firmaría en Cali, con la misma Conciviles S.A., el contrato para la pavimentación de la pista de aterrizaje, las calles de rodaje y las plataformas del aeropuerto. La firma Camacho & Guerrero compañía, entrega los planos y respectivos estudios, se fija la fecha del 5 de agosto de 1969 para el cierre de la licitación referente a las estructuras del edificio terminal del nuevo aeropuerto. A partir de este momento la responsabilidad de la obra recae sobre las firmas AIC y AIA, con la interventoría de Planes Ltda.

Tras los problemas de orden económico acaecidos entre 1970 y 1971, la Unidad de Acción Vallecaucana logra que el gobierno central destine partidas por $36’000.000=. En razón al compromiso que había adquirido la ciudad de Cali en Winnipeg, realizar los Juegos Panamericanos, se efectúa la inauguración de la primera etapa del aeropuerto. Este acto solemne tuvo lugar el 24 de julio de 1971. Al acto asistió el Presidente de la República y los altos dignatarios de los gobiernos seccional, regional y nacional.

En el año 2000, el consorcio Aerocali S.A. cuyos integrantes eran Aeropuertos Españoles y Navegación Aérea – AENA y Dragados de España, y la entidad financiera Corficolombiana, fue adjudicatario de la concesión del aeropuerto de Cali (Colombia) para los próximos 20 años, tras ganar la licitación pública internacional de esta terminal.""")
            

            st.image("https://www.aerocali.com.co/wp-content/uploads/2014/09/webhist.jpg")

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
        elif option == "Consultar pais":
            ans = 7

        return ans
    
    ## Crea vuelos y retorna un diccionario

    def createFlight(self):
        ans = None

        airline = st.selectbox("Seleccione la aerolinea", ["Latam Airlines", "Avianca", "Copa Airlines"])

        if airline == "Latam Airlines":
            st.image("https://s.latamairlines.com/images/seo/logo-latam-airlines.png")
            airline = "Latam Airlines 🔵🔴"
        
        elif airline == "Avianca":
            st.image("https://volavi.co/wp-content/uploads/2023/10/Nuevo-Logo_avianca-Octubre2023.jpg.webp")
            airline = "Avianca 🔴⚪"

        elif airline == "Copa Airlines":
            st.image("https://i.pinimg.com/originals/36/2e/f1/362ef1504c88832dafac7d03d05f419a.jpg")
            airline = "Copa Airlines 🔵⚪"

        id = st.number_input("Ingrese la identificacion del vuelo:", step=1, value=None)
        destination = st.text_input("Ingrese la ciudad de destino:", value=None)
        date = st.date_input("Fecha del vuelo:", format="YYYY/MM/DD", value=None)
        st.write(date)
        time = st.time_input("Hora del vuelo:", step=900, value=None)
        st.write(time)
        boton = st.button("Crear vuelo", type="primary")
        if boton and (id != None) and (destination != None) and (date != None):
            ans = {"ID" : id, "Date" : date, "Departure Country" : "CLO 🟡🔵🔴", "Destination" : destination, "Time" : time, "Airline" : airline}
            st.success("Su vuelo fue creado con exito")
        elif boton and ((id == None) or (destination == None) or (date == None)):
            st.error("⛔Todos los campos son obligatorios")
            ans = 0
        else: 
            ans = 0
        return ans
        
    ## Menu de seleccionar qué aeronave crear

    def createAircraft(self):

        st.title("Creacion de aeronaves")
        choice = st.selectbox("Seleccione un tipo de aeronave:", ["Avion", "Jet Privado", "Helicoptero"])

        if choice == "Avion":
            ans = 1

        elif choice == "Jet Privado":
            ans = 2

        elif choice == "Helicoptero":
            ans = 3

        return ans

    ## las siguientes 3 Funciones para crean aeronaves y retornan diccionarios con la info necesaria para hacer el objeto

    def createAirplane(self):
        ans = None
        brand = st.selectbox("Marca del avion:", ["Boeing", "Airbus"])

        if brand == "Boeing":
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Boeing_full_logo.svg/1200px-Boeing_full_logo.svg.png", caption="Seattle, United States")
            select = st.selectbox("Linea:", ["Boeing 737", "Boeing 747", "Boeing 777", "Boeing 787"])

            if select == "Boeing 737":
                st.image("https://i.blogs.es/30c172/7372/1366_521.jpg", caption= "Boeing 737 max")
                capacity = st.number_input("Capacidad del avion:", step=1, value=180)
                st.info("La capacidad recomendada esta relacionada con la linea del avion")
                engineCount = 2
                category = "Comercial"
                autonomy = 3550

            elif select == "Boeing 747":
                st.image("https://aircharterservice-globalcontent-live.cphostaccess.com/images/aircraft-guide-images/group/boeing-747-400-large_tcm36-3689.jpg", caption="Boeing 747-400")
                capacity = st.number_input("Capacidad del avion:", step=1, value=550)
                st.info("La capacidad recomendada esta relacionada con la linea del avion")
                engineCount = 4
                category = "Comercial"
                autonomy = 7730

            elif select == "Boeing 777":
                st.image("https://i0.wp.com/www.transponder1200.com/wp-content/uploads/2023/04/BOEING-777-ROLLOUT.jpg?fit=1050%2C600&ssl=1", caption="Boeing 777 premium comfort")
                capacity = st.number_input("Capacidad del avion:", step=1, value=288)
                st.info("La capacidad recomendada esta relacionada con la linea del avion")
                engineCount = 2
                category = "Comercial"
                autonomy = 7880

            elif select == "Boeing 787":
                st.image("https://easbcn.com/wp-content/uploads/2020/07/256409_1-1000x423.jpg", caption="Boeing 787 dreamliner")
                capacity = st.number_input("Capacidad del avion:", step=1, value=250)
                st.info("La capacidad recomendada esta relacionada con la linea del avion")
                engineCount = 2
                category = "Comercial"
                autonomy = 7643

        elif brand == "Airbus":
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Airbus_Group_Logo_2014.svg/2560px-Airbus_Group_Logo_2014.svg.png", caption="Blagnac, France")
            select = st.selectbox("Linea:", ["Airbus A320", "Airbus A330", "Airbus A350", "Airbus A380", "Beluga Airbus"])

            if select == "Airbus A320":
                st.image("https://aircharterservice-globalcontent-live.cphostaccess.com/images/aircraft-guide-images/group/airbus-a320-large_tcm36-3644.jpg", caption= "Airbus A320")
                capacity = st.number_input("Capacidad del avion:", step=1, value=180)
                st.info("La capacidad recomendada esta relacionada con la linea del avion")
                engineCount = 2
                category = "Comercial"
                autonomy = 3300

            elif select == "Airbus A330":
                st.image("https://aircharterservice-globalcontent-live.cphostaccess.com/images/aircraft-guide-images/group/airbus-a330-200-large_tcm36-3653.jpg", caption="Airbus A330-200")
                capacity = st.number_input("Capacidad del avion:", step=1, value=268)
                st.info("La capacidad recomendada esta relacionada con la linea del avion")
                engineCount = 2
                category = "Comercial"
                autonomy = 7200

            elif select == "Airbus A350":
                st.image("https://aeroaffaires.es/wp-content/uploads/2021/07/1200px-a350_first_flight_-_low_pass_03-800x430-c-center.jpg", caption="Airbus A350")
                capacity = st.number_input("Capacidad del avion:", step=1, value=410)
                st.info("La capacidad recomendada esta relacionada con la linea del avion")
                engineCount = 2
                category = "Comercial"
                autonomy = 8690

            elif select == "Airbus A380":
                st.image("https://images.theconversation.com/files/259828/original/file-20190219-43267-sw50kg.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1356&h=668&fit=crop", caption="Airbus A380")
                capacity = st.number_input("Capacidad del avion:", step=1, value=853)
                st.info("La capacidad recomendada esta relacionada con la linea del avion")
                engineCount = 4
                category = "Comercial"
                autonomy = 8200

            elif select == "Beluga Airbus":
                st.image("https://upload.wikimedia.org/wikipedia/commons/7/72/%22Beluga_XL%22_A330-743L_%28cropped%29.jpg", caption="Beluga Airbus")
                capacity = st.number_input("Capacidad del avion:", step=1)
                st.info("Este es un avion de carga, por lo tanto se recomienda que la capacidad sea la cantidad de miembros para la tripulacion")
                engineCount = 2
                category = "Comercial"
                autonomy = 2200

        advance = st.button("Mostrar especificaciones")
        conguration = {"Cantidad de motores" : engineCount, "Categoria del avion" : category, "Autonomy (miles)" : autonomy}
        estado = True
        if advance:
            st.table(conguration)

            if st.button("Cerrar"):
                advance = False

        ap = st.button("Crear avion", type="primary")

        if ap and capacity > 0:
            ans = {"Brand" : brand, "Capacity" : capacity, "Engine Count" : engineCount, "Category" : category, "Autonomy" : autonomy, "Available" : estado}
            st.success("Avion creado con exito")
        elif ap and capacity <= 0:
            st.error("⛔La capacidad debe ser un entero postivo")
            ans = 0
        else: ans = 0

        return ans
        
    def createJet(self):
        ans = None
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

        capacityJet = st.number_input("Capacidad del Jet", step=1, value=None)
        owner = st.text_input("Nombre del propietario del Jet", value=None)
        jetButton = st.button("Crear Jet", type="primary")
        if jetButton and (owner != None) and (capacityJet != None):
            ans = {"Brand" : brand, "Capacity" : capacityJet, "Owner" : owner}
            st.success("Jet creado con exito")
        elif jetButton and ((owner == None) or (capacityJet == None)):
            st.error("⛔Todos los campos son obligatorios")
            ans = 0
        else: ans = 0
        return ans
        
    def createHelicopter(self):
        ans = None
        brand = st.selectbox("Marca del Helicopter", ["Airbus Helicopters", "Bell"])

        if brand == "Airbus Helicopters":
            st.image("https://logovectordl.com/wp-content/uploads/2020/10/airbus-helicopters-logo-vector.png", caption="Blagnac, France")
            select = st.selectbox("Serie", ["Airbus H175M", "Airbus ACH160"])
            

            if select == "Airbus H175M":
                st.image("https://www.airforce-technology.com/wp-content/uploads/sites/6/2023/07/Featured-Image-H175M-helicopter.jpg", caption="Airbus x Boeing")
                numRotores = 1
                elevation = 12242
                use = "Fuerzas especiales"

            else:
                st.image("https://www.airbus.com/sites/g/files/jlcbta136/files/styles/airbus_608x608/public/2023-03/ACH160%20Exclusive%20-%20Copy.jpg?itok=hnOYYt3h", caption="Airbus ACH160", width=700)
                numRotores = 1
                elevation = 12242
                use = "Servicio de rescate"
        
        elif brand == "Bell":
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Bell_Helicopter_Logo.svg/2560px-Bell_Helicopter_Logo.svg.png", caption="New York, United States")
            select = st.selectbox("Serie", ["Bell 427", "Bell 429"])

            if select == "Bell 427":
                st.image("https://flight-way.com/upload/resize_cache/webp/iblock/f99/709_545_1/f99be5cfc693dab6666665efee185adf.webp", caption="Bell 427")
                numRotores = 1
                elevation = 12242
                use = "Turismo"

            else:
                st.image("https://d21buns5ku92am.cloudfront.net/67992/images/365357-ESGBell_429Rendering-d5a7cc-large-1600878707.jpg", caption="Bell 429", width=700)
                numRotores = 1
                elevation = 12242
                use = "Servicio de rescate"

        capacityHelicopter = st.number_input("Capacidad:", step=1, value=None)
        
        advance = st.button("Mostrar Configuracion Avanzada")

        helicopterConfig = {"Number of Rotors" : numRotores, "Max Elevation" : elevation, "Use" : use}

        if advance:
            st.table(helicopterConfig)
                
            if st.button("Cerrar"):
                advance = False
        hbutton = st.button("Crear helicoptero", type="primary")

        if hbutton and (capacityHelicopter != None):
            ans = {"Brand" : brand, "Capacity" : capacityHelicopter, "Number of Rotors" : numRotores, "Max Height" : elevation, "Use" : use}
            st.success("Helicoptero creado con exito")
        elif hbutton and (capacityHelicopter == None):
            st.error("⛔Todos los campos son obligatorios") 
            ans = 0
        else: ans = 0

        return ans
            
            
    def bookFlight(self):
        st.title("Reservar Vuelo")
        
    def showInfo(self):
        ans = 1
        st.title("Sistema Integrado De Consulta")
        select = st.selectbox("Seleccione el tipo de consulta", ["Consultar vuelos", "Consultar puertas", "Consultar aeronaves"])
        if select == "Consultar puertas":
            ans = 2
        elif select == "Consultar aeronaves":
            ans = 3
        return ans

    def showFlights(self, aeropuerto):
        if aeropuerto.empty():
            st.warning("⚠️ No hay vuelos")
        else: st.table(aeropuerto.destinations)
        
    def showAirplanes(self, aeropuerto):
        if aeropuerto.emptyAirplanes():
            st.warning("⚠️ No hay aviones")
        else: st.table(aeropuerto.avionesAeropuerto)

    def showJets(self, aeropuerto):
        if aeropuerto.emptyJets():
            st.warning("⚠️ No hay Jets")
        else: st.table(aeropuerto.jetsAeropuerto)

    def showHelicopters(self, aeropuerto):
        if aeropuerto.emptyHelicopters():
            st.warning("⚠️ No hay Helicopteros")
        else: st.table(aeropuerto.helicopterosAeropuerto)
        
    def registerPassenger(self, aeropuerto):
        st.title("Reservar Vuelo")
        if aeropuerto.empty():
            st.warning("⚠️ No hay vuelos")
            ans = 0
        else: 
            st.header("Registrar Pasajero")
            ans = 1
        return ans
            
            
    def passengerData(self):
        with st.form("Register Passenger"):
            nombre = st.text_input("Ingrese el nombre del pasajero: ")
            apellido = st.text_input("Ingrese el apellido del pasajero: ")
            edad = st.number_input("Ingrese la edad del pasajero: ", step=1, value=None)
            cedula = st.text_input("Ingrese la cedula del pasajero: ")
            fechaNacimiento = st.date_input("Ingrese la fecha de nacimiento del pasajero: ")
            genero = st.selectbox("Ingrese el genero del pasajero: ", ["Masculino", "Femenino"])
            direccion = st.text_input("Ingrese la direccion del pasajero: ")
            numTel = st.text_input("Ingrese el numero de telefono del pasajero: ")
            correo = st.text_input("Ingrese el correo del pasajero: ")
            nacionalidad = st.text_input("Pais de nacimiento: ")
            infoMedica = st.text_input("Ingrese la informacion medica del pasajero: ")
            numMaletasBodega = st.number_input("Ingrese el numero de maletas de bodega del pasajero: ", step=1, value=None)
            if st.form_submit_button("Registrarse",type="primary"):
                ans = {"Name" : nombre, "Last Name" : apellido, "Age" : edad, "id" : cedula, "Birth Day" : fechaNacimiento,
                        "Gender" : genero, "Address" : direccion, "Phone Number" : numTel, "Email" : correo, 
                        "Nationality" : nacionalidad, "Medical Info" : infoMedica, "Checked bags" : numMaletasBodega} 
            else: ans = 0
        return ans  
    
    def showAircraft(self):
        select = st.selectbox("Tipo de aeronave:", ["Avion", "Jet", "Helicoptero"])
        if select == "Avion":
            ans = 1
        elif select == "Jet":
            ans = 2
        elif select == "Helicoptero":
            ans = 3
        
        return ans
    
    def bookFlight(self, aeropuerto):
        st.title("Sistema de reserva de vuelo")
        self.showFlights(aeropuerto)
        option = st.number_input("Indice del vuelo a reservar:", step=1) 
        but = st.button("Reservar vuelo", type="primary")
        if but and (option < len(aeropuerto.vuelos)):
            ans = option
        elif but and (option >= len(aeropuerto.vuelos)):
            st.error("El indice debe estar en la tabla de vuelos")
            ans = -1
        else: 
            ans = -1
        return ans
    
    def sim(self, aeropuerto):
        st.title("Sistema Integrado de Simulación")
        simButton = st.button("Simular", type="primary")
        if simButton: 
            if ((len(aeropuerto.vuelos)) < 2):
                st.error("No se puede empezar la simulacion, No hay suficientes vuelos")
            elif ((len(aeropuerto.avionesAeropuerto)) + (len(aeropuerto.helicopterosAeropuerto)) + (len(aeropuerto.jetsAeropuerto)) < 2):
                st.error("No se puede empezar la simulacion, No hay suficientes aeronaves")
            else:
                aeropuerto.asignarVuelo()
                aeropuerto.torreControl.simulacion()
                st.balloons()
        st.info("Antes de simular se deben de haber creado 2 vuelos y 2 aeronaves como minimo")
            
    def getCountryInfo(self):
        st.title("Sistema Integrado de Consulta API")
        country = st.text_input("Nombre del pais:")
        country.lower()
        st.info("El pais a consultar debe estar escrito en Ingles")
        if st.button("Consultar", type="primary"):
            
            url = "https://restcountries.com/v3.1/name/" + country
            ans = requests.get(url)
            if ans.status_code == 200:

                    data = json.loads(ans.text)
                    name = data[0]["name"]["official"]
                    currency = data[0]["currencies"]
                    capital = data[0]["capital"][0]
                    region = data[0]["region"]
                    popu = data[0]["population"]
                    flag = data[0]["flags"]["png"]
                    dic = {"Name" : name, 
                            "Capital City" : capital,
                            "Continent" : region,
                            "Population" : popu}
                    st.header("Información general")
                    st.table(dic)
                    st.header("Moneda")
                    st.table(currency)
                    st.image(flag)
                    st.balloons()

            else:
                st.error("No se logró encontrar información del pais")

    def manageAirplanes(self, aeropuerto):
        ans = 0
        st.title("Gestionar Aviones")
        password = st.text_input("Ingrese la contraseña:", value=None)
        if password == "nomelase":
            numb = st.number_input("Ingrese el indice del avion que quiere gestionar: ", step=1)
            if numb < len(aeropuerto.avionesAeropuerto):
                op = st.selectbox("Seleccione una opcion:", ["Disponible", "Mantenimiento"])
                
                if op == "Mantenimiento":
                    ans = [1, numb]
                elif op == "Disponible":
                    ans = [2, numb]
        elif password != None:
            st.error("Contraseña Incorrecta")

        return ans