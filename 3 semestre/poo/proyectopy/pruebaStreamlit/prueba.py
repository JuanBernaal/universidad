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