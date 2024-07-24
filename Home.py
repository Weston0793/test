import streamlit as st
from home_backend import handle_file_upload, confirm_and_upload_data
import uuid
from helper_functions import (
    select_main_type, select_view, select_main_region, 
    select_subregion, select_sub_subregion, select_sub_sub_subregion, 
    select_sub_sub_sub_subregion, select_finger, select_complications, 
    select_associated_conditions, ao_classification, neer_classification, gartland_classification
)
from Styles import upload_markdown

def initialize_home_session_state():
    if 'confirm_data' not in st.session_state:
        st.session_state.confirm_data = None
    if 'regions' not in st.session_state:
        st.session_state.regions = [{'main_region': None, 'side': None, 'sub_region': None, 'sub_sub_region': None, 'sub_sub_sub_region': None, 'sub_sub_sub_sub_region': None, 'finger': None, 'editable': True}]
    if 'patient_id' not in st.session_state:
        st.session_state.patient_id = str(uuid.uuid4())
    if 'multi_region' not in st.session_state:
        st.session_state.multi_region = False
    if 'new_region_blocked' not in st.session_state:
        st.session_state.new_region_blocked = False
    if 'multi_image_upload' not in st.session_state:
        st.session_state.multi_image_upload = False
    if 'new_image_uploaded' not in st.session_state:
        st.session_state.new_image_uploaded = False

def reset_session_state():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    initialize_home_session_state()
    st.experimental_rerun()

