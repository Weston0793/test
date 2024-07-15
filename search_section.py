import streamlit as st
from firebase_helpers import db, create_zip
import uuid
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

    st.markdown('<div class="search-box">', unsafe_allow_html=True)
    st.markdown('<div class="search-title">Képek keresése</div>', unsafe_allow_html=True)

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
