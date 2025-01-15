import streamlit as st
import pandas as pd
from datetime import date, time
import seaborn as sns
st.audio("music.mp3")

df = sns.load_dataset("taxis")
list_zone = df.pickup_borough.unique()
st.title("Bienvenue sur le site web de Iuliia")

st.markdown('''#### Indiquez votre arrondissement de recuperation''')

quartal = st.selectbox("", list_zone)

if type(quartal) is str:
    st.markdown(f"#### Tu as choisis: {quartal}")

if quartal == "Manhattan":
    st.image("manh.jpg")
elif quartal == "Queens":
    st.image("queens.jpg")
elif quartal == "Bronx":
    st.image("bronx.jpg")
elif quartal == "Brooklyn":
    st.image("brooklyn.jpg")
else:
    st.image("wtf.jpg")
#st.dataframe(df.pickup_borough.unique().values, use_container_width=True)
