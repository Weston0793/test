import streamlit as st
from backend import handle_file_upload, confirm_and_upload_data
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
        .file-upload-instruction {
            font-size: 18px;
            font-weight: bold;
            color: black;
            margin-bottom: 20px;
            text-align: center;
            border: 2px solid black;
            padding: 10px;
            background-color: #f9f9f9;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

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
            type = st.radio("Válassza ki a típusát", ["Normál", "Törött", "Egyéb"], key="type")
            if type == "Egyéb":
                type = st.text_input("Adja meg a specifikus típust (Egyéb)")

        with col2:
            view = st.radio("Válassza ki a nézetet", ["AP", "Lateral", "Egyéb"], key="view")
            if view == "Egyéb":
                view = st.selectbox("Specifikálás (Egyéb Nézet)", ["Ferde", "PA", "Speciális"])
                if view == "Speciális":
                    view = st.text_input("Adja meg a specifikus nézetet (Speciális)")

        main_region = st.selectbox("Fő régió", ["Felső végtag", "Alsó végtag", "Gerinc", "Koponya", "Mellkas", "Has"])

        sub_region = ""
        sub_sub_region = ""
        sub_sub_sub_region = ""

        col3, col4 = st.columns(2)
        with col3:
            if main_region == "Felső végtag":
                sub_region = st.selectbox("Régió", ["Váll", "Kar", "Könyök", "Alkar", "Csukló", "Kéz"])

                if sub_region == "Váll":
                    sub_sub_region = st.selectbox("Alrégió", ["Clavicula", "Scapula", "Humerus fej", "Proximális humerus", "Humerus nyak"])
                    if sub_sub_region == "Clavicula":
                        sub_sub_sub_region = st.selectbox("Részletes régió", ["Sternoclavicularis", "Középső szakasz", "Acromioclavicularis"])
                    elif sub_sub_region == "Scapula":
                        sub_sub_sub_region = st.selectbox("Részletes régió", ["Acromion", "Coracoid processus", "Glenoid"])
                    elif sub_sub_region == "Humerus fej":
                        sub_sub_sub_region = st.selectbox("Részletes régió", ["Hill-Sachs", "Fordított Hill-Sachs"])

                elif sub_region == "Kar":
                    sub_sub_region = st.selectbox("Alrégió", ["Humerus szár"])

                elif sub_region == "Könyök":
                    sub_sub_region = st.selectbox("Alrégió", ["Distalis humerus", "Humerus condylus", "Epicondylus", "Capitellum", "Olecranon", "Supracondylaris", "Coronoid processus"])
                    if sub_sub_region == "Humerus condylus":
                        sub_sub_sub_region = st.selectbox("Részletes régió", ["Lateralis", "Medialis"])
                    elif sub_sub_region == "Epicondylus":
                        sub_sub_sub_region = st.selectbox("Részletes régió", ["Medialis", "Lateralis"])
                    elif sub_sub_region == "Supracondylaris":
                        sub_sub_sub_region = st.selectbox("Részletes régió", ["Extensio", "Flexio"])

                elif sub_region == "Alkar":
                    sub_sub_region = st.selectbox("Alrégió", ["Ulna", "Radius", "Mindkét csont", "Nightstick", "Essex-Lopresti", "Galeazzi", "Monteggia"])

                elif sub_region == "Csukló":
                    sub_sub_region = st.selectbox("Alrégió", ["Distalis radius", "Distalis ulna"])
                    if sub_sub_region == "Distalis radius":
                        sub_sub_sub_region = st.selectbox("Részletes régió", ["Chauffeur", "Colles", "Smith", "Barton", "Fordított Barton"])
                    elif sub_sub_region == "Carpalis csontok":
                        sub_sub_sub_region = st.selectbox("Részletes régió", ["Scaphoid", "Lunate", "Capitate", "Triquetral", "Pisiform", "Hamate", "Trapezoid", "Trapezium"])

                elif sub_region == "Kéz":
                    sub_sub_region = st.selectbox("Alrégió", ["Metacarpalis", "Hüvelykujj", "Phalanx"])
                    if sub_sub_region == "Metacarpalis":
                        sub_sub_sub_region = st.selectbox("Részletes régió", ["Boxer", "Fordított Bennett"])
                    elif sub_sub_region == "Hüvelykujj":
                        sub_sub_sub_region = st.selectbox("Részletes régió", ["Gamekeeper's Thumb", "Epibasal", "Rolando", "Bennett"])
                    elif sub_sub_region == "Phalanx":
                        sub_sub_sub_region = st.selectbox("Részletes régió", ["Distalis phalanx", "Jersey Finger", "Mallet Finger", "Seymour", "Középső phalanx", "Volar Plate Avulsion", "Pilon", "Proximális phalanx"])

            elif main_region == "Alsó végtag":
                sub_region = st.selectbox("Régió", ["Medence", "Sacralis", "Coccygealis", "Csípő", "Femur", "Térd", "Lábszár", "Boka", "Láb"])
                if sub_region == "Medence":
                    sub_sub_region = st.selectbox("Részletes régió", ["Malgaigne", "Windswept pelvis", "Pelvic bucket handle", "Pelvic insufficiency", "Anterior inferior iliac spine avulsion", "Duverney", "Open book", "Pubic rami", "Anterior superior iliac spine (ASIS) avulsion"])
                elif sub_region == "Csípő":
                    sub_sub_region = st.selectbox("Részletes régió", ["Acetabular", "Femoral head", "Femoral neck", "Trochanteric"])
                    if sub_sub_region == "Femoral neck":
                        sub_sub_sub_region = st.selectbox("Részletes régió", ["Subcapital", "Transcervical", "Basicervical"])
                    elif sub_sub_region == "Trochanteric":
                        sub_sub_sub_region = st.selectbox("Részletes régió", ["Pertrochanteric", "Intertrochanteric", "Subtrochanteric"])
                elif sub_region == "Femur":
                    sub_sub_region = st.selectbox("Részletes régió", ["Mid-shaft", "Bisphosphonate-related", "Distal femoral"])
                elif sub_region == "Térd":
                    sub_sub_region = st.selectbox("Részletes régió", ["Avulsion", "Patellar", "Tibial plateau"])
                    if sub_sub_region == "Avulsion":
                        sub_sub_sub_region = st.selectbox("Részletes régió", ["Segond", "Reverse Segond", "Anterior cruciate ligament avulsion", "Posterior cruciate ligament avulsion", "Arcuate complex avulsion (arcuate sign)", "Biceps femoris avulsion", "Iliotibial band avulsion", "Semimembranosus tendon avulsion", "Stieda (MCL avulsion fracture)"])
                elif sub_region == "Lábszár":
                    sub_sub_region = st.selectbox("Részletes régió", ["Tibial tuberosity avulsion", "Tibial shaft", "Fibular shaft", "Maisonneuve"])
                elif sub_region == "Boka":
                    sub_sub_region = st.selectbox("Részletes régió", ["Bimalleolar", "Trimalleolar", "Triplane", "Tillaux", "Bosworth", "Pilon", "Wagstaffe-Le Fort"])
                elif sub_region == "Láb":
                    sub_sub_region = st.selectbox("Részletes régió", ["Tarsal bones", "Metatarsal bones", "Toes"])
                    if sub_sub_region == "Tarsal bones":
                        sub_sub_sub_region = st.selectbox("Részletes régió", ["Chopart", "Calcaneal", "Lover's", "Calcaneal tuberosity avulsion", "Talar", "Talar body", "Talar dome osteochondral", "Posterior talar process", "Lateral talar process", "Talar neck", "Aviator astragalus", "Talar head", "Navicular", "Medial cuneiform", "Intermediate cuneiform", "Lateral cuneiform", "Cuboid"])
                    elif sub_sub_region == "Metatarsal bones":
                        sub_sub_sub_region = st.selectbox("Részletes régió", ["March", "Lisfranc fracture-dislocation", "Stress fracture of the 5th metatarsal", "Jones", "Pseudo-Jones", "Avulsion fracture of the proximal 5th metatarsal"])

            elif main_region == "Gerinc":
                sub_region = st.selectbox("Régió", ["Nyaki", "Háti", "Ágyéki", "Kereszt- és farokcsonti"])
        
            elif main_region == "Koponya":
                sub_region = st.selectbox("Régió", ["Arckoponya", "Agykoponya", "Állkapocs"])
        
            elif main_region == "Mellkas":
                sub_region = st.selectbox("Régió", ["Borda", "Sternum", "Kulcscsont", "Tüdő", "Szív"])
        
            elif main_region == "Has":
                sub_region = st.selectbox("Régió", ["Máj", "Lép", "Vese", "Bél", "Hólyag"])

        age = st.select_slider("Életkor (opcionális)", options=["NA"] + list(range(0, 121)), value="NA")
        age_group = ""
        if age != "NA":
            age = int(age)
            age_group = "Gyermek" if age <= 18 else "Felnőtt"

        comment = st.text_area("Megjegyzés (opcionális)", key="comment", value="")

        if "confirm_data" not in st.session_state:
            st.session_state["confirm_data"] = None

        if st.button("Feltöltés"):
            upload_data = {
                "patient_id": patient_id,
                "type": type,
                "view": view,
                "main_region": main_region,
                "sub_region": sub_region,
                "sub_sub_region": sub_sub_region if type != "Normál" else "",
                "sub_sub_sub_region": sub_sub_sub_region if type != "Normál" else "",
                "age": age,
                "age_group": age_group,
                "comment": comment,
                "file": uploaded_file,
                "complications": complications if type != "Normál" else [],
                "associated_conditions": associated_conditions if type != "Normál" else []
            }
            st.session_state["confirm_data"] = upload_data
            st.rerun()

        if st.session_state["confirm_data"]:
            confirm_and_upload_data(st.session_state["confirm_data"])

    if st.experimental_get_query_params().get("scroll_to") == ["confirmation"]:
        st.markdown('<script>window.scrollTo(0, document.body.scrollHeight);</script>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
