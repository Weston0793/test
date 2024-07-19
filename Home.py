import streamlit as st
from home_backend import handle_file_upload, confirm_and_upload_data
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

        sub_region_options = []
        sub_sub_region_options = []
        sub_sub_sub_region_options = []

        if main_region == "Felső végtag":
            sub_region_options = ["Váll", "Kar", "Könyök", "Alkar", "Csukló", "Kéz"]
        elif main_region == "Alsó végtag":
            sub_region_options = ["Medence", "Sacralis", "Coccygealis", "Csípő", "Femur", "Térd", "Lábszár", "Boka", "Láb"]
        elif main_region == "Gerinc":
            sub_region_options = ["Nyaki", "Háti", "Ágyéki", "Kereszt- és farokcsonti"]
        elif main_region == "Koponya":
            sub_region_options = ["Arckoponya", "Agykoponya", "Állkapocs"]
        elif main_region == "Mellkas":
            sub_region_options = ["Borda", "Sternum", "Kulcscsont", "Tüdő", "Szív"]
        elif main_region == "Has":
            sub_region_options = ["Máj", "Lép", "Vese", "Bél", "Hólyag"]

        if sub_region_options:
            sub_region = st.selectbox("Régió", sub_region_options)

        if sub_region == "Váll":
            sub_sub_region_options = ["Clavicula", "Scapula", "Humerus fej", "Proximális humerus", "Humerus nyak"]
        elif sub_region == "Kar":
            sub_sub_region_options = ["Humerus szár"]
        elif sub_region == "Könyök":
            sub_sub_region_options = ["Distalis humerus", "Humerus condylus", "Epicondylus", "Capitellum", "Olecranon", "Supracondylaris", "Coronoid processus"]
        elif sub_region == "Alkar":
            sub_sub_region_options = ["Ulna", "Radius", "Mindkét csont", "Nightstick", "Essex-Lopresti", "Galeazzi", "Monteggia"]
        elif sub_region == "Csukló":
            sub_sub_region_options = ["Distalis radius", "Distalis ulna"]
        elif sub_region == "Kéz":
            sub_sub_region_options = ["Metacarpalis", "Hüvelykujj", "Phalanx"]
        elif sub_region == "Medence":
            sub_sub_region_options = ["Malgaigne", "Windswept pelvis", "Pelvic bucket handle", "Pelvic insufficiency", "Anterior inferior iliac spine avulsion", "Duverney", "Open book", "Pubic rami", "Anterior superior iliac spine (ASIS) avulsion"]
        elif sub_region == "Csípő":
            sub_sub_region_options = ["Acetabular", "Femoral head", "Femoral neck", "Trochanteric"]
        elif sub_region == "Femur":
            sub_sub_region_options = ["Mid-shaft", "Bisphosphonate-related", "Distal femoral"]
        elif sub_region == "Térd":
            sub_sub_region_options = ["Avulsion", "Patellar", "Tibial plateau"]
        elif sub_region == "Lábszár":
            sub_sub_region_options = ["Tibial tuberosity avulsion", "Tibial shaft", "Fibular shaft", "Maisonneuve"]
        elif sub_region == "Boka":
            sub_sub_region_options = ["Bimalleolar", "Trimalleolar", "Triplane", "Tillaux", "Bosworth", "Pilon", "Wagstaffe-Le Fort"]
        elif sub_region == "Láb":
            sub_sub_region_options = ["Tarsal bones", "Metatarsal bones", "Toes"]

        if sub_sub_region_options:
            sub_sub_region = st.selectbox("Alrégió", ["NA"] + sub_sub_region_options, index=0)

        if sub_sub_region == "Clavicula":
            sub_sub_sub_region_options = ["Sternoclavicularis", "Középső szakasz", "Acromioclavicularis"]
        elif sub_sub_region == "Scapula":
            sub_sub_sub_region_options = ["Acromion", "Coracoid processus", "Glenoid"]
        elif sub_sub_region == "Humerus fej":
            sub_sub_sub_region_options = ["Hill-Sachs", "Fordított Hill-Sachs"]
        elif sub_sub_region == "Humerus condylus":
            sub_sub_sub_region_options = ["Lateralis", "Medialis"]
        elif sub_sub_region == "Epicondylus":
            sub_sub_sub_region_options = ["Medialis", "Lateralis"]
        elif sub_sub_region == "Supracondylaris":
            sub_sub_sub_region_options = ["Extensio", "Flexio"]
        elif sub_sub_region == "Distalis radius":
            sub_sub_sub_region_options = ["Chauffeur", "Colles", "Smith", "Barton", "Fordított Barton"]
        elif sub_sub_region == "Carpalis csontok":
            sub_sub_sub_region_options = ["Scaphoid", "Lunate", "Capitate", "Triquetral", "Pisiform", "Hamate", "Trapezoid", "Trapezium"]
        elif sub_sub_region == "Metacarpalis":
            sub_sub_sub_region_options = ["Boxer", "Fordított Bennett"]
        elif sub_sub_region == "Hüvelykujj":
            sub_sub_sub_region_options = ["Gamekeeper's Thumb", "Epibasal", "Rolando", "Bennett"]
        elif sub_sub_region == "Phalanx":
            sub_sub_sub_region_options = ["Distalis phalanx", "Jersey Finger", "Mallet Finger", "Seymour", "Középső phalanx", "Volar Plate Avulsion", "Pilon", "Proximális phalanx"]
        elif sub_sub_region == "Femoral neck":
            sub_sub_sub_region_options = ["Subcapital", "Transcervical", "Basicervical"]
        elif sub_sub_region == "Trochanteric":
            sub_sub_sub_region_options = ["Pertrochanteric", "Intertrochanteric", "Subtrochanteric"]
        elif sub_sub_region == "Avulsion":
            sub_sub_sub_region_options = ["Segond", "Reverse Segond", "Anterior cruciate ligament avulsion", "Posterior cruciate ligament avulsion", "Arcuate complex avulsion (arcuate sign)", "Biceps femoris avulsion", "Iliotibial band avulsion", "Semimembranosus tendon avulsion", "Stieda (MCL avulsion fracture)"]
        elif sub_sub_region == "Tarsal bones":
            sub_sub_sub_region_options = ["Chopart", "Calcaneal", "Lover's", "Calcaneal tuberosity avulsion", "Talar", "Talar body", "Talar dome osteochondral", "Posterior talar process", "Lateral talar process", "Talar neck", "Aviator astragalus", "Talar head", "Navicular", "Medial cuneiform", "Intermediate cuneiform", "Lateral cuneiform", "Cuboid"]
        elif sub_sub_region == "Metatarsal bones":
            sub_sub_sub_region_options = ["March", "Lisfranc fracture-dislocation", "Stress fracture of the 5th metatarsal", "Jones", "Pseudo-Jones", "Avulsion fracture of the proximal 5th metatarsal"]

        if sub_sub_sub_region_options:
            sub_sub_sub_region = st.selectbox("Részletes régió", ["NA"] + sub_sub_sub_region_options, index=0)

        if type != "Normál":
            complications = st.multiselect("Komplikációk (többet is választhat)", ["Nyílt", "Darabos", "Avulsio", "Luxatio", "Subluxatio", "Idegsérülés", "Nagyobb Érsérülés", "Szalagszakadás", "Meniscus Sérülés", "Epiphysis Sérülés", "Fertőzés"])
            associated_conditions = st.multiselect("Társuló Kórállapotok (többet is választhat)", ["Osteoarthritis", "Osteoporosis", "Osteomyelitis", "Rheumatoid Arthritis", "Cysta", "Metastasis", "Malignus Tumor", "Benignus Tumor", "Genetikai"])

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
                "sub_region": sub_region if type != "Normál" else "",
                "sub_sub_region": sub_sub_region if sub_sub_region != "NA" else "",
                "sub_sub_sub_region": sub_sub_sub_region if sub_sub_sub_region != "NA" else "",
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
