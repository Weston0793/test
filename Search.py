import streamlit as st
from google.cloud import firestore
from firebase_helpers import db, create_zip
import uuid
from google.api_core.exceptions import GoogleAPICallError
from search_backend import perform_search

def search_section():
    st.markdown(
        """
        <style>
        .search-title {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            border: 2px solid black;
            padding: 10px;
            margin-bottom: 20px;
        }
        .result-image {
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 5px;
            margin-bottom: 10px;
        }
        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 10px 0;
        }
        .button-container button {
            font-size: 18px;
            padding: 10px 20px;
            margin: 0 5px;
            border-radius: 5px;
            background-color: #4CAF50; /* Green */
            color: white;
            border: none;
            cursor: pointer;
        }
        .button-container button:hover {
            background-color: #45a049;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="search-title">Képek keresése</div>', unsafe_allow_html=True)

    predefined_types = ["", "Normál", "Törött", "Egyéb"]
    predefined_views = ["", "AP", "Lateral", "Ferde", "PA", "Speciális"]
    main_regions = ["", "Felső végtag", "Alsó végtag", "Gerinc", "Koponya", "Mellkas", "Has"]

    # Type and view in one row
    col1, col2 = st.columns(2)
    with col1:
        search_type = st.selectbox("Típus keresése", predefined_types)
    with col2:
        search_view = st.selectbox("Nézet keresése", predefined_views)

    # Main and sub region in one row
    col3, col4 = st.columns(2)
    with col3:
        search_main_region = st.selectbox("Fő régió keresése", main_regions)
    with col4:
        if search_main_region == "Felső végtag":
            search_sub_region = st.selectbox("Régió keresése", ["", "Váll", "Kar", "Könyök", "Alkar", "Csukló", "Kéz"])
        elif search_main_region == "Alsó végtag":
            search_sub_region = st.selectbox("Régió keresése", ["", "Medence", "Csípő", "Femur", "Térd", "Lábszár", "Boka", "Láb"])
        elif search_main_region == "Gerinc":
            search_sub_region = st.selectbox("Régió keresése", ["", "Nyaki", "Háti", "Ágyéki", "Sacralis", "Coccygealis"])
        elif search_main_region == "Koponya":
            search_sub_region = st.selectbox("Régió keresése", ["", "Arckoponya", "Agykoponya", "Állkapocs"])
        elif search_main_region == "Mellkas":
            search_sub_region = st.selectbox("Régió keresése", ["", "Borda", "Sternum", "Kulcscsont", "Tüdő", "Szív"])
        elif search_main_region == "Has":
            search_sub_region = st.selectbox("Régió keresése", ["", "Máj", "Lép", "Vese", "Bél", "Hólyag"])
        else:
            search_sub_region = ""

    # Sub-subregion and sub-sub-subregion in one row
    col5, col6 = st.columns(2)
    with col5:
        if search_sub_region == "Váll":
            search_sub_sub_region = st.selectbox("Alrégió keresése", ["", "Clavicula", "Scapula", "Humerus fej", "Proximális humerus", "Humerus nyak"])
        elif search_sub_region == "Kar":
            search_sub_sub_region = st.selectbox("Alrégió keresése", ["", "Humerus szár"])
        elif search_sub_region == "Könyök":
            search_sub_sub_region = st.selectbox("Alrégió keresése", ["", "Distalis humerus", "Humerus condylus", "Epicondylus", "Capitellum", "Olecranon", "Supracondylaris", "Coronoid processus"])
        elif search_sub_region == "Alkar":
            search_sub_sub_region = st.selectbox("Alrégió keresése", ["", "Ulna", "Radius", "Mindkét csont", "Nightstick", "Essex-Lopresti", "Galeazzi", "Monteggia"])
        elif search_sub_region == "Csukló":
            search_sub_sub_region = st.selectbox("Alrégió keresése", ["", "Distalis radius", "Distalis ulna"])
        elif search_sub_region == "Kéz":
            search_sub_sub_region = st.selectbox("Alrégió keresése", ["", "Metacarpalis", "Hüvelykujj", "Phalanx"])
        elif search_sub_region == "Medence":
            search_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Malgaigne", "Windswept pelvis", "Pelvic bucket handle", "Pelvic insufficiency", "Anterior inferior iliac spine avulsion", "Duverney", "Open book", "Pubic rami", "Anterior superior iliac spine (ASIS) avulsion"])
        elif search_sub_region == "Csípő":
            search_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Acetabular", "Femoral head", "Femoral neck", "Trochanteric"])
        elif search_sub_region == "Femur":
            search_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Mid-shaft", "Bisphosphonate-related", "Distal femoral"])
        elif search_sub_region == "Térd":
            search_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Avulsion", "Patellar", "Tibial plateau"])
        elif search_sub_region == "Lábszár":
            search_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Tibial tuberosity avulsion", "Tibial shaft", "Fibular shaft", "Maisonneuve"])
        elif search_sub_region == "Boka":
            search_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Bimalleolar", "Trimalleolar", "Triplane", "Tillaux", "Bosworth", "Pilon", "Wagstaffe-Le Fort"])
        elif search_sub_region == "Láb":
            search_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Tarsal bones", "Metatarsal bones", "Toes"])
        else:
            search_sub_sub_region = ""

    with col6:
        if search_sub_sub_region == "Clavicula":
            search_sub_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Sternoclavicularis", "Középső szakasz", "Acromioclavicularis"])
        elif search_sub_sub_region == "Scapula":
            search_sub_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Acromion", "Coracoid processus", "Glenoid"])
        elif search_sub_sub_region == "Humerus fej":
            search_sub_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Hill-Sachs", "Fordított Hill-Sachs"])
        elif search_sub_sub_region == "Humerus condylus":
            search_sub_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Lateralis", "Medialis"])
        elif search_sub_sub_region == "Epicondylus":
            search_sub_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Medialis", "Lateralis"])
        elif search_sub_sub_region == "Supracondylaris":
            search_sub_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Extensio", "Flexio"])
        elif search_sub_sub_region == "Distalis radius":
            search_sub_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Chauffeur", "Colles", "Smith", "Barton", "Fordított Barton"])
        elif search_sub_sub_region == "Carpalis csontok":
            search_sub_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Scaphoid", "Lunate", "Capitate", "Triquetral", "Pisiform", "Hamate", "Trapezoid", "Trapezium"])
        elif search_sub_sub_region == "Metacarpalis":
            search_sub_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Boxer", "Fordított Bennett"])
        elif search_sub_sub_region == "Hüvelykujj":
            search_sub_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Gamekeeper's Thumb", "Epibasal", "Rolando", "Bennett"])
        elif search_sub_sub_region == "Phalanx":
            search_sub_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Distalis phalanx", "Jersey Finger", "Mallet Finger", "Seymour", "Középső phalanx", "Volar Plate Avulsion", "Pilon", "Proximális phalanx"])
        elif search_sub_sub_region == "Femoral neck":
            search_sub_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Subcapital", "Transcervical", "Basicervical"])
        elif search_sub_sub_region == "Trochanteric":
            search_sub_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Pertrochanteric", "Intertrochanteric", "Subtrochanteric"])
        elif search_sub_sub_region == "Avulsion":
            search_sub_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Segond", "Reverse Segond", "Anterior cruciate ligament avulsion", "Posterior cruciate ligament avulsion", "Arcuate complex avulsion (arcuate sign)", "Biceps femoris avulsion", "Iliotibial band avulsion", "Semimembranosus tendon avulsion", "Stieda (MCL avulsion fracture)"])
        elif search_sub_sub_region == "Tarsal bones":
            search_sub_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "Chopart", "Calcaneal", "Lover's", "Calcaneal tuberosity avulsion", "Talar", "Talar body", "Talar dome osteochondral", "Posterior talar process", "Lateral talar process", "Talar neck", "Aviator astragalus", "Talar head", "Navicular", "Medial cuneiform", "Intermediate cuneiform", "Lateral cuneiform", "Cuboid"])
        elif search_sub_sub_region == "Metatarsal bones":
            search_sub_sub_sub_region = st.selectbox("Részletes régió keresése", ["", "March", "Lisfranc fracture-dislocation", "Stress fracture of the 5th metatarsal", "Jones", "Pseudo-Jones", "Avulsion fracture of the proximal 5th metatarsal"])
        else:
            search_sub_sub_sub_region = ""

    search_complications = st.multiselect("Komplikációk keresése", ["Nyílt", "Darabos", "Avulsio", "Luxatio", "Subluxatio", "Idegsérülés", "Nagyobb Érsérülés", "Szalagszakadás", "Meniscus Sérülés", "Epiphysis Sérülés", "Fertőzés"])
    search_associated_conditions = st.multiselect("Társuló Kórállapotok keresése", ["Osteoarthritis", "Osteoporosis", "Osteomyelitis", "Rheumatoid Arthritis", "Cysta", "Metastasis", "Malignus Tumor", "Benignus Tumor", "Genetikai"])

    # Age filter with checkbox
    age_filter_active = st.checkbox("Életkor keresése (intervallum)")
    if age_filter_active:
        search_age = st.slider("Életkor keresése (intervallum)", min_value=0, max_value=120, value=(0, 18), step=1, format="%d")
    else:
        search_age = None

    search_age_group = st.selectbox("Életkori csoport keresése", ["", "Gyermek", "Felnőtt"])

    # Page and items per page in one row
    col7, col8 = st.columns(2)
    with col7:
        page = st.number_input("Oldal", min_value=1, step=1, value=1)
    with col8:
        items_per_page = st.selectbox("Találatok száma oldalanként", options=[10, 25, 50, 100], index=0)

    # Button for search
    search_button_clicked = st.button("Keresés", key="search_button")

    if search_button_clicked:
        page = 1  # Reset to the first page on new search
        st.session_state.search_button_clicked = True
        st.session_state.query_params = {
            "search_button_clicked": True,
            "type": search_type,
            "view": search_view,
            "main_region": search_main_region,
            "sub_region": search_sub_region,
            "sub_sub_region": search_sub_sub_region,
            "sub_sub_sub_region": search_sub_sub_sub_region,
            "complications": search_complications,
            "associated_conditions": search_associated_conditions,
            "age_filter_active": age_filter_active,
            "age": str(search_age) if search_age else "",
            "age_group": search_age_group,
            "page": page,
            "items_per_page": items_per_page
        }
        st.experimental_rerun()

    if 'search_button_clicked' in st.session_state:
        perform_search(st.session_state.query_params)

if __name__ == "__main__":
    search_section()

