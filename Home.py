import streamlit as st
from home_backend import handle_file_upload, confirm_and_upload_data
import uuid
from Styles import upload_markdown
from helper_functions import (
    select_main_type, select_view, select_main_region, 
    select_subregion, select_sub_subregion, select_sub_sub_subregion, 
    select_sub_sub_sub_subregion, select_finger, select_complications, 
    select_associated_conditions, ao_classification, neer_classification, gartland_classification
)

def initialize_home_session_state():
    if 'confirm_data' not in st.session_state:
        st.session_state.confirm_data = None
    if 'regions' not in st.session_state:
        st.session_state.regions = [{'main_region': None, 'side': None, 'sub_region': None, 'sub_sub_region': None, 'sub_sub_sub_region': None, 'sub_sub_sub_sub_region': None, 'finger': None}]
    if 'adding_multiple' not in st.session_state:
        st.session_state.adding_multiple = False

def main():
    initialize_home_session_state()
    upload_markdown()
    st.markdown('<div class="upload-title">Orvosi Röntgenkép Adatbázis</div>', unsafe_allow_html=True)

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

        age = st.select_slider("Életkor (opcionális)", options=["NA"] + list(range(0, 121)), value="NA")
        age_group = ""
        if age != "NA":
            age = int(age)
            age_group = "Gyermek" if age <= 18 else "Felnőtt"

        if main_type != "Normál":
            complications = select_complications()
            associated_conditions = select_associated_conditions()

        classification_types = st.multiselect("Válassza ki az osztályozás típusát", ["AO", "Gartland", "Neer"])

        comment = st.text_area("Megjegyzés (opcionális)", key="comment", value="")

        st.markdown("### Sérült Régiók Kiválasztása")

        def add_region():
            if st.session_state.regions:
                previous_region = st.session_state.regions[-1]
            else:
                previous_region = {}

            new_region = {
                'main_region': previous_region.get('main_region', None),
                'side': previous_region.get('side', None),
                'sub_region': previous_region.get('sub_region', None),
                'sub_sub_region': previous_region.get('sub_sub_region', None),
                'sub_sub_sub_region': previous_region.get('sub_sub_sub_region', None),
                'sub_sub_sub_sub_region': previous_region.get('sub_sub_sub_sub_region', None),
                'finger': previous_region.get('finger', None)
            }

            with st.container():
                col3, col4, col5 = st.columns([1, 1, 1])
                with col3:
                    main_region = select_main_region()
                    new_region['main_region'] = main_region
                if main_region:
                    if main_region in ["Felső végtag", "Alsó végtag"]:
                        with col4:
                            side = st.selectbox("Oldal", ["Bal", "Jobb"])
                            new_region['side'] = side
                    else:
                        new_region['side'] = None
                    with col5:
                        sub_region = select_subregion(main_region)
                        new_region['sub_region'] = sub_region

                sub_sub_region = None
                sub_sub_sub_region = None
                sub_sub_sub_sub_region = None
                finger = None
                if sub_region:
                    with st.container():
                        col6, col7, col8, col9 = st.columns([1, 1, 1, 1])
                        with col6:
                            sub_sub_region = select_sub_subregion(sub_region)
                            new_region['sub_sub_region'] = sub_sub_region
                        if sub_sub_region:
                            with col7:
                                sub_sub_sub_region = select_sub_sub_subregion(sub_sub_region)
                                new_region['sub_sub_sub_region'] = sub_sub_sub_region
                        if sub_sub_sub_region:
                            with col9:
                                if sub_sub_sub_region in ["Metacarpus", "Phalanx", "Metatarsus", "Lábujjak", "Pollex", "Hallux"]:
                                    finger, _ = select_finger(sub_sub_sub_region)
                                    new_region['finger'] = finger
                                else:
                                    new_region['finger'] = None
                            with col8:
                                sub_sub_sub_sub_region = select_sub_sub_sub_subregion(sub_sub_sub_region)
                                new_region['sub_sub_sub_sub_region'] = sub_sub_sub_sub_region
                        else:
                            new_region['sub_sub_sub_sub_region'] = None

            st.session_state.regions.append(new_region)

        # Ensure there is always at least one region to select
        if not st.session_state.regions or st.session_state.regions[0]['main_region'] is None:
            add_region()

        if st.button("Mentés s új régió hozzáadása"):
            st.session_state.adding_multiple = True
            add_region()

        st.markdown("### Kiválasztott régiók")
        for idx, region in enumerate(st.session_state.regions):
            st.markdown(f"**Régió {idx + 1}:**")
            st.markdown(f"**Fő régió:** {region['main_region']}")
            if region['side']:
                st.markdown(f"**Oldal:** {region['side']}")
            st.markdown(f"**Alrégió:** {region['sub_region']}")
            if region['sub_sub_region']:
                st.markdown(f"**Részletes régió:** {region['sub_sub_region']}")
            if region['sub_sub_sub_region']:
                st.markdown(f"**Legpontosabb régió:** {region['sub_sub_sub_region']}")
            if region['finger']:
                st.markdown(f"**Ujj:** {region['finger']}")
            if region['sub_sub_sub_sub_region']:
                st.markdown(f"**Legrészletesebb régió:** {region['sub_sub_sub_sub_region']}")

        if st.button("Feltöltés"):
            upload_data = {
                "patient_id": patient_id,
                "main_type": main_type,
                "sub_type": sub_type,
                "sub_sub_type": sub_sub_type,
                "view": view,
                "sub_view": sub_view,
                "sub_sub_view": sub_sub_view,
                "age": age,
                "age_group": age_group,
                "comment": comment,
                "file": uploaded_file,
                "complications": complications if main_type != "Normál" else [],
                "associated_conditions": associated_conditions if main_type != "Normál" else [],
                "classifications": classifications,
                "regions": st.session_state.regions
            }
            st.session_state.confirm_data = upload_data
            st.experimental_rerun()

        if st.session_state.confirm_data:
            confirm_and_upload_data(st.session_state.confirm_data)

    if st.experimental_get_query_params().get("scroll_to") == ["confirmation"]:
        st.markdown('<script>window.scrollTo(0, document.body.scrollHeight);</script>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
