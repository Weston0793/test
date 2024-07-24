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
from functions import (
    initialize_home_session_state, reset_session_state,
    display_region
)

def main():
    initialize_home_session_state()
    upload_markdown()
    st.markdown('<div class="upload-title">Orvosi Röntgenkép Adatbázis</div>', unsafe_allow_html=True)

    st.text_input("Beteg azonosító", st.session_state.patient_id, disabled=True)

    st.markdown('<div class="file-upload-instruction">Kérem húzzon az alábbi ablakra vagy válasszon ki a fájlkezelőn keresztül egy röntgenképet (Max 15 MB)</div>', unsafe_allow_html=True)
    st.session_state.allow_multiple_uploads = st.checkbox("Több kép feltöltése")

    if st.session_state.allow_multiple_uploads:
        st.warning("Ugyanazokkal a címkékkel lesz jelölve az összes kép!")

    uploaded_file = st.file_uploader("Fájl kiválasztása", type=["jpg", "jpeg", "png"], accept_multiple_files=False, key=st.session_state.file_uploader_key)

    if uploaded_file is not None:
        uploaded_image = handle_file_upload(uploaded_file)
        if st.session_state.allow_multiple_uploads:
            if uploaded_file.name not in [f.name for f in st.session_state.uploaded_files]:
                st.session_state.uploaded_files.append(uploaded_image)
        else:
            st.session_state.uploaded_file = uploaded_image
            st.session_state.uploaded_files = [uploaded_image]

    if st.session_state.uploaded_files:
        if not st.session_state.allow_multiple_uploads:
            st.image(st.session_state.uploaded_files[0], caption=f"Feltöltött kép: {st.session_state.uploaded_files[0].name}", use_column_width=True)
        else:
            cols = st.columns(2)
            for idx, file in enumerate(st.session_state.uploaded_files):
                with cols[idx % 2]:
                    st.image(file, caption=f"ID: {uuid.uuid4()} - {file.name}", use_column_width=True)

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
                new_region = previous_region.copy() if previous_region else {
                    'main_region': None,
                    'side': None,
                    'sub_region': None,
                    'sub_sub_region': None,
                    'sub_sub_sub_region': None,
                    'sub_sub_sub_sub_region': None,
                    'finger': None,
                    'editable': True
                }
                st.session_state.regions.append(new_region)
                st.success("Új régió hozzáadva")
                st.session_state.new_region_blocked = True
                st.experimental_rerun()
            elif st.session_state.new_region_blocked:
                st.error("Mentse a jelenlegi régiót mielőtt újat hozna létre.")

    for idx, region in enumerate(st.session_state.regions):
        st.markdown(f"**Régió {idx + 1}:**")
        st.session_state.regions[idx] = display_region(region, idx)
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
                "files": st.session_state.uploaded_files,
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

    if st.button("Reset"):
        reset_session_state()
        st.session_state.file_uploader_key = str(uuid.uuid4())
        st.experimental_rerun()

if __name__ == "__main__":
    main()
