import streamlit as st

def select_main_type():
    main_type = st.radio("Válassza ki a típusát", ["Normál", "Törött", "Egyéb"], key="main_type")
    sub_type = ""
    sub_sub_type = ""
    if main_type == "Egyéb":
        sub_type = st.selectbox("Specifikálás (Egyéb)", [
            "Luxatio", "Subluxatio", "Osteoarthritis", "Osteoporosis", 
            "Osteomyelitis", "Cysta", "Malignus Tumor", "Benignus Tumor", 
            "Metastasis", "Rheumatoid Arthritis", "Genetikai/Veleszületett", "Egyéb"
        ])
        if sub_type in ["Malignus Tumor", "Benignus Tumor", "Genetikai/Veleszületett", "Egyéb"]:
            sub_sub_type = st.text_input("Adja meg a specifikus típust (Egyéb)")
    return main_type, sub_type, sub_sub_type

def select_view():
    view = st.radio("Válassza ki a nézetet", ["AP", "Lateral", "Egyéb"], key="view")
    sub_view = ""
    sub_sub_view = ""
    if view == "Egyéb":
        sub_view = st.selectbox("Specifikálás (Egyéb Nézet)", ["Ferde", "PA", "Speciális"])
        if sub_view == "Speciális":
            sub_sub_view = st.text_input("Adja meg a specifikus nézetet (Speciális)")
    return view, sub_view, sub_sub_view

def select_main_region():
    main_region = st.selectbox("Fő régió", ["Felső végtag", "Alsó végtag", "Gerinc", "Koponya", "Mellkas", "Has"])
    return main_region

def select_complications():
    complications = st.multiselect("Komplikációk (többet is választhat)", [
        "Nyílt", "Darabos", "Avulsio", "Luxatio", "Subluxatio", 
        "Idegsérülés", "Nagyobb Érsérülés", "Szalagszakadás", 
        "Meniscus Sérülés", "Epiphysis Sérülés", "Fertőzés"
    ])
    return complications

def select_associated_conditions():
    associated_conditions = st.multiselect("Társuló Kórállapotok (többet is választhat)", [
        "Osteoarthritis", "Osteoporosis", "Osteomyelitis", "Cysta", 
        "Rheumatoid Arthritis", "Metastasis", "Malignus Tumor", 
        "Benignus Tumor", "Genetikai"
    ])
    return associated_conditions

def select_subregion(main_reg):
    regions = {
        "Felső végtag": ["", "Váll", "Humerus", "Könyök", "Alkar", "Csukló", "Kéz"],
        "Alsó végtag": ["", "Medence", "Pelvis", "Femur", "Térd", "Lábszár", "Boka", "Láb"],
        "Gerinc": ["", "Cervicalis", "Thoracalis", "Lumbaris", "Sacralis", "Coccygealis"],
        "Koponya": ["", "Arckoponya", "Agykoponya", "Mandibula"],
        "Mellkas": ["", "Borda", "Sternum", "Tüdő", "Szív"],
        "Has": ["", "Máj", "Lép", "Vese", "Bél", "Hólyag"]
    }
    return st.selectbox("Régió keresése", regions.get(main_reg, [""]))

