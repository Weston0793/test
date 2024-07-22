import streamlit as st

def select_main_type():
    main_type = st.radio("Válassza ki a típusát", ["Normál", "Törött", "Egyéb"], key="main_type")
    sub_type = ""
    sub_sub_type = ""
    if main_type == "Egyéb":
        sub_type = st.selectbox("Specifikálás (Egyéb)", [
            "Luxatio", "Subluxatio", "Szalagszakadás", "Osteoarthritis", "Osteoporosis", 
            "Osteomyelitis", "Cysta", "Álízűlet", "Malignus Tumor", "Benignus Tumor", 
            "Metastasis", "Rheumatoid Arthritis", "Genetikai/Veleszületett", "Implant", "Egyéb"
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
        "Elmozdulás", "Intraarticularis", "Nyílt", "Fragmentált", "Avulsio", "Luxatio", "Subluxatio", 
        "Idegsérülés", "Nagyobb Érsérülés", "Szalagszakadás", 
        "Meniscus Sérülés", "Epiphysis Sérülés", "Fertőzés"
    ])
    return complications

def select_associated_conditions():
    associated_conditions = st.multiselect("Társuló Kórállapotok (többet is választhat)", [
        "Osteoarthritis", "Osteoporosis", "Osteomyelitis", "Cysta", "Álízűlet", "Implant"
        "Rheumatoid Arthritis", "Metastasis", "Malignus Tumor", 
        "Benignus Tumor", "Genetikai"
    ])
    return associated_conditions

def select_subregion(main_reg):
    regions = {
        "Felső végtag": ["", "Váll", "Humerus", "Könyök", "Alkar", "Csukló", "Kéz"],
        "Alsó végtag": ["", "Medence", "Csípő", "Femur", "Térd", "Lábszár", "Boka", "Láb"],
        "Gerinc": ["", "Cervicalis", "Thoracalis", "Lumbaris", "Sacralis", "Coccygealis"],
        "Koponya": ["", "Arckoponya", "Agykoponya", "Mandibula"],
        "Mellkas": ["", "Borda", "Sternum", "Tüdő", "Szív"],
        "Has": ["", "Máj", "Lép", "Vese", "Bél", "Hólyag"]
    }
    return st.selectbox("Főrégió keresése", regions.get(main_reg, [""]))

def select_sub_subregion(sub_reg):
    sub_regions = {
        "Váll": ["", "Clavicula", "Scapula", "Proximális humerus"],
        "Humerus": ["", "Humerus diaphysis"],
        "Könyök": ["", "Distalis humerus", "Proximalis ulna", "Proximalis radius"],
        "Alkar": ["", "Ulna diaphysis", "Radius diaphysis", "Mindkét csont", "Nightstick", "Essex-Lopresti", "Galeazzi", "Monteggia"],
        "Csukló": ["", "Distalis radius", "Distalis ulna", "Carpus"],
        "Kéz": ["", "Metacarpus", "Pollex", "Phalanx"],
        "Pelvis": ["", "Ramus Pubicus ",  "Anterior inferior csípőtövis avulsio",  "Anterior superior csípőtövis (ASIS) avulsio", "Duverney", "Malgaigne", "Windswept pelvis", "Pelvic bucket handle", "Medencei elégtelenség", "Nyitott könyv"],
        "Csípő": ["", "Acetabulum", "Proximalis femur" "Femur fej", "Femur nyak", "Trochanterikus"],
        "Femur": ["", "Femur diaphysis", "Distalis femur", "Bisphosphonáthoz kapcsolódó"],
        "Térd": ["", "Avulsio", "Patella",  "Proximalis tibia", "Proximalis fibula"],
        "Lábszár": ["", "Tibia diaphysis", "Fibula diaphysis", "Tuberositas tibiae avulsio", "Maisonneuve"],
        "Boka": ["", "Distalis tibia", "Distalis fibula", "Bimalleolaris", "Trimalleolaris", "Triplane", "Tillaux", "Bosworth", "Pilon", "Wagstaffe-Le Fort"],
        "Láb": ["", "Tarsus", "Metatarsus", "Hallux", "Lábujjak"]
    }
    return st.selectbox("Régió ", sub_regions.get(sub_reg, [""]))
    
