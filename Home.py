import streamlit as st
from firebase_helpers import save_image
import uuid

def main():
    st.markdown(
        """
        <style>
        .upload-title {
            font-size: 24px;
            font-weight: bold;
            color: black;
            margin-bottom: 20px;
            text-align: center;
            border: 2px solid black;
            padding: 10px;
        }
        .center-button {
            display: flex;
            justify-content: center;
        }
        .upload-button, .confirm-button {
            font-size: 24px;
            background-color: #4CAF50;
            color: white;
            padding: 15px 30px;
            border: none;
            cursor: pointer;
            border: 2px solid black;
            margin: 10px;
        }
        .upload-button:hover, .confirm-button:hover {
            background-color: #45a049;
        }
        .confirmation-box {
            padding: 20px;
            margin-top: 20px;
            text-align: center;
        }
        .confirmation-title, .confirmation-text {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="upload-title">Orvosi Röntgenkép Adatbázis</div>', unsafe_allow_html=True)

    patient_id = str(uuid.uuid4())

    st.text_input("Beteg azonosító", patient_id, disabled=True)

    uploaded_file = st.file_uploader("Válassz egy képet", type=["jpg", "jpeg", "png"])

    st.write("Típus")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Normál"):
            st.session_state["type"] = "Normál"
    with col2:
        if st.button("Törött"):
            st.session_state["type"] = "Törött"
    with col3:
        type_other = st.selectbox("Egyéb", ["", "Luxatio", "Subluxatio", "Osteoarthritis", "Osteoporosis", "Osteomyelitis", "Malignus Tumor", "Benignus Tumor", "Metastasis", "Rheumatoid Arthritis", "Cysta", "Genetikai/Veleszületett"])
        if type_other:
            st.session_state["type"] = type_other
            if type_other in ["Malignus Tumor", "Benignus Tumor", "Genetikai/Veleszületett"]:
                type_comment = st.text_input("Specifikálás (Egyéb)")
                st.session_state["type_comment"] = type_comment

    if "type" in st.session_state and st.session_state["type"] != "Normál":
        st.write("Társultak")
        associated_conditions = ["Nyílt", "Darabos", "Avulsio", "Luxatio", "Subluxatio", "Idegsérülés", "Nagyobb Érsérülés", "Szalagszakadás", "Meniscus Sérülés", "Epihysis Sérülés", "Fertőzés", "Cysta", "Tumor", "Genetikai"]
        selected_conditions = st.multiselect("Társult feltételek", associated_conditions)

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

    age = st.select_slider("Életkor", options=["NA"] + list(range(0, 121)), value="NA")
    comment = st.text_area("Megjegyzés", key="comment", value="")

    if "confirm_data" not in st.session_state:
        st.session_state["confirm_data"] = None

    if st.button("Feltöltés"):
        if uploaded_file and "type" in st.session_state and view and main_region and sub_region:
            upload_data = {
                "patient_id": patient_id,
                "type": st.session_state["type"],
                "view": view,
                "main_region": main_region,
                "sub_region": sub_region,
                "age": age,
                "comment": comment + " " + st.session_state.get("type_comment", "") + " " + view_comment,
                "file": uploaded_file
            }
            if "selected_conditions" in locals():
                upload_data["associated_conditions"] = selected_conditions
            st.session_state["confirm_data"] = upload_data
            st.experimental_rerun()

    if st.session_state["confirm_data"]:
        upload_data = st.session_state["confirm_data"]
        st.markdown('<div class="confirmation-box">', unsafe_allow_html=True)
        st.markdown('<div class="confirmation-title">Kérlek, erősítsd meg a következő adatokat:</div>', unsafe_allow_html=True)
        st.markdown(f'**Beteg azonosító:** {upload_data["patient_id"]}')
        st.markdown(f'**Típus:** {upload_data["type"]}')
        st.markdown(f'**Nézet:** {upload_data["view"]}')
        st.markdown(f'**Fő régió:** {upload_data["main_region"]}')
        st.markdown(f'**Alrégió:** {upload_data["sub_region"]}')
        st.markdown(f'**Életkor:** {upload_data["age"]}')
        st.markdown(f'**Megjegyzés:** {upload_data["comment"]}')
        if "associated_conditions" in upload_data:
            st.markdown(f'**Társult feltételek:** {", ".join(upload_data["associated_conditions"])}')

        st.markdown('<div class="center-button">', unsafe_allow_html=True)
        if st.button("Megerősít és Feltölt", key="confirm_upload"):
            try:
                save_image(**upload_data)
                st.success("Kép sikeresen feltöltve!")
                st.session_state["confirm_data"] = None
            except Exception as e:
                st.error(f"Hiba a kép mentésekor: {e}")
                st.session_state["confirm_data"] = None
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
