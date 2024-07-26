import streamlit as st
from multipage import MultiPage
from Upload import main as upload
from Search import search_section as search
from Status import main as status
from Contact import main as contact
from Home import main as home
# CSS stílus a navigációs sávhoz
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
            padding: 20px;
            border: 2px solid #000;
            border-radius: 10px;
        }
        .sidebar .sidebar-content .selectbox {
            font-size: 18px;
        }
        .sidebar .sidebar-content .stSelectbox {
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)
app = MultiPage()

# Add all your applications (pages) here with emojis as icons
app.add_page("Főoldal", home, icon="🏠")
app.add_page("Kép feltöltése", upload, icon="📤")
app.add_page("Képek keresése", search, icon="🔍")
app.add_page("Státusz", status, icon="📊")
app.add_page("Elérhetőség", contact, icon="✉️")

# The main app
if __name__ == '__main__':
      app.run()

