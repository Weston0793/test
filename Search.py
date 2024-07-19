import streamlit as st
from google.cloud import firestore
from firebase_helpers import db, create_zip
import uuid
from google.api_core.exceptions import GoogleAPICallError
from search_backend import perform_search
from helper_functions import style_markdown, select_subregion, select_sub_subregion, select_sub_sub_subregion

def initialize_session_state():
    if 'search_button_clicked' not in st.session_state:
        st.session_state.search_button_clicked = False
    if 'query_params' not in st.session_state:
        st.session_state.query_params = {
            "search_button_clicked": False,
            "type": "",
            "view": "",
            "main_region": "",
            "sub_region": "",
            "sub_sub_region": "",
            "sub_sub_sub_region": "",
            "complications": [],
            "associated_conditions": [],
            "age_filter_active": False,
            "age": "",
            "age_group": "",
            "page": 1,
            "items_per_page": 10
        }

def search_section():
    initialize_session_state()
    style_markdown()
    st.markdown('<div class="search-title">Képek keresése</div>', unsafe_allow_html=True)

    types = ["", "Normál", "Törött", "Egyéb"]
    views = ["", "AP", "Lateral", "Ferde", "PA", "Speciális"]
    regions = ["", "Felső végtag", "Alsó végtag", "Gerinc", "Koponya", "Mellkas", "Has"]

    # Type and view in one row
    col1, col2 = st.columns(2)
    with col1:
        search_type = st.selectbox("Típus keresése", types, index=types.index(st.session_state.query_params["type"]))
    with col2:
        search_view = st.selectbox("Nézet keresése", views, index=views.index(st.session_state.query_params["view"]))

    # Main and sub region in one row
    col3, col4 = st.columns(2)
    with col3:
        search_main_region = st.selectbox("Fő régió keresése", regions, index=regions.index(st.session_state.query_params["main_region"]))
    with col4:
        search_sub_region = select_subregion(search_main_region)

    # Sub-subregion and sub-sub-subregion in one row
    col5, col6 = st.columns(2)
    with col5:
        search_sub_sub_region = select_sub_subregion(search_sub_region)
    with col6:
        search_sub_sub_sub_region = select_sub_sub_subregion(search_sub_sub_region)

    # Multiselects for complications and associated conditions
    search_complications = st.multiselect("Komplikációk keresése", ["Nyílt", "Darabos", "Avulsio", "Luxatio", "Subluxatio", "Idegsérülés", "Nagyobb Érsérülés", "Szalagszakadás", "Meniscus Sérülés", "Epiphysis Sérülés", "Fertőzés"], default=st.session_state.query_params["complications"])
    search_associated_conditions = st.multiselect("Társuló Kórállapotok keresése", ["Osteoarthritis", "Osteoporosis", "Osteomyelitis", "Rheumatoid Arthritis", "Cysta", "Metastasis", "Malignus Tumor", "Benignus Tumor", "Genetikai"], default=st.session_state.query_params["associated_conditions"])

    # Age filter with checkbox
    age_filter_active = st.checkbox("Életkor keresése (intervallum)", value=st.session_state.query_params["age_filter_active"])
    if age_filter_active:
        search_age = st.slider("Életkor keresése (intervallum)", min_value=0, max_value=120, value=eval(st.session_state.query_params["age"]), step=1, format="%d")
    else:
        search_age = None

    search_age_group = st.selectbox("Életkori csoport keresése", ["", "Gyermek", "Felnőtt"], index=["", "Gyermek", "Felnőtt"].index(st.session_state.query_params["age_group"]))

    # Page and items per page in one row
    col7, col8 = st.columns(2)
    with col7:
        page = st.number_input("Oldal", min_value=1, step=1, value=st.session_state.query_params["page"])
    with col8:
        items_per_page = st.selectbox("Találatok száma oldalanként", options=[10, 25, 50, 100], index=[10, 25, 50, 100].index(st.session_state.query_params["items_per_page"]))

    # Button for search
    search_button_clicked = st.button("Keresés", key="search_button")

    if search_button_clicked:
        page = 1  # Reset to the first page on new search
        st.session_state.search_button_clicked = True
        st.session_state.query_params = {
            "search_button_clicked": True,
            "type": search_type,
            "view": search_view,
            "main_region": search_main_region,
            "sub_region": search_sub_region,
            "sub_sub_region": search_sub_sub_region,
            "sub_sub_sub_region": search_sub_sub_sub_region,
            "complications": search_complications,
            "associated_conditions": search_associated_conditions,
            "age_filter_active": age_filter_active,
            "age": str(search_age) if search_age else "",
            "age_group": search_age_group,
            "page": page,
            "items_per_page": items_per_page
        }
        st.experimental_rerun()

    if st.session_state.search_button_clicked:
        perform_search(st.session_state.query_params)

if __name__ == "__main__":
    search_section()
