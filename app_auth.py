import streamlit as st
from streamlit_authenticator import Authenticate
import streamlit as st
# Importation du module
from streamlit_option_menu import option_menu
import seaborn as sns
import matplotlib.pyplot as plt


lesDonneesDesComptes = {'usernames': {'kitty': {'name': 'kitty kat',
   'password': '1234',
   'email': 'kitty.kat@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)
authenticator.login()

def home_page():
    st.subheader(":rainbow[Welcome to the home page of my photos]")
    st.image("rainbow.jpg")
    st.write("That was a beatiful rainbow from my window")

def photos():
    st.subheader("Welcome to my cat album")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("A sleeping cat")
        st.image("cat1.jpg")

    with col2:
        st.write("A cat that wants attention")
        st.image("cat2.jpg")

    with col3:
        st.write("A cat is going to a date")
        st.image("cat3.jpg")

def seaborn_stuff():
    list_datasets = sns.get_dataset_names()
    st.header("Data manipulation and dataviz")
    st.write("Which dataset are we going to use?")
    dataset  = st.selectbox("", list_datasets)
    df = sns.load_dataset(dataset)
    st.dataframe(df.head(20))
    x_axis  = st.selectbox("Now I want you to chose X axis", df.columns)
    y_axis  = st.selectbox("Without Y axis there is no fun. Please chose it as well", df.columns)
    graph = st.selectbox("Which type of graph are we going to use", 
                            ["bar", "scatter", "line"])

    eval(f"st.{graph}_chart(df, x = x_axis, y = y_axis)")   

    matrix = st.checkbox('Do you want me to show you correlation matrix?')
    if matrix:
        if (df[x_axis].dtype in ["float64", "int64"]) and (df[y_axis].dtype in ["float64", "int64"]):
            sns.heatmap(df[[f"{x_axis}", f"{y_axis}"]].corr(),  annot=True)
            st.pyplot(plt.gcf())
        else:
            st.markdown(f"#### :red[You need to chose numeric columns. Chose between these {df.select_dtypes(['float64', 'int64']).columns.values}]")
  

def accueil():
    with st.sidebar:
         # Le bouton de déconnexion
        authenticator.logout("Deconnect")
        selection = option_menu(
            menu_title=None,
            options = ["🌈 Home page", "🐈 Photos", "🌊  Seaborn stuff"]
        )
    if selection == "🌈 Home page":
        home_page()
        
    elif selection == "🐈 Photos":
        photos()

    elif selection == "🌊  Seaborn stuff":
        seaborn_stuff()


if st.session_state["authentication_status"]:
    accueil()

elif st.session_state["authentication_status"] is False:
    st.error("Name or password is incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('You need to fill name and password fields')


