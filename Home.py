import streamlit as st
from home_backend import handle_file_upload, confirm_and_upload_data
import uuid
from helper_functions import (
    select_main_type, select_view, select_main_region, 
    select_subregion, select_sub_subregion, select_sub_sub_subregion, 
    select_complications, select_associated_conditions
)
from Styles import upload_markdown

def initialize_home_session_state():
    if 'confirm_data' not in st.session_state:
        st.session_state.confirm_data = None

def upload_markdown():
    st.markdown('<div class="upload-title">Orvosi Röntgenkép Adatbázis</div>', unsafe_allow_html=True)

def main():
    initialize_home_session_state()
    upload_markdown()

    patient_id = str(uuid.uuid4())
    st.text_input("Beteg azonosító", patient_id, disabled=True)

    st.markdown('<div class="file-upload-instruction">Kérem húzzon az alábbi ablakra vagy válasszon ki a fájlkezelőn keresztül egy röntgenképet (Max 15 MB)</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Fájl kiválasztása", type=["jpg", "jpeg", "png"], accept_multiple_files=False)

    if uploaded_file is not None:
        uploaded_file = handle_file_upload(uploaded_file)

    if uploaded_file:
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

        if main_type != "Normál":
            complications = select_complications()
            associated_conditions = select_associated_conditions()

        age = st.select_slider("Életkor (opcionális)", options=["NA"] + list(range(0, 121)), value="NA")
        age_group = ""
        if age != "NA":
            age = int(age)
            age_group = "Gyermek" if age <= 18 else "Felnőtt"

        comment = st.text_area("Megjegyzés (opcionális)", key="comment", value="")

        if st.button("Feltöltés"):
            upload_data = {
                "patient_id": patient_id,
                "main_type": main_type,
                "sub_type": sub_type,
                "sub_sub_type": sub_sub_type,
                "view": view,
                "sub_view": sub_view,
                "sub_sub_view": sub_sub_view,
                "main_region": main_region,
                "sub_region": sub_region if main_type != "Normál" else "",
                "sub_sub_region": sub_sub_region if sub_sub_region != "NA" else "",
                "sub_sub_sub_region": sub_sub_sub_region if sub_sub_sub_region != "NA" else "",
                "age": age,
                "age_group": age_group,
                "comment": comment,
                "file": uploaded_file,
                "complications": complications if main_type != "Normál" else [],
                "associated_conditions": associated_conditions if main_type != "Normál" else []
            }
            st.session_state.confirm_data = upload_data
            st.experimental_rerun()

        if st.session_state.confirm_data:
            confirm_and_upload_data(st.session_state.confirm_data)

    if st.experimental_get_query_params().get("scroll_to") == ["confirmation"]:
        st.markdown('<script>window.scrollTo(0, document.body.scrollHeight);</script>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
