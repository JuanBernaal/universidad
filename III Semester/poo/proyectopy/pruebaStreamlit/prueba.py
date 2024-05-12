import streamlit as st

st.title("This is an example")
inpt = st.text_input("Introduce algo: ")
st.text("Hello World")
activated = st.toggle("Activate")
st.link_button("DO NOT PRESS ME", "https://www.youtube.com/watch?v=xvFZjo5PgG0", type="primary") 

st.sidebar.write("This lives in the sidebar")
if (st.sidebar.button("Click me!")):
    st.text("Si")

st.latex("e^x * y^2")

data = [
    {"Elemento" : "Lo que quiera", "Asi si": 3},
    {"Elemento" : "Lo que quiera", "Asi si" : 3}
]

st.table(data)

st.warning("Unable to fetch image. Skipping...", icon="⚠️")

st.number_input("Ingrese un numero", min_value=1)

fecha = st.date_input("Fecha del vuelo")

st.write(fecha)

hora = st.time_input("Hora del vuelo")

st.write(hora)

nombre = "Juan"
edad = 15

# Variable de estado para controlar la visualización del formulario
show_form = st.button("Show more")

if show_form:
    with st.form("Mi formulario"):
        # Agregar elementos del formulario
        nombre = st.text_input("Nombre")
        edad = st.number_input("Edad", min_value=0, max_value=100)
        # Crear un botón de envío específico del formulario
        submitted = st.form_submit_button("Enviar formulario")

    # Verificar si el formulario fue enviado
        if submitted:
            # Realizar acciones asociadas con el envío del formulario
            st.write(f"¡El formulario fue enviado! Nombre: {nombre}, Edad: {edad}")
            st.info("Guardado")
st.write(nombre, edad)