def main():
    initialize_home_session_state()
    upload_markdown()
    st.markdown('<div class="upload-title">Orvosi Röntgenkép Adatbázis</div>', unsafe_allow_html=True)

    if st.checkbox("Több kép feltöltése ugyanazokkal a beállításokkal", value=st.session_state.multi_image_upload):
        st.session_state.multi_image_upload = True
        st.warning("Több kép feltöltése aktiválva! Minden új kép új azonosítót kap.")
    else:
        st.session_state.multi_image_upload = False

    st.text_input("Beteg azonosító", st.session_state.patient_id, disabled=True)

    st.markdown('<div class="file-upload-instruction">Kérem húzzon az alábbi ablakra vagy válasszon ki a fájlkezelőn keresztül egy röntgenképet (Max 15 MB)</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Fájl kiválasztása", type=["jpg", "jpeg", "png"], accept_multiple_files=False)

    if uploaded_file is not None and not st.session_state.new_image_uploaded:
        uploaded_file = handle_file_upload(uploaded_file)
        if uploaded_file:
            st.session_state.uploaded_file = uploaded_file
            st.session_state.new_region_blocked = False
            st.session_state.new_image_uploaded = True
            if not st.session_state.multi_image_upload:
                st.session_state.regions = [{'main_region': None, 'side': None, 'sub_region': None, 'sub_sub_region': None, 'sub_sub_sub_region': None, 'sub_sub_sub_sub_region': None, 'finger': None, 'editable': True}]
            st.session_state.patient_id = str(uuid.uuid4())
            st.experimental_rerun()

    if 'uploaded_file' in st.session_state:
        st.image(st.session_state.uploaded_file, caption="Feltöltött kép", use_column_width=True)
        
        col1, col2 = st.columns(2)
        with col1:
            main_type, sub_type, sub_sub_type = select_main_type()

        with col2:
            view, sub_view, sub_sub_view = select_view()

        st.markdown("### Sérült Régiók Kiválasztása")

        col_checkbox, col_button = st.columns([1, 1])
        with col_checkbox:
            st.session_state.multi_region = st.checkbox("Több régió jelölése", value=st.session_state.multi_region)
        
        with col_button:
            if st.session_state.multi_region:
                if st.button("Új régió hozzáadása") and not st.session_state.new_region_blocked:
                    previous_region = st.session_state.regions[-1] if st.session_state.regions else None
                    new_region = {
                        'main_region': previous_region['main_region'] if previous_region else None,
                        'side': previous_region['side'] if previous_region else None,
                        'sub_region': previous_region['sub_region'] if previous_region else None,
                        'sub_sub_region': previous_region['sub_sub_region'] if previous_region else None,
                        'sub_sub_sub_region': previous_region['sub_sub_sub_region'] if previous_region else None,
                        'sub_sub_sub_sub_region': previous_region['sub_sub_sub_sub_region'] if previous_region else None,
                        'finger': previous_region['finger'] if previous_region else None,
                        'editable': True
                    }
                    st.session_state.regions.append(new_region)
                    st.success("Új régió hozzáadva")
                    st.session_state.new_region_blocked = True
                    st.experimental_rerun()
                elif st.session_state.new_region_blocked:
                    st.error("Mentse a jelenlegi régiót mielőtt újat hozna létre.")

        def display_region(region, idx):
            col3, col4, col5 = st.columns([1, 1, 1])
            with col3:
                if region['editable']:
                    region['main_region'] = select_main_region()
                else:
                    st.write(f"Fő régió: {region['main_region']}")
            if region['main_region']:
                if region['main_region'] in ["Felső végtag", "Alsó végtag"]:
                    with col4:
                        if region['editable']:
                            region['side'] = st.selectbox("Oldal", ["Bal", "Jobb"], index=["Bal", "Jobb"].index(region['side']) if region.get('side') else 0)
                        else:
                            st.write(f"Oldal: {region['side']}")
                if region['editable']:
                    with col5:
                        region['sub_region'] = select_subregion(region['main_region'])
                else:
                    st.write(f"Alrégió: {region['sub_region']}")
            if region['sub_region']:
                col6, col7, col8, col9 = st.columns([1, 1, 1, 1])
                with col6:
                    if region['editable']:
                        region['sub_sub_region'] = select_sub_subregion(region['sub_region'])
                    else:
                        st.write(f"Részletes régió: {region['sub_sub_region']}")
                if region['sub_sub_region']:
                    with col7:
                        if region['editable']:
                            region['sub_sub_sub_region'] = select_sub_sub_subregion(region['sub_sub_region'])
                        else:
                            st.write(f"Legpontosabb régió: {region['sub_sub_sub_region']}")
                if region['sub_sub_sub_region']:
                    with col8:
                        if region['editable']:
                            region['sub_sub_sub_sub_region'] = select_sub_sub_sub_subregion(region['sub_sub_sub_region'])
                        else:
                            st.write(f"Legrészletesebb régió: {region['sub_sub_sub_sub_region']}")
                    with col9:
                        if region['editable']:
                            if region['sub_sub_sub_region'] in ["Metacarpus", "Phalanx", "Metatarsus", "Lábujjak", "Pollex", "Hallux"]:
                                region['finger'], _ = select_finger(region['sub_sub_sub_region'])
                            else:
                                region['finger'] = None
                        else:
                            st.write(f"Ujj: {region['finger']}")

            if st.session_state.multi_region:
                if region['editable']:
                    if st.button(f"Régió {idx + 1} mentése", key=f"save_region_{idx}"):
                        region['editable'] = False
                        st.session_state.new_region_blocked = False
                        st.experimental_rerun()
                else:
                    if st.button(f"Régió {idx + 1} módosítása", key=f"modify_region_{idx}"):
                        region['editable'] = True
                        st.experimental_rerun()
                    if st.button(f"Régió {idx + 1} törlése", key=f"delete_region_{idx}"):
                        st.session_state.regions.pop(idx)
                        st.experimental_rerun()

        for idx, region in enumerate(st.session_state.regions):
            st.markdown(f"**Régió {idx + 1}:**")
            display_region(region, idx)

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

        if st.button("Feltöltés"):
            try:
                upload_data = {
                    "patient_id": st.session_state.patient_id,
                    "main_type": main_type,
                    "sub_type": sub_type,
                    "sub_sub_type": sub_sub_type,
                    "view": view,
                    "sub_view": sub_view,
                    "sub_sub_view": sub_sub_view,
                    "age": age,
                    "age_group": age_group,
                    "comment": comment,
                    "file": st.session_state.uploaded_file,
                    "complications": complications if main_type != "Normál" else [],
                    "associated_conditions": associated_conditions if main_type != "Normál" else [],
                    "classifications": {},
                    "regions": st.session_state.regions
                }
                st.session_state.confirm_data = upload_data
                st.success("Adatok sikeresen mentve. Kérem erősítse meg a feltöltést.")
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Hiba történt a mentés során: {e}")

        if st.session_state.confirm_data:
            confirm_and_upload_data(st.session_state.confirm_data)

    if st.experimental_get_query_params().get("scroll_to") == ["confirmation"]:
        st.markdown('<script>window.scrollTo(0, document.body.scrollHeight);</script>', unsafe_allow_html=True)

    st.button("Reset", on_click=reset_session_state)

if __name__ == "__main__":
    main()
