import streamlit as st
from multipage import MultiPage
from Upload import main as upload
from Search import search_section as search
from Status import main as status
from Contact import main as contact
from Home import main as home

app = MultiPage()

# Add all your applications (pages) here with Material Symbols icons
app.add_page("Home", home, icon=":material/home:")
app.add_page("Upload Image", upload, icon=":material/cloud_upload:")
app.add_page("Search Images", search, icon=":material/search:")
app.add_page("Status", status, icon=":material/insights:")
app.add_page("Contact", contact, icon=":material/contact_mail:")

# The main app
if __name__ == '__main__':
    app.run()