def select_sub_subregion(sub_reg):
    sub_regions = {
        "Váll": ["", "Clavicula", "Scapula", "Humerus fej", "Proximális humerus", "Humerus nyak"],
        "Humerus": ["", "Humerus diaphysis"],
        "Könyök": ["", "Distalis humerus", "Supracondylaris", "Humerus condylus", "Epicondylus", "Capitellum", "Olecranon", "Coronoid processus"],
        "Alkar": ["", "Ulna", "Radius", "Mindkét csont", "Nightstick", "Essex-Lopresti", "Galeazzi", "Monteggia"],
        "Csukló": ["", "Distalis radius", "Distalis ulna", "Carpus"],
        "Kéz": ["", "Metacarpus", "Pollex", "Phalanx"],
        "Pelvis": ["", "Ramus Pubicus ",  "Anterior inferior csípőtövis avulsio",  "Anterior superior csípőtövis (ASIS) avulsio", "Duverney", "Malgaigne", "Windswept pelvis", "Pelvic bucket handle", "Medencei elégtelenség", "Nyitott könyv"],
        "Csípő": ["", "Acetabulum", "Femur fej", "Femur nyak", "Trochanterikus"],
        "Femur": ["", "Femur diaphysis", "Distalis femur", "Bisphosphonáthoz kapcsolódó"],
        "Térd": ["", "Avulsio", "Patella", "Tibia plateau"],
        "Lábszár": ["", "Tibialis tuberositas avulsio", "Tibia diaphysis", "Fibula diaphysis", "Maisonneuve"],
        "Boka": ["", "Bimalleolaris", "Trimalleolaris", "Triplane", "Tillaux", "Bosworth", "Pilon", "Wagstaffe-Le Fort"],
        "Láb": ["", "Tarsus", "Metatarsus ", "Lábujjak"]
    }
    return st.selectbox("Alrégió keresése", sub_regions.get(sub_reg, [""]))
    
def select_sub_sub_subregion(sub_sub_reg):
    sub_sub_regions = {
        "Clavicula": ["", "Sternoclavicularis", "Középső szakasz", "Acromioclavicularis"],
        "Scapula": ["", "Acromion", "Coracoid processus", "Glenoid"],
        "Humerus fej": ["", "Hill-Sachs", "Fordított Hill-Sachs"],
        "Humerus condylus": ["", "Medialis", "Lateralis"],
        "Epicondylus": ["", "Medialis", "Lateralis"],
        "Supracondylaris": ["", "Extensio", "Flexio"],
        "Distalis radius": ["", "Chauffeur", "Colles", "Smith", "Barton", "Fordított Barton"],
        "Carpus": ["", "Scaphoideum", "Lunatum", "Capitatum", "Triquetrum", "Pisiforme", "Hamatum", "Trapezoidum", "Trapezium"],
        "Metacarpus": ["", "Boxer", "Fordított Bennett"],
        "Pollex": ["", "Gamekeeper's Thumb", "Epibasal", "Rolando", "Bennett"],
        "Phalanx": ["", "Distalis phalanx", "Jersey Finger", "Mallet Finger", "Seymour", "Középső phalanx", "Volar Plate Avulsio", "Pilon", "Proximális phalanx"],
        "Femur nyak": ["", "Subcapitalis", "Transcervicalis", "Basicervicalis"],
        "Trochanterikus": ["", "Pertrochanterikus", "Intertrochanterikus", "Subtrochanterikus"],
        "Avulsio": ["", "Segond", "Fordított Segond", "Anterior cruciatum ligamentum avulsio", "Posterior cruciatum ligamentum avulsio", "Arcuatus komplex avulsio (arcuatus jel)", "Biceps femoris avulsio", "Iliotibial ligamentum avulsio", "Semimembranosus tendon avulsio", "Stieda (MCL avulsion fracture)"],
        "Tarsus": ["", "Chopart", "Calcaneus", "Lover's", "Calcaneus tuberositas avulsio", "Talus test", "Talus kupola osteochondralis", "Posterior talus processus", "Lateralis talus processus", "Talus nyak", "Aviator astragalus", "Talus fej", "Naviculare", "Medialis cuneiformis", "Középső cuneiformis", "Lateral cuneiformis", "Cuboid"],
        "Metatarsus": ["", "March", "Lisfranc törés-luxatio", "Az 5. metatarsus stressz törés", "Jones", "Pseudo-Jones", "Az 5. metatarsus proximalis avulsiós törés"]
    }
    return st.selectbox("Részletes régió keresése", sub_sub_regions.get(sub_sub_reg, [""]))
