import streamlit as st
from multipage import MultiPage, nav_page
from Upload import main as upload
from Search import search_section as search
from Status import main as status
from Contact import main as contact
from Home import main as home

app = MultiPage()

# Add all your applications (pages) here
app.add_page("Főoldal", home)
app.add_page("Kép feltöltése", upload)
app.add_page("Képek keresése", search)
app.add_page("Státusz", status)
app.add_page("Elérhetőség", contact)

# Example usage of nav_page in buttons within a page function
def home():
    st.title("Főoldal")
    if st.button("Next >"):
        nav_page("Kép feltöltése")

def upload():
    st.title("Kép feltöltése")
    if st.button("< Prev"):
        nav_page("Főoldal")
    if st.button("Next >"):
        nav_page("Képek keresése")

def search():
    st.title("Képek keresése")
    if st.button("< Prev"):
        nav_page("Kép feltöltése")
    if st.button("Next >"):
        nav_page("Státusz")

def status():
    st.title("Státusz")
    if st.button("< Prev"):
        nav_page("Képek keresése")
    if st.button("Next >"):
        nav_page("Elérhetőség")

def contact():
    st.title("Elérhetőség")
    if st.button("< Prev"):
        nav_page("Státusz")

# The main app
if __name__ == '__main__':
    app.run()