def select_sub_sub_subregion(sub_sub_reg):
    sub_sub_regions = {
        "Clavicula": ["", "Perifériás harmad", "Középső harmad", "Centrális harmad"],
        "Scapula": ["", "Scapula nyúlványok", "Scapula test", "Scapula nyak", "Cavitas glenoidalis", "Kombinált/Romos"],
        "Proximalis humerus": ["", "Humerus nyak", "Tuberculum majus", "Tuberculum minus", "Humerus fej", "Hill-Sachs", "Fordított Hill-Sachs"],
        "Distalis humerus": ["", "Supracondylaris", "Humerus condylus", "Epicondylus", "Capitellum"], 
        "Proximalis ulna": ["", "Olecranon", "Coronoid processus"], 
        "Proximalis radius": ["", "Radius fej", "Radius nyak"],
        "Distalis radius": ["", "Chauffeur", "Colles", "Smith", "Barton", "Fordított Barton"],
        "Distalis ulna": ["", "Processus styloideus ulnae"], 
        "Carpus": ["", "Scaphoideum", "Lunatum", "Capitatum", "Triquetrum", "Pisiforme", "Hamatum", "Trapesoideum", "Trapesium"],
        "Metacarpus": ["",  "Boxer", "Fordított Bennett"],
        "Pollex": ["", "Gamekeeper's Thumb", "Epibasal", "Rolando", "Bennett"],
        "Phalanx": ["", "Distalis phalanx", "Középső phalanx", "Proximális phalanx"],
        "Avulsio": ["", "Lig. cruciatum anterior avulsio", " Lig. cruciatum posterior avulsio", "Arcuatus komplex avulsio (arcuatus jel)", "Biceps femoris avulsio", "Lig. iliotibiale avulsio", "Semimembranosus tendon avulsio","Segond", "Fordított Segond", "Stieda (MCL avulsion fracture)"],
        "Proximalis tibia": ["", "Tibia plateau"],
        "Proximalis fibula": ["", "Fibula fej", "Fibula nyak"],
        "Tarsus": ["", "Chopart", "Calcaneus", "Talus", "Naviculare", "Medialis cuneiformis", "Középső cuneiformis", "Lateral cuneiformis", "Cuboideum"],
        "Metatarsus": ["", "March", "Lisfranc törés-luxatio", "V. metatarsus stressz törés", "Jones", "Pseudo-Jones", "V. metatarsus proximalis avulsio"]
    }
    return st.selectbox("Alrégió", sub_sub_regions.get(sub_sub_reg, [""]))

def select_sub_sub_sub_subregion(sub_sub_sub_reg):
    sub_sub_sub_regions = {
        "Nyúlványtörések": ["", "Acromion", "Coracoid processus"],
        "Scapula nyak": ["", "Stabil", "Instabil"],
        "Cavitas glenoidalis": ["", "Bankart", "Fordított Bankart"],
        "Humerus nyak": ["", "Collum anatomicum", "Collum chirurgicum"], 
        "Humerus condylus": ["", "Medialis", "Lateralis"],
        "Epicondylus": ["", "Medialis", "Lateralis"],
        "Supracondylaris": ["", "Extensio", "Flexio"],
        "Scaphoideum": ["", "De Quervain", ],
        "Distalis phalanx": ["", "Basis", "Corpus", "Caput", "Jersey Finger", "Mallet Finger", "Seymour",],
        "Középső phalanx": ["", "Basis", "Corpus", "Caput", "Volar Plate avulsio", "Pilon",],
        "Proximális phalanx": ["", "Basis", "Corpus", "Caput"],
        "Femur nyak": ["", "Subcapitalis", "Transcervicalis", "Basicervicalis"],
        "Trochanterikus": ["", "Pertrochanterikus", "Intertrochanterikus", "Subtrochanterikus"],
        "Calcaneus": ["", "Lover's", "Calcaneus tuberositas avulsio"],
        "Talus": ["", "Talus fej", "Talus test", "Talus nyak", "Talus kupola", "Posterior talus processus", "Lateralis talus processus", "Aviator astragalus"],
        "Cuboideum": ["","Nutcracker"],
    }
    return st.selectbox("Részletes régió", sub_sub_sub_regions.get(sub_sub_sub_reg, [""]))  
    
def select_finger(sub_sub_regions):
    finger = None
    if sub_sub_regions in ["Metacarpus", "Phalanx", "Metatarsus", "Lábujjak"]:
        finger = st.selectbox("Ujj", ["I", "II", "III", "IV", "V"])
    return finger

