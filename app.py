import streamlit as st
import os
import uuid
import io
import zipfile
import firebase_admin
from firebase_admin import credentials, firestore, storage
from PIL import Image

import streamlit as st
from firebase_helpers import save_image, create_zip, db
import uuid

def confirm_popup(upload_data):
    st.session_state["confirm"] = st.checkbox("Ne kérdezzen többé")
    if not st.session_state.get("confirm", False):
        st.warning(
            "Megerősíti a következő adatokat?\n"
            f"Beteg azonosító: {upload_data['patient_id']}\n"
            f"Típus: {upload_data['type']}\n"
            f"Nézet: {upload_data['view']}\n"
            f"Fő régió: {upload_data['main_region']}\n"
            f"Alrégió: {upload_data['sub_region']}\n"
            f"Életkor: {upload_data['age']}\n"
            f"Megjegyzés: {upload_data['comment']}"
        )
        return st.button("Megerősít")
    return True

def upload_section():
    st.markdown(
        """
        <style>
        .upload-box {
            border: 2px solid black;
            padding: 20px;
            margin-bottom: 20px;
            text-align: center;
        }
        .upload-title {
            font-size: 24px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="upload-box"><div class="upload-title">Kép feltöltése és címkézése</div>', unsafe_allow_html=True)

    patient_id = st.text_input("Beteg azonosító (hagyja üresen új beteg esetén)", str(uuid.uuid4()))

    uploaded_file = st.file_uploader("Válassz egy képet", type=["jpg", "jpeg", "png"])

    type = st.selectbox("Típus", ["Törött", "Normál", "Egyéb"])
    type_comment = st.text_input("Specifikálás (Egyéb)") if type == "Egyéb" else ""

    view = st.selectbox("Nézet", ["AP", "Lateral", "Egyéb"])
    view_comment = st.text_input("Specifikálás (Egyéb Nézet)") if view == "Egyéb" else ""

    main_region = st.selectbox("Fő régió", ["Felső végtag", "Alsó végtag", "Gerinc", "Koponya"])

    if main_region == "Felső végtag":
        sub_region = st.selectbox("Alrégió", ["Clavicula", "Scapula", "Váll", "Humerus", "Könyök", "Radius", "Ulna", "Csukló", "Kéz"])
    elif main_region == "Alsó végtag":
        sub_region = st.selectbox("Alrégió", ["Csípő", "Comb", "Térd", "Tibia", "Fibula", "Boka", "Láb"])
    elif main_region == "Gerinc":
        sub_region = st.selectbox("Alrégió", ["Nyaki", "Háti", "Ágyéki", "Kereszt- és farokcsonti"])
    elif main_region == "Koponya":
        sub_region = st.selectbox("Alrégió", ["Arckoponya", "Agykoponya", "Állkapocs"])
    else:
        sub_region = ""

    age = st.slider("Életkor", min_value=0, max_value=120, step=1, format="%d", value=0)
    comment = st.text_area("Megjegyzés", key="comment", value="")

    if st.button("Feltöltés"):
        if uploaded_file and type and view and main_region and sub_region:
            upload_data = {
                "patient_id": patient_id,
                "type": type,
                "view": view,
                "main_region": main_region,
                "sub_region": sub_region,
                "age": age,
                "comment": comment + " " + type_comment + " " + view_comment,
                "file": uploaded_file
            }

            if confirm_popup(upload_data):
                try:
                    save_image(**upload_data)
                    st.success("Kép sikeresen feltöltve!")
                except Exception as e:
                    st.error(f"Hiba a kép mentésekor: {e}")
        else:
            st.error("Tölts fel egy képet és add meg a szükséges információkat.")

    st.markdown('</div>', unsafe_allow_html=True)

def search_section():
    st.markdown(
        """
        <style>
        .search-box {
            border: 2px solid black;
            padding: 20px;
            margin-bottom: 20px;
        }
        .search-title {
            font-size: 24px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="search-box"><div class="search-title">Képek keresése</div>', unsafe_allow_html=True)

    search_labels = st.text_input("Keresés címkék alapján (vesszővel elválasztva)")

    search_type = st.selectbox("Típus keresése", ["", "Törött", "Normál"])
    search_view = st.selectbox("Nézet keresése", ["", "AP", "Lateral"])
    search_main_region = st.selectbox("Fő régió keresése", ["", "Felső végtag", "Alsó végtag", "Gerinc", "Koponya"])

    if search_main_region == "Felső végtag":
        search_sub_region = st.selectbox("Alrégió keresése", ["", "Clavicula", "Scapula", "Váll", "Humerus", "Könyök", "Radius", "Ulna", "Csukló", "Kéz"])
    elif search_main_region == "Alsó végtag":
        search_sub_region = st.selectbox("Alrégió keresése", ["", "Csípő", "Comb", "Térd", "Tibia", "Fibula", "Boka", "Láb"])
    elif search_main_region == "Gerinc":
        search_sub_region = st.selectbox("Alrégió keresése", ["", "Nyaki", "Háti", "Ágyéki", "Kereszt- és farokcsonti"])
    elif search_main_region == "Koponya":
        search_sub_region = st.selectbox("Alrégió keresése", ["", "Arckoponya", "Agykoponya", "Állkapocs"])
    else:
        search_sub_region = ""

    if st.button("Keresés"):
        results = db.collection('images')

        if search_labels:
            for label in search_labels.split(","):
                results = results.where('type', '==', label.strip())

        if search_type:
            results = results.where('type', '==', search_type)
        if search_view:
            results = results.where('view', '==', search_view)
        if search_main_region:
            results = results.where('main_region', '==', search_main_region)
        if search_sub_region:
            results = results.where('sub_region', '==', search_sub_region)

        docs = results.stream()
        file_paths = []

        for doc in docs:
            data = doc.to_dict()
            st.image(data['url'], caption=f"{data['type']}, {data['view']}, {data['main_region']}, {data['sub_region']}")
            file_paths.append(data['url'])

        if file_paths:
            zip_buffer = create_zip(file_paths)
            st.download_button(
                label="Képek letöltése ZIP-ben",
                data=zip_buffer,
                file_name="images.zip",
                mime="application/zip"
            )

    st.markdown('</div>', unsafe_allow_html=True)

def main():
    st.title("Orvosi Röntgen Adatbázis")
    upload_section()
    search_section()

if __name__ == "__main__":
    main()
