import streamlit as st
from firebase_helpers import save_image

import streamlit as st
from firebase_helpers import save_image

def handle_file_upload(uploaded_file):
    if uploaded_file.size > 15 * 1024 * 1024:
        st.error("A kép mérete nem lehet nagyobb, mint 15 MB.")
        return None
    else:
        st.image(uploaded_file, caption="Feltöltött kép", use_column_width=True)
        return uploaded_file

def confirm_and_upload_data(upload_data):
    if upload_data['age'] == "NA":
        age_group = st.radio("Kérem válassza ki az életkori csoportot", ["Gyermek", "Felnőtt"])
        upload_data['age_group'] = age_group

    st.markdown('<div class="confirmation-box">', unsafe_allow_html=True)
    st.markdown('<div class="confirmation-title">Kérlek, a feltöltéshez erősítsd meg a következő adatokat:</div>', unsafe_allow_html=True)
    st.markdown(f'**Beteg azonosító:** {upload_data["patient_id"]}')
    st.markdown(f'**Típus:** {upload_data["main_type"]}')
    if upload_data["sub_type"]:
        st.markdown(f'**Specifikus típus:** {upload_data["sub_type"]}')
    if upload_data["sub_sub_type"]:
        st.markdown(f'**Legspecifikusabb típus:** {upload_data["sub_sub_type"]}')
    st.markdown(f'**Nézet:** {upload_data["view"]}')
    if upload_data["sub_view"]:
        st.markdown(f'**Specifikus nézet:** {upload_data["sub_view"]}')
    if upload_data["sub_sub_view"]:
        st.markdown(f'**Legspecifikusabb nézet:** {upload_data["sub_sub_view"]}')
    st.markdown(f'**Életkor: (opcionális)** {upload_data["age"]}')
    st.markdown(f'**Életkori Csoport:** {upload_data["age_group"]}')
    st.markdown(f'**Megjegyzés: (opcionális)** {upload_data["comment"]}')
    if upload_data["complications"]:
        st.markdown(f'**Komplikációk: (többet is választhat)** {", ".join(upload_data["complications"])}')
    if upload_data["associated_conditions"]:
        st.markdown(f'**Társuló Kórállapotok: (többet is választhat)** {", ".join(upload_data["associated_conditions"])}')
    if upload_data.get("classifications"):
        for classification, details in upload_data["classifications"].items():
            st.markdown(f'**{classification} osztályozás:**')
            st.markdown(f'**Név:** {details["name"]}')
            st.markdown(f'**Súlyosság:** {details["severity"]}')
            if "subseverity" in details:
                st.markdown(f'**Alsúlyosság:** {details["subseverity"]}')
            if "description" in details:
                st.markdown(f'**Leírás:** {details["description"]}')

    st.markdown("### Kiválasztott régiók")
    for idx, region in enumerate(upload_data["regions"]):
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

    st.markdown('<div class="center-button">', unsafe_allow_html=True)
    if st.button("Megerősít és Feltölt", key="confirm_upload"):
        try:
            save_image(**upload_data)
            st.success("Kép sikeresen feltöltve!")
            st.session_state["confirm_data"] = None
            st.experimental_set_query_params(scroll_to="confirmation")
        except Exception as e:
            st.error(f"Hiba a kép mentésekor: {e}")
            st.session_state["confirm_data"] = None
    st.markdown('</div>', unsafe_allow_html=True)
