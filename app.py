import streamlit as st
from multipage import MultiPage
from Upload import main as upload
from Search import search_section as search
from Status import main as status
from Contact import main as contact
from Home import main as home

app = MultiPage()

# Add all your applications (pages) here with emojis as icons
app.add_page("Home", home, icon="🏠")
app.add_page("Upload Image", upload, icon="📤")
app.add_page("Search Images", search, icon="🔍")
app.add_page("Status", status, icon="📊")
app.add_page("Contact", contact, icon="✉️")

# The main app
if __name__ == '__main__':
      app.run()

