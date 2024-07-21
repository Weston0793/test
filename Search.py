import streamlit as st
from google.cloud import firestore
from firebase_helpers import db, create_zip
import uuid
from google.api_core.exceptions import GoogleAPICallError
from search_backend import perform_search
from helper_functions import (
    select_main_type, select_view, select_subregion, 
    select_sub_subregion, select_sub_sub_subregion, select_complications, select_associated_conditions
)
from Styles import search_markdown

def initialize_session_state():
    if 'search_button_clicked' not in st.session_state:
        st.session_state.search_button_clicked = False
    if 'query_params' not in st.session_state:
        st.session_state.query_params = {
            "search_button_clicked": False,
            "main_type": "",
            "sub_type": "",
            "sub_sub_type": "",
            "view": "",
            "sub_view": "",
            "sub_sub_view": "",
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
    search_markdown()
    st.markdown('<div class="search-title">Képek keresése</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        main_type, sub_type, sub_sub_type = select_main_type()
    with col2:
        view, sub_view, sub_sub_view = select_view()

    col3, col4 = st.columns(2)
    with col3:
        main_region = select_main_region()
    with col4:
        sub_region = select_subregion(main_region)

    col5, col6 = st.columns(2)
    with col5:
        sub_sub_region = select_sub_subregion(sub_region)
    with col6:
        sub_sub_sub_region = select_sub_sub_subregion(sub_sub_region)

    complications = select_complications()
    
    associated_conditions = select_associated_conditions()

    age_filter_active = st.checkbox("Életkor keresése (intervallum)", value=st.session_state.query_params["age_filter_active"])
    age_group = st.selectbox("Életkori csoport keresése", ["", "Gyermek", "Felnőtt"], index=["", "Gyermek", "Felnőtt"].index(st.session_state.query_params["age_group"]))

    if age_filter_active:
        if age_group == "Gyermek":
            age = st.slider("Életkor keresése (intervallum)", min_value=0, max_value=18, value=(0, 18), step=1, format="%d")
        elif age_group == "Felnőtt":
            age = st.slider("Életkor keresése (intervallum)", min_value=19, max_value=120, value=(19, 120), step=1, format="%d")
        else:
            try:
                age_value = eval(st.session_state.query_params["age"]) if st.session_state.query_params["age"] else (0, 120)
            except ValueError:
                age_value = (0, 120)
            age = st.slider("Életkor keresése (intervallum)", min_value=0, max_value=120, value=age_value, step=1, format="%d")
    else:
        age = None

    col7, col8 = st.columns(2)
    with col7:
        page = st.number_input("Oldal", min_value=1, step=1, value=st.session_state.query_params["page"])
    with col8:
        items_per_page = st.selectbox("Találatok száma oldalanként", options=[10, 25, 50, 100], index=[10, 25, 50, 100].index(st.session_state.query_params["items_per_page"]))

    search_button_clicked = st.button("Keresés", key="search_button")

    if search_button_clicked:
        page = 1
        st.session_state.search_button_clicked = True
        st.session_state.query_params = {
            "search_button_clicked": True,
            "main_type": main_type,
            "sub_type": sub_type,
            "sub_sub_type": sub_sub_type,
            "view": view,
            "sub_view": sub_view,
            "sub_sub_view": sub_sub_view,
            "main_region": main_region,
            "sub_region": sub_region,
            "sub_sub_region": sub_sub_region,
            "sub_sub_sub_region": sub_sub_sub_region,
            "complications": complications,
            "associated_conditions": associated_conditions,
            "age_filter_active": age_filter_active,
            "age": str(age) if age else "",
            "age_group": age_group,
            "page": page,
            "items_per_page": items_per_page
        }
        st.experimental_rerun()

    if st.session_state.search_button_clicked:
        perform_search(st.session_state.query_params)

if __name__ == "__main__":
    search_section()
