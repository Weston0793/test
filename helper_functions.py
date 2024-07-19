import streamlit as st
def style_markdown2():
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

def style_markdown():
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

def select_subregion(main_reg):
    regions = {
        "Felső végtag": ["", "Váll", "Kar", "Könyök", "Alkar", "Csukló", "Kéz"],
        "Alsó végtag": ["", "Medence", "Csípő", "Femur", "Térd", "Lábszár", "Boka", "Láb"],
        "Gerinc": ["", "Nyaki", "Háti", "Ágyéki", "Sacralis", "Coccygealis"],
        "Koponya": ["", "Arckoponya", "Agykoponya", "Állkapocs"],
        "Mellkas": ["", "Borda", "Sternum", "Kulcscsont", "Tüdő", "Szív"],
        "Has": ["", "Máj", "Lép", "Vese", "Bél", "Hólyag"]
    }
    return st.selectbox("Régió keresése", regions.get(main_reg, [""]))

def select_sub_subregion(sub_reg):
    sub_regions = {
        "Váll": ["", "Clavicula", "Scapula", "Humerus fej", "Proximális humerus", "Humerus nyak"],
        "Kar": ["", "Humerus szár"],
        "Könyök": ["", "Distalis humerus", "Humerus condylus", "Epicondylus", "Capitellum", "Olecranon", "Supracondylaris", "Coronoid processus"],
        "Alkar": ["", "Ulna", "Radius", "Mindkét csont", "Nightstick", "Essex-Lopresti", "Galeazzi", "Monteggia"],
        "Csukló": ["", "Distalis radius", "Distalis ulna"],
        "Kéz": ["", "Metacarpalis", "Hüvelykujj", "Phalanx"],
        "Medence": ["", "Malgaigne", "Windswept pelvis", "Pelvic bucket handle", "Pelvic insufficiency", "Anterior inferior iliac spine avulsion", "Duverney", "Open book", "Pubic rami", "Anterior superior iliac spine (ASIS) avulsion"],
        "Csípő": ["", "Acetabular", "Femoral head", "Femoral neck", "Trochanteric"],
        "Femur": ["", "Mid-shaft", "Bisphosphonate-related", "Distal femoral"],
        "Térd": ["", "Avulsion", "Patellar", "Tibial plateau"],
        "Lábszár": ["", "Tibial tuberosity avulsion", "Tibial shaft", "Fibular shaft", "Maisonneuve"],
        "Boka": ["", "Bimalleolar", "Trimalleolar", "Triplane", "Tillaux", "Bosworth", "Pilon", "Wagstaffe-Le Fort"],
        "Láb": ["", "Tarsal bones", "Metatarsal bones", "Toes"]
    }
    return st.selectbox("Alrégió keresése", sub_regions.get(sub_reg, [""]))

def select_sub_sub_subregion(sub_sub_reg):
    sub_sub_regions = {
        "Clavicula": ["", "Sternoclavicularis", "Középső szakasz", "Acromioclavicularis"],
        "Scapula": ["", "Acromion", "Coracoid processus", "Glenoid"],
        "Humerus fej": ["", "Hill-Sachs", "Fordított Hill-Sachs"],
        "Humerus condylus": ["", "Lateralis", "Medialis"],
        "Epicondylus": ["", "Medialis", "Lateralis"],
        "Supracondylaris": ["", "Extensio", "Flexio"],
        "Distalis radius": ["", "Chauffeur", "Colles", "Smith", "Barton", "Fordított Barton"],
        "Carpalis csontok": ["", "Scaphoid", "Lunate", "Capitate", "Triquetral", "Pisiform", "Hamate", "Trapezoid", "Trapezium"],
        "Metacarpalis": ["", "Boxer", "Fordított Bennett"],
        "Hüvelykujj": ["", "Gamekeeper's Thumb", "Epibasal", "Rolando", "Bennett"],
        "Phalanx": ["", "Distalis phalanx", "Jersey Finger", "Mallet Finger", "Seymour", "Középső phalanx", "Volar Plate Avulsion", "Pilon", "Proximális phalanx"],
        "Femoral neck": ["", "Subcapital", "Transcervical", "Basicervical"],
        "Trochanteric": ["", "Pertrochanteric", "Intertrochanteric", "Subtrochanteric"],
        "Avulsion": ["", "Segond", "Reverse Segond", "Anterior cruciate ligament avulsion", "Posterior cruciate ligament avulsion", "Arcuate complex avulsion (arcuate sign)", "Biceps femoris avulsion", "Iliotibial band avulsion", "Semimembranosus tendon avulsion", "Stieda (MCL avulsion fracture)"],
        "Tarsal bones": ["", "Chopart", "Calcaneal", "Lover's", "Calcaneal tuberosity avulsion", "Talar", "Talar body", "Talar dome osteochondral", "Posterior talar process", "Lateral talar process", "Talar neck", "Aviator astragalus", "Talar head", "Navicular", "Medial cuneiform", "Intermediate cuneiform", "Lateral cuneiform", "Cuboid"],
        "Metatarsal bones": ["", "March", "Lisfranc fracture-dislocation", "Stress fracture of the 5th metatarsal", "Jones", "Pseudo-Jones", "Avulsion fracture of the proximal 5th metatarsal"]
    }
    return st.selectbox("Részletes régió keresése", sub_sub_regions.get(sub_sub_reg, [""]))
