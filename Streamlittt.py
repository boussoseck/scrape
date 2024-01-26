import streamlit as st
import pandas as pd
# Fonctions pour chaque page


def page_scrap():
    st.title("Données Web_Scrapping")

   


def page_web():
    st.title("Donnees Web Scrapping")
    st.write("Choisissez le tableaux")

    # Charger les données
    chaussures_hom = pd.read_csv("type.csv")
    vet_hom = pd.read_csv("vetment_hom.csv")
    vetements_enfants = pd.read_csv("vetements_enfants.csv")
    chaussure_enfants = pd.read_csv("chaussures_enfant.csv")

    # Afficher les informations
    st.header("chaussures_hom")
    st.write(chaussures_hom)

    st.header("vet_hom")
    st.write(vet_hom)

    st.header("vetements_enfants ")
    st.write(vetements_enfants)

    st.header("chaussure_enfants ")
    st.write(chaussure_enfants)

def page_dash():

    st.title("Données Web Scrapping")
    st.write("Voici les differents graphiques  ")

    
pages = {
    "Donnees Beautifulsoup": page_scrap,
    "Donnees Web Scrappin": page_web,
    "Dash Board": page_dash,
}

selection = st.sidebar.radio("Navigation", list(pages.keys()))

# Afficher la page sélectionnée
pages[selection]()
