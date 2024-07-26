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

# Example usage of nav_page in buttons
if st.button("< Prev"):
    nav_page("Főoldal")
if st.button("Next >"):
    nav_page("Kép feltöltése")

# The main app
if __name__ == '__main__':
    app.run()
