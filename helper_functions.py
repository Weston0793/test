import streamlit as st

def select_main_type():
    main_type = st.radio("Válassza ki a típusát", ["Normál", "Törött", "Egyéb"], key="main_type")
    sub_type = ""
    sub_sub_type = ""
    
    if main_type == "Egyéb":
        sub_type = st.selectbox("Specifikálás (Egyéb)", [
            "Luxatio", "Subluxatio", "Szalagszakadás", "Osteoarthritis", "Osteoporosis", 
            "Osteomyelitis", "Cysta", "Álízület", "Vérzés", "Tumor", 
            "Metastasis", "Rheumatoid Arthritis", "Genetikai/Veleszületett", "Implant", "Egyéb"
        ])
        
        if sub_type == "Tumor":
            tumor_type = st.selectbox("Válassza ki a daganat típusát", [
                "Chondrogen daganatok", "Osteogen daganatok", "Fibrogen daganatok", "Vascularis daganatok",
                "Osteoclastikus óriássejtdús daganatok", "Notokordiális daganatok", "Egyéb mesenchymalis daganatok",
                "Haematopoeticus daganatok"
            ])
            
            sub_type = tumor_type  # Update sub_type to be the selected tumor category
            
            if tumor_type == "Chondrogen daganatok":
                sub_sub_type = st.selectbox("Válassza ki a specifikus típust (Chondrogen daganatok)", [
                    "Osteochondroma", "Periostealis chondroma", "Enchondroma", "Chondromyxoid fibroma",
                    "Osteochondromyxoma", "Subungualis exostosis", "Bizarr parostealis osteochondromatos proliferáció",
                    "Synovialis chondromatosis", "Chondroblastoma", "Centrális atípusos chondrogén tumor / chondrosarcoma (1. fokozat)",
                    "Szekunder perifériás atípusos chondrogén tumor / chondrosarcoma (1. fokozat)",
                    "Centrális chondrosarcoma (2-3. fokozat)", "Szekunder chondrosarcoma (2-3. fokozat)",
                    "Periostealis chondrosarcoma", "Dedifferenciált chondrosarcoma", "Mesenchymalis chondrosarcoma",
                    "Tiszta sejtes chondrosarcoma"
                ])
            elif tumor_type == "Osteogen daganatok":
                sub_sub_type = st.selectbox("Válassza ki a specifikus típust (Osteogen daganatok)", [
                    "Osteoma", "Osteoid osteoma", "Osteoblastoma", "Alacsony fokozatú centrális osteosarcoma",
                    "Osteosarcoma", "Konvencionális osteosarcoma", "Telangiectaticus osteosarcoma",
                    "Kis sejtes osteosarcoma", "Parostealis osteosarcoma", "Periostealis osteosarcoma",
                    "Magas fokozatú felszíni osteosarcoma", "Szekunder osteosarcoma"
                ])
            elif tumor_type == "Fibrogen daganatok":
                sub_sub_type = st.selectbox("Válassza ki a specifikus típust (Fibrogen daganatok)", [
                    "Desmoplasticus fibroma csontban", "Fibrosarcoma csontban"
                ])
            elif tumor_type == "Vascularis daganatok":
                sub_sub_type = st.selectbox("Válassza ki a specifikus típust (Vascularis daganatok)", [
                    "Haemangioma", "Epithelioid haemangioma", "Epithelioid haemangioendothelioma", "Angiosarcoma"
                ])
            elif tumor_type == "Osteoclastikus óriássejtdús daganatok":
                sub_sub_type = st.selectbox("Válassza ki a specifikus típust (Osteoclastikus óriássejtdús daganatok)", [
                    "Aneurizmás csont ciszta", "Óriássejtes daganat csontban", "Nem csontosodó fibroma"
                ])
            elif tumor_type == "Notokordiális daganatok":
                sub_sub_type = st.selectbox("Válassza ki a specifikus típust (Notokordiális daganatok)", [
                    "Jóindulatú notokordiális sejt tumor", "Chordoma", "Dedifferenciált chordoma", "Gyengén differenciált chordoma"
                ])
            elif tumor_type == "Egyéb mesenchymalis daganatok":
                sub_sub_type = st.selectbox("Válassza ki a specifikus típust (Egyéb mesenchymalis daganatok)", [
                    "Chondromesenchymalis hamartoma", "Osteofibrosus dysplasia", "Adamantinoma",
                    "Egyszerű csont ciszta", "Fibrocartilaginous mesenchymoma", "Fibrosus dysplasia",
                    "Lipoma csontban", "Liposarcoma", "Leiomyosarcoma", "Nem differenciált pleomorf sarcoma",
                    "Csont metastasis"
                ])
            elif tumor_type == "Haematopoeticus daganatok":
                sub_sub_type = st.selectbox("Válassza ki a specifikus típust (Haematopoeticus daganatok)", [
                    "Solitaris plasmacytoma csontban", "Primer non-Hodgkin lymphoma csontban", "Langerhans sejt histiocytosis",
                    "Erdheim-Chester betegség", "Rosai-Dorfman betegség"
                ])
        elif sub_type == "Genetikai/Veleszületett" or sub_type == "Egyéb":
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

def select_gender():
    gender = st.radio("Nem", ["", "Férfi", "Nő"], key="gender")
    return gender
    
def select_main_region():
    main_region = st.selectbox("Fő régió", ["Felső végtag", "Alsó végtag", "Gerinc", "Koponya", "Mellkas", "Has"])
    return main_region

def select_complications():
    complications = st.multiselect("Komplikációk (többet is választhat)", [
        "Elmozdulás", "Intraarticularis", "Nyílt", "Fragmentált", "Avulsio", "Luxatio", "Subluxatio", 
        "Idegsérülés", "Nagyobb Érsérülés", "Szalagszakadás", 
        "Meniscus Sérülés", "Epiphysis Sérülés", "Fertőzés",
    ])
    return complications

def select_associated_conditions():
    associated_conditions = st.multiselect("Társuló Kórállapotok (többet is választhat)", [
        "Osteoarthritis", "Osteoporosis", "Osteomyelitis", "Cysta", "Álízűlet", "Implant",
        "Rheumatoid Arthritis", "Metastasis", "Malignus Tumor", 
        "Benignus Tumor", "Genetikai"
    ])
    return associated_conditions

def select_subregion(main_reg):
    regions = {
        "Felső végtag": ["", "Váll", "Humerus", "Könyök", "Alkar", "Csukló", "Kéz"],
        "Alsó végtag": ["", "Medence", "Csípő", "Femur", "Térd", "Lábszár", "Boka", "Láb"],
        "Gerinc": ["", "Cervicalis", "Thoracalis", "Lumbalis", "Sacrum", "Coccyx"],
        "Koponya": ["", "Arckoponya", "Mandibula", "Calvaria", "Koponyaalap", "Fog"],
        "Mellkas": ["", "Borda", "Sternum", "Tüdő", "Szív", "Mell"],
        "Has": ["", "Máj", "Epehólyag", "Pancreas", "Lép", "Vese", "Húgyhólyag", "Gyomor", "Vékonybél", "Vastagbél" ]
    }
    return st.selectbox("Régió", regions.get(main_reg, [""]))

def select_sub_subregion(sub_reg):
    sub_regions = {
        "Váll": ["", "Clavicula", "Scapula", "Proximális humerus"],
        "Humerus": ["", "Humerus diaphysis"],
        "Könyök": ["", "Distalis humerus", "Proximalis ulna", "Proximalis radius"],
        "Alkar": ["", "Ulna diaphysis", "Radius diaphysis", "Mindkét csont", "Nightstick", "Essex-Lopresti", "Galeazzi", "Monteggia"],
        "Csukló": ["", "Distalis radius", "Distalis ulna", "Carpus"],
        "Kéz": ["", "Metacarpus", "Pollex", "Phalanx"],
        "Pelvis": ["", "Ramus pubicus",  "Anterior inferior csípőtövis avulsio",  "Anterior superior csípőtövis avulsio", "Duverney", "Malgaigne", "Windswept pelvis", "Pelvic bucket handle", "Medencei elégtelenség", "Nyitott könyv"],
        "Csípő": ["", "Acetabulum", "Proximalis femur"],
        "Femur": ["", "Femur diaphysis",  "Bisphosphonáthoz kapcsolódó"],
        "Térd": ["", "Distalis femur", "Avulsio", "Patella",  "Proximalis tibia", "Proximalis fibula"],
        "Lábszár": ["", "Tibia diaphysis", "Fibula diaphysis", "Tuberositas tibiae avulsio", "Maisonneuve"],
        "Boka": ["", "Distalis tibia", "Distalis fibula", "Bimalleolaris", "Trimalleolaris", "Triplane", "Tillaux", "Bosworth", "Pilon", "Wagstaffe-Le Fort"],
        "Láb": ["", "Tarsus", "Metatarsus", "Hallux", "Lábujjak"],
        "Cervicalis": ["", "C1-Atlas", "C2-Axis", "C3", "C4", "C5", "C6", "C7"],
        "Thoracalis": ["", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10", "T11", "T12"],
        "Lumbalis": ["", "L1", "L2", "L3", "L4", "L5"],   
        "Arckoponya": ["", " Orrcsont", "Orbita", "Zygomaticum", "Arcus zygomaticus", "Processus alveolaris", "Panfacialis"], 
        "Mandibula": ["", "Corpus mandibulae", "Symphysis", "Szemfogtájék", "Szemfog és angulus között", "Angulus mandibulae", "Ramus mandibulae", "Processus articularis", "Processus muscularis"],  
        "Calvaria": ["", "Frontale", "Parietale", "Temporale", "Occipitale"], 
        "Koponyaalap": ["","Condylus occipitalis", "Fossa anterior", "Fossa mediale", "Fossa posterior"],
        "Fog": ["","Szemfog", "Metszőfog", "Kisörlő", "Nagyörlő"]
    }
    return st.selectbox("Alrégió", sub_regions.get(sub_reg, [""]))
    
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
        "Pollex": ["", "Distalis phalanx", "Proximalis phalanx", "Gamekeeper's Thumb", "Epibasal", "Rolando", "Bennett"],
        "Phalanx": ["", "Distalis phalanx", "Középső phalanx", "Proximalis phalanx"],
        "Proximalis femur": ["", "Femur fej", "Femur nyak", "Trochanterikus"],
        "Avulsio": ["", "Lig. cruciatum anterior avulsio", " Lig. cruciatum posterior avulsio", "Arcuatus komplex avulsio (arcuatus jel)", "Biceps femoris avulsio", "Lig. iliotibiale avulsio", "Semimembranosus tendon avulsio","Segond", "Fordított Segond", "Stieda (MCL avulsion fracture)"],
        "Proximalis tibia": ["", "Tibia plateau"],
        "Proximalis fibula": ["", "Fibula fej", "Fibula nyak"],
        "Tarsus": ["", "Chopart", "Calcaneus", "Talus", "Naviculare", "Medialis cuneiformis", "Középső cuneiformis", "Lateral cuneiformis", "Cuboideum"],
        "Metatarsus": ["", "March", "Lisfranc törés-luxatio", "V. metatarsus stressz törés", "Jones", "Pseudo-Jones", "V. metatarsus proximalis avulsio"],
        "C1-Atlas": ["","Jefferson"],
        "C2-Axis": ["", "Dens axis", "Csigolyatest", "Hangman"],
        "Panfacialis": ["", "Le Fort I", "Le Fort II", "Le Fort III", "Naso-orbito-ethmoidalis"],
        "Processus articularis": ["", "Extracapsularis", "Intracapsularis"],
        "Szemfog": ["", "Korona", "Gyökér"], 
        "Metszőfog": ["", "Korona", "Gyökér"], 
        "Kisörlő": ["", "Korona", "Gyökér"], 
        "Nagyörlő": ["", "Korona", "Gyökér"] 
    }
    return st.selectbox("Részletes régió", sub_sub_regions.get(sub_sub_reg, [""]))

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
        "Hamatum": ["", "Hamulus"],
        "Distalis phalanx": ["", "Basis", "Corpus", "Caput", "Jersey Finger", "Mallet Finger", "Seymour"],
        "Középső phalanx": ["", "Basis", "Corpus", "Caput", "Volar Plate avulsio", "Pilon"],
        "Proximalis phalanx": ["", "Basis", "Corpus", "Caput"],
        "Femur nyak": ["", "Subcapitalis", "Transcervicalis", "Basicervicalis"],
        "Trochanterikus": ["", "Pertrochanterikus", "Intertrochanterikus", "Subtrochanterikus"],
        "Calcaneus": ["", "Lover's", "Calcaneus tuberositas avulsio"],
        "Talus": ["", "Talus fej", "Talus test", "Talus nyak", "Talus kupola", "Posterior talus processus", "Lateralis talus processus", "Aviator astragalus"],
        "Cuboideum": ["", "Nutcracker"],
        "Dens axis": ["", "Dens csúcs", "Dens basis", "Csigolyatestre terjedő"]
    }
    return st.selectbox("Legpontosabb régió", sub_sub_sub_regions.get(sub_sub_sub_reg, [""]))  
    
def select_finger(sub_sub_regions):
    side = st.selectbox("Oldal", ["Bal", "Jobb"])
    
    finger = None
    if sub_sub_regions in ["Metacarpus", "Phalanx", "Metatarsus", "Lábujjak", "Pollex", "Hallux"]:
        if sub_sub_regions in ["Pollex", "Hallux"]:
            finger = "I"
        elif sub_sub_regions in ["Phalanx", "Lábujjak"]:
            finger = st.selectbox("Ujj", ["II", "III", "IV", "V"])   
        else:
            finger = st.selectbox("Ujj", ["I", "II", "III", "IV", "V"])
    return finger, side

def ao_classification(sub_sub_reg):
    ao_classes = {
        "Proximalis humerus": {
            "11A": "Extraarticularis, unifokális, 2 rész",
            "11B": "Extraarticularis, bifokális, 3 rész",
            "11C": "Ízületi vagy 4 rész",
        },
         "Humerus diaphysis": {
            "12A": "Egyszeres",
            "12B": "Ék",
            "12C": "Többszörös"
        },
        "Distalis humerus": {
            "13A": "Extraarticularis",
            "13B": "Részleges ízületi",
            "13C": "Teljes ízületi"
        },
        "Proximalis radius": {
            "2R1A": "Extraarticularis",
            "2R1B": "Részleges ízületi",
            "2R1C": "Teljes ízületi"
        },
        "Radius diaphysis": {
            "2R2A": "Egyszeres",
            "2R2B": "Ék",
            "2R2C": "Többszörös"
        },
        "Distalis radius": {
            "2R3A": "Extraarticularis",
            "2R3B": "Részleges ízületi",
            "2R3C": "Teljes ízületi"
        },
        "Proximalis ulna": {
            "2U1A": "Extraarticularis",
            "2U1B": "Részleges ízületi",
            "2U1C": "Teljes ízületi"
        },
        "Ulna diaphysis": {
            "2U2A": "Egyszeres",
            "2U2B": "Ék",
            "2U2C": "Többszörös"
        },
        "Distalis ulna": {
            "2U3A": "Extraarticularis",
            "2U3B": "Részleges ízületi",
            "2U3C": "Teljes ízületi"
        }
        "Proximalis femur": {
            "31A": "Trochantericus régió",
            "31B": "Femur nyak",
            "31C": "Femur fej"
        },
        "Femur diaphysis": {
            "32A": "Egyszeres",
            "32B": "Ék",
            "32C": "Többszörös"
        },
        "Distalis femur": {
            "33A": "Extraarticularis",
            "33B": "Részleges ízületi",
            "33C": "Teljes ízületi"
        },
        "Proximalis tibia": {
            "41A": "Extraarticularis",
            "41B": "Részleges ízületi",
            "41C": "Teljes ízületi"
        },
        "Tibia diaphysis": {
            "42A": "Egyszeres",
            "42B": "Ék",
            "42C": "Többszörös"
        },
        "Distalis tibia": {
            "43A": "Extraarticularis",
            "43B": "Részleges ízületi",
            "43C": "Teljes ízületi"
        },
    }

    ao_type_options = [f"{key} - {value}" for key, value in ao_classes.get(sub_sub_reg, {}).items()]
    if not ao_type_options:
        return None, None, None

    ao_type = st.selectbox("AO klasszifikáció típusa", ao_type_options)
    if not ao_type:
        return None, None, None

    ao_severity = ao_type.split(" - ")[0]
    ao_subtype = st.selectbox("AO altípus részletezése", get_ao_subtype_details(ao_severity))
    
    classification_name = "AO klasszifikáció"
    ao_subseverity = ao_subtype
    
    return classification_name, ao_severity, ao_subseverity

def get_ao_subtype_details(ao_type):
    details = {
        "11A": {
            "1": "Tuberositas",
            "2": "Collum chirurgicum",
            "3": "Vertikális"
        },
        "11B": {
            "1": "Collum chirurgicum"
        },
        "11C": {
            "1": "Collum anatomicum",
            "3": "Collum anatomicum metafízis töréssel"
        },
        "12A": {
            "1": "Spirális",
            "2": "Ferde (≥ 30°)",
            "3": "Keresztirányú (< 30°)"
        },
        "12B": {
            "2": "Ép ék",
            "3": "Töredezett ék"
        },
        "12C": {
            "2": "Ép szegmentális",
            "3": "Töredezett szegmentális"
        },
        "13A": {
            "1": "Avulsio",
            "2": "Egyszeres",
            "3": "Ék vagy többszörös"
        },
        "13B": {
            "1": "Laterális sagittális",
            "2": "Mediális sagittális",
            "3": "Frontal/coronal plane"
        },
        "13C": {
            "1": "Egyszerű ízületi, egyszerű metafízis",
            "2": "Egyszerű ízületi, ék vagy többszörös metafízis",
            "3": "Többszörös ízületi, ék vagy többszörös metafízis"
        },
        "2R1A": {
            "1": "Bicipitalis tuberositas avulsiós törés",
            "2": "Egyszeres nyaktörés",
            "3": "Többszörös nyaktörés"
        },
        "2R1B": {
            "1": "Egyszeres",
            "3": "Többszörös"
        },
        "2R1C": {
            "1": "Egyszeres",
            "3": "Többszörös"
        },
        "2R2A": {
            "1": "Spirális",
            "2": "Ferde (≥ 30°)",
            "3": "Haránt (< 30°)"
        },
        "2R2B": {
            "2": "Ép ék",
            "3": "Töredezett ék"
        },
        "2R2C": {
            "1": "Ép szegmentális",
            "2": "Töredezett szegmentális"
        },
        "2R3A": {
            "1": "Processus styloideus radii avulsiós törés",
            "2": "Egyszeres",
            "3": "Ék vagy többszörös"
        },
        "2R3B": {
            "1": "Sagittalis",
            "2": "Dorsalis perem (Barton's)",
            "3": "Volaris perem (reverse Barton's)"
        },
        "2R3C": {
            "1": "Egyszerű ízületi és metaphysealis",
            "2": "Többszörös metaphysealis",
            "3": "Többszörös ízületi, egyszerű vagy többszörös metaphysealis"
        },
        "2U1A": {
            "1": "Triceps tapadási avulsiós törés",
            "2": "Egyszeres metaphysealis",
            "3": "Többszörös metaphysealis"
        },
        "2U1B": {
            "1": "Olecranon",
            "2": "Processus coronoideus"
        },
        "2U1C": {
            "3": "Olecranon és processus coronoideus"
        },
        "2U2A": {
            "1": "Spirális törés",
            "2": "Ferdevágású törés (≥ 30°)",
            "3": "Haránt törés (< 30°)"
        },
        "2U2B": {
            "2": "Ép ék",
            "3": "Töredezett ék"
        },
        "2U2C": {
            "2": "Ép szegmentális",
            "3": "Töredezett szegmentális"
        },
        "2U3A": {
            "1": "Processus styloideus avulsiós törés",
            "2": "Egyszeres törés",
            "3": "Többszörös törés"
        },
        "31A": {
            "1": "Egyszerű pertrochantericus",
            "2": "Többrészű pertrochantericus",
            "3": "Intertrochantericus (fordított dőlésszög)"
        },
        "31B": {
            "1": "Subcapitalis",
            "2": "Transcervicalis",
            "3": "Basicervicalis"
        },
        "31C": {
            "1": "Hasadék",
            "2": "Benyomódás"
        },
        "32A": {
            "1": "Spirális",
            "2": "Ferde (≥ 30°)",
            "3": "Haránt (< 30°)"
        },
        "32B": {
            "2": "Ép ék",
            "3": "Töredezett ék"
        },
        "32C": {
            "2": "Ép szegmentális",
            "3": "Töredezett szegmentális"
        },
        "33A": {
            "1": "Avulsio",
            "2": "Egyszerű",
            "3": "Ék vagy többrészű"
        },
        "33B": {
            "1": "Lateral condyle, sagittal",
            "2": "Medial condyle, sagittal",
            "3": "Frontal/coronal"
        },
        "33C": {
            "1": "Egyszerű ízületi, egyszerű metafízis",
            "2": "Egyszerű ízületi, ék vagy többrészű metafízis",
            "3": "Többrészű ízületi, egyszerű, ék vagy többrészű metafízis"
        },
        "41A": {
            "1": "Avulsio",
            "2": "Egyszerű",
            "3": "Ék vagy többszörös"
        },
        "41B": {
            "1": "Hasadék",
            "2": "Benyomódás",
            "3": "Hasadék benyomódással"
        },
        "41C": {
            "1": "Egyszerű ízületi, egyszerű metafízis",
            "2": "Egyszerű ízületi, ék vagy többrészű metafízis",
            "3": "Többrészű ízületi, többrészű metafízis"
        },
        "42A": {
            "1": "Spirál",
            "2": "Ferde (≥ 30°)",
            "3": "Haránt (< 30°)"
        },
        "42B": {
            "2": "Ép ék",
            "3": "Töredezett ék"
        },
        "42C": {
            "2": "Ép szegmentális",
            "3": "Töredezett szegmentális"
        },
        "43A": {
            "1": "Egyszeres",
            "2": "Ék",
            "3": "Többszörös"
        },
        "43B": {
            "1": "Hasadék",
            "2": "Hasadék benyomódással",
            "3": "Benyomódás"
        },
        "43C": {
            "1": "Egyszerű ízületi, egyszerű metafízis",
            "2": "Egyszerű ízületi, többrészű metafízis",
            "3": "Többrészű ízületi és többrészű metafízis"
        },
    }
    return [f"{key} - {value}" for key, value in details.get(ao_type, {}).items()]
    
def get_ao_subsubseverity_details(ao_type):
    details = {
        "11A1": {
            ".1": "Tuberculum majus",
            ".2": "Tuberculum minus"
        },
        "11A2": {
            ".1": "Egyszeres",
            ".2": "Ék",
            ".3": "Többszörös"
        },
        "11B1": {
            ".1": "Tuberculum majus töréssel",
            ".2": "Tuberculum minus töréssel"
        },
        "11C1": {
            ".1": "Valgus impressiós"
            ".3": "Izolált collum anatomicum",
        },
        "12A1": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "12A2": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "12A3": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "12B2": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "12B3": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },        
        "12C2": {
            "i": "Proximalis diaphysealis-metaphysealis",
            "j": "Tisztán diaphysealis"
            "k": "Distalis diaphysealis-metaphysealis"
        },
        "12C3": {
            "i": "Proximalis diaphysealis-metaphysealis",
            "j": "Tisztán diaphysealis"
            "k": "Distalis diaphysealis-metaphysealis"
        },
        "13A1": {
            ".1": "Lateralis epicondylus",
            ".2": "Medialis epicondylus"
        },
        "13A2": {
            ".1": "Spirál",
            ".2": "Ferdev (≥ 30°)",
            ".3": "Haránt (< 30°)"
        },
        "13A3": {
            "1": "Ép ék",
            "2": "Töredezett ék"
            "3": "Többszörös törés"
        },
        "13B1": {
            "1": "Egyszerű transtrochlearis",
            "2": "Capitellum",
            "3": "Darabos transtrochlearis"
        },
        "13B2": {
            "1": "Egyszerű transtrochlearis, trochlea árkon át",
            "2": "Egyszerű transtrochlearis, a medialis ízfelszinen",
            "3": "Darabos transtrochlearis"
        },
        "13B3": {
            "1": "Capitellum ",
            "2": "Trochlea",
            "3": "Capitellum és trochlea"
        },
        "13C1": {
            "1": "Transcodylaris tengely felett",
            "3": "Transcodylaris tengelyen át vagy alatt"
        },
        "13C2": {
            "1": "Ép ék",
            "2": "Töredezett ék"
            "3": "Többszörös törés"
        },
        "13C3": {
            "1": "Egyszerű metapysealis",
            "2": "Ék metapysealis"
            "3": "Többszörös metapysealis"
        },
        "2U1B1": {
            "d": "Egyszeres",
            "e": "Többszörös"
        },
        "2U1B2": {
            "n": "Involving sublime facet",
            "o": "Csúcs (avulsio)"
            "p": "<50%"
            "q": "≥50%"            
        },
        "2R2A1": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "2R2A2": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "2R2A3": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "2U2A1": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "2U2A2": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "2U2A3": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "2R2B2": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "2R2B3": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "2U2B2": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "2U2B3": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "2R2C2": {
            "i": "Proximalis diaphysealis-metaphysealis",
            "j": "Tisztán diaphysealis"
            "k": "Distalis diaphysealis-metaphysealis"
        },
        "2R2C3": {
            "i": "Proximalis diaphysealis-metaphysealis",
            "j": "Tisztán diaphysealis"
            "k": "Distalis diaphysealis-metaphysealis"
        },
        "2U2C2": {
            "i": "Proximalis diaphysealis-metaphysealis",
            "j": "Tisztán diaphysealis"
            "k": "Distalis diaphysealis-metaphysealis"
        },
        "2U2C3": {
            "i": "Proximalis diaphysealis-metaphysealis",
            "j": "Tisztán diaphysealis"
            "k": "Distalis diaphysealis-metaphysealis"
        },
        "2R3A2": {
            ".1": "Haránt, elmozdulás/dőlés nélkül (esetleg rövidülés)",
            ".2": "Dorsalis elmozdulás/dőlés (Colles)",
            ".3": "Volaris elmozdulás/dőlés (Smith's)"
        },
        "2R3A3": {
            ".1": "Ép ék",
            ".2": "Darabos ék",
            ".3": "Többszörös"
        },
        "2U3A1": {
            ".1": "Styloideus csúcs",
            ".2": "Styloideus alap",
        },
        "2U3A2": {
            ".1": "Spirál",
            ".2": "Ferde (≥ 30°)",
            ".3": "Haránt (< 30°)"
        },
        "2R3B1": {
            ".1": "Fossa schaphoideumot érintő",
            ".2": "Fossa lunatumot érintő",
        },
        "2R3B2": {
            ".1": "Egyszeres",
            ".2": "Darabos",
            ".3": "Dorsalis dislocatioval"
        },
        "2R3B2": {
            ".1": "Egyszeres",
            ".3": "Darabos"
        },
        "2R3C1": {
            ".1": "Sagittalis ízületi",
            ".2": "Frontalis/coronalis"
            ".3": "Diaphyist érintő"
        },
        "2R3C2": {
            ".1": "Dorsomedialis ízületi",
            ".2": "Sagittalis ízületi",
            ".3": "Frontalis/coronalis ízületi"
        },
        "2R3C3": {
            ".1": "Egyszerű metaphysealis",
            ".2": "Metaphysealis darabos",
            ".3": "Diaphyist érintő"
        },
        "31A1": {
            "1": "Egyszerű pertrochantericus törés",
            "2": "Többszörös pertrochantericus törés",
            "3": "Intertrochantericus (fordított dőlésszög)"
        },
        "31B1": {
            "1": "Subcapitalis törés",
            "2": "Transcervicalis törés",
            "3": "Basicervicalis törés"
        },
        "31C1": {
            "1": "Repedés",
            "2": "Benyómódás"
        },
        "32A1": {
            "1": "Spirál",
            "2": "Ferdevágású (≥ 30°)",
            "3": "Haránt (< 30°)"
        },
        "32B2": {
            "1": "Ép ék",
            "2": "Töredezett ék"
        },
        "32C2": {
            "1": "Ép szegmentális",
            "2": "Töredezett szegmentális"
        },
        "33A1": {
            "1": "Avulsiós törés",
            "2": "Egyszerű törés",
            "3": "Ék vagy többrészű törés"
        },
        "33B1": {
            "1": "Lateralis condylus, sagittalis törés",
            "2": "Medialis condylus, sagittalis törés",
            "3": "Frontalis/coronalis törés"
        },
        "33C1": {
            "1": "Egyszerű ízületi, egyszerű metaphysealis törés",
            "2": "Egyszerű ízületi, ék vagy többrészű metaphysealis törés",
            "3": "Többszörös ízületi, ék vagy többrészű metaphysealis törés"
        },
        "41A1": {
            "1": "Avulsiós törés",
            "2": "Egyszerű törés",
            "3": "Ék vagy többrészű törés"
        },
        "41B1": {
            "1": "Repedés",
            "2": "Benyómódás",
            "3": "Repedés benyómódással"
        },
        "41C1": {
            "1": "Egyszerű ízületi, egyszerű metaphysealis törés",
            "2": "Egyszerű ízületi, ék vagy többrészű metaphysealis törés",
            "3": "Többszörös ízületi, többrészű metaphysealis törés"
        },
        "42A1": {
            "1": "Spirális törés",
            "2": "Ferdevágású törés (≥ 30°)",
            "3": "Haránt törés (< 30°)"
        },
        "42B2": {
            "1": "Ép ék",
            "2": "Töredezett ék"
        },
        "42C2": {
            "1": "Ép szegmentális",
            "2": "Töredezett szegmentális"
        },
        "43A1": {
            "1": "Egyszerű törés",
            "2": "Ék",
            "3": "Többszörös törés"
        },
        "43B1": {
            "1": "Repedés",
            "2": "Repedés benyómódással",
            "3": "Benyómódás"
        },
        "43C1": {
            "1": "Egyszerű ízületi, egyszerű metaphysealis törés",
            "2": "Egyszerű ízületi, többrészű metaphysealis törés",
            "3": "Többszörös ízületi és többrészű metaphysealis törés"
        },

    }
    return [f"{key} - {value}" for key, value in details.get(ao_type, {}).items()]

def get_ao_subsubsubseverity_details(ao_subsubtype):
    details = {
        "11B1.1": {
            "u": "Ép ék",
            "v": "Töredezett ék"
        },
        "11B1.2": {
            "u": "Ép ék",
            "v": "Töredezett ék"
        },
        "11C1.1": {
            "n": "Tuberculum majus töréssel",
            "o": "Tuberculum minus töréssel",
            "p": "Mindkét tuberculum"
        },
        "11C3.2": {
            "x": "Egyszerű ízületi",
            "y": "Multifragmentált, ízületi",
        },
        "11C3.3": {
            "x": "Egyszerű ízületi",
            "y": "Multifragmentált, ízületi",
        },        
        "13A3.1": {
            "f": "Lateralis",
            "h": "Medialis",
        },
        "13A3.2": {
            "f": "Lateralis",
            "h": "Medialis",
        },
        "13B1.2": {
            "q": "Transcapitellaris",
            "r": "Capitellum s trochlea között",
        },
        "13C2.1": {
            "f": "Lateralis",
            "h": "Medialis",
            "u": "Ép ék"
        },
        "13C2.2": {
            "f": "Lateralis",
            "h": "Medialis",
            "u": "Ép ék"
        },
        "13C3.1": {
            "s": "Proximalis a transcondylaris tengelytől",
            "t": "Distalis a transcondylaris tengelytől",
        },
        "13C3.2": {
            "f": "Lateralis",
            "h": "Medialis",
            "l": "Darabos"
            "u": "Ép ék"
        },
        "2R3C1.1": {
            "t": "DRUJ stabil",
            "u": "DRUJ instabil"
        },
        "2R3C1.2": {
            "t": "DRUJ stabil",
            "u": "DRUJ instabil"
        },
        "2R3C1.3": {
            "t": "DRUJ stabil",
            "u": "DRUJ instabil"
        },
        "2R3C2.1": {
            "t": "DRUJ stabil",
            "u": "DRUJ instabil"
        },
        "2R3C2.2": {
            "t": "DRUJ stabil",
            "u": "DRUJ instabil"
        },
        "2R3C2.3": {
            "t": "DRUJ stabil",
            "u": "DRUJ instabil"
        },        
        "2R3C2.1": {
            "t": "DRUJ stabil",
            "u": "DRUJ instabil"
        },
        "2R3C3.2": {
            "t": "DRUJ stabil",
            "u": "DRUJ instabil"
        },
        "2R3C3.3": {
            "t": "DRUJ stabil",
            "u": "DRUJ instabil"
        },
        "31A1.1": {
            "1": "Egyszerű pertrochantericus törés",
            "2": "Többszörös pertrochantericus törés",
            "3": "Intertrochantericus (fordított dőlésszög)"
        },
        "31A1.2": {
            "1": "Egyszerű pertrochantericus törés",
            "2": "Többszörös pertrochantericus törés",
            "3": "Intertrochantericus (fordított dőlésszög)"
        },
        "31B1.1": {
            "1": "Subcapitalis törés",
            "2": "Transcervicalis törés",
            "3": "Basicervicalis törés"
        },
        "31B1.2": {
            "1": "Subcapitalis törés",
            "2": "Transcervicalis törés",
            "3": "Basicervicalis törés"
        },
        "31C1.1": {
            "1": "Repedés",
            "2": "Benyomódás"
        },
        "31C1.2": {
            "1": "Repedés",
            "2": "Benyomódás"
        },
        "32A1.1": {
            "1": "Spirális törés",
            "2": "Ferdevágású törés (≥ 30°)",
            "3": "Haránt törés (< 30°)"
        },
        "32A1.2": {
            "1": "Spirális törés",
            "2": "Ferdevágású törés (≥ 30°)",
            "3": "Haránt törés (< 30°)"
        },
        "32B2.1": {
            "1": "Ép ék",
            "2": "Töredezett ék"
        },
        "32B2.2": {
            "1": "Ép ék",
            "2": "Töredezett ék"
        },
        "32C2.1": {
            "1": "Ép szegmentális",
            "2": "Töredezett szegmentális"
        },
        "32C2.2": {
            "1": "Ép szegmentális",
            "2": "Töredezett szegmentális"
        },
        "33A1.1": {
            "1": "Avulsiós törés",
            "2": "Egyszerű törés",
            "3": "Ék vagy többrészű törés"
        },
        "33A1.2": {
            "1": "Avulsiós törés",
            "2": "Egyszerű törés",
            "3": "Ék vagy többrészű törés"
        },
        "33B1.1": {
            "1": "Lateralis condylus, sagittalis törés",
            "2": "Medialis condylus, sagittalis törés",
            "3": "Frontalis/coronalis törés"
        },
        "33B1.2": {
            "1": "Lateralis condylus, sagittalis törés",
            "2": "Medialis condylus, sagittalis törés",
            "3": "Frontalis/coronalis törés"
        },
        "33C1.1": {
            "1": "Egyszerű ízületi, egyszerű metaphysealis törés",
            "2": "Egyszerű ízületi, ék vagy többrészű metaphysealis törés",
            "3": "Többszörös ízületi, ék vagy többrészű metaphysealis törés"
        },
        "33C1.2": {
            "1": "Egyszerű ízületi, egyszerű metaphysealis törés",
            "2": "Egyszerű ízületi, ék vagy többrészű metaphysealis törés",
            "3": "Többszörös ízületi, ék vagy többrészű metaphysealis törés"
        },
        "41A1.1": {
            "1": "Avulsiós törés",
            "2": "Egyszerű törés",
            "3": "Ék vagy többrészű törés"
        },
        "41A1.2": {
            "1": "Avulsiós törés",
            "2": "Egyszerű törés",
            "3": "Ék vagy többrészű törés"
        },
        "41B1.1": {
            "1": "Repedés",
            "2": "Benyomódás",
            "3": "Repedés benyomódással"
        },
        "41B1.2": {
            "1": "Repedés",
            "2": "Benyomódás",
            "3": "Repedés benyomódással"
        },
        "41C1.1": {
            "1": "Egyszerű ízületi, egyszerű metaphysealis törés",
            "2": "Egyszerű ízületi, ék vagy többrészű metaphysealis törés",
            "3": "Többszörös ízületi, többrészű metaphysealis törés"
        },
        "41C1.2": {
            "1": "Egyszerű ízületi, egyszerű metaphysealis törés",
            "2": "Egyszerű ízületi, ék vagy többrészű metaphysealis törés",
            "3": "Többszörös ízületi, többrészű metaphysealis törés"
        },
        "42A1.1": {
            "1": "Spirális törés",
            "2": "Ferdevágású törés (≥ 30°)",
            "3": "Haránt törés (< 30°)"
        },
        "42A1.2": {
            "1": "Spirális törés",
            "2": "Ferdevágású törés (≥ 30°)",
            "3": "Haránt törés (< 30°)"
        },
        "42B2.1": {
            "1": "Ép ék",
            "2": "Töredezett ék"
        },
        "42B2.2": {
            "1": "Ép ék",
            "2": "Töredezett ék"
        },
        "42C2.1": {
            "1": "Ép szegmentális",
            "2": "Töredezett szegmentális"
        },
        "42C2.2": {
            "1": "Ép szegmentális",
            "2": "Töredezett szegmentális"
        },
        "43A1.1": {
            "1": "Egyszerű törés",
            "2": "Ék",
            "3": "Többszörös törés"
        },
        "43A1.2": {
            "1": "Egyszerű törés",
            "2": "Ék",
            "3": "Többszörös törés"
        },
        "43B1.1": {
            "1": "Repedés",
            "2": "Repedés benyomódással",
            "3": "Benyomódás"
        },
        "43B1.2": {
            "1": "Repedés",
            "2": "Repedés benyomódással",
            "3": "Benyomódás"
        },
        "43C1.1": {
            "1": "Egyszerű ízületi, egyszerű metaphysealis törés",
            "2": "Egyszerű ízületi, többrészű metaphysealis törés",
            "3": "Többszörös ízületi és többrészű metaphysealis törés"
        },
        "43C1.2": {
            "1": "Egyszerű ízületi, egyszerű metaphysealis törés",
            "2": "Egyszerű ízületi, többrészű metaphysealis törés",
            "3": "Többszörös ízületi és többrészű metaphysealis törés"
        },
    }
    return [f"{key} - {value}" for key, value in details.get(ao_subsubtype, {}).items()]

def neer_classification(sub_sub_reg):
    neer_classes = {
        "Proximalis humerus": {
            "I": "Egy része érintett (<1 cm elmozdulás, <45° szög)",
            "II": "Két része érintett (tuberositas majus/minor törés, nyak törés)",
            "III": "Három része érintett (fej, nyak, tuberositas)",
            "IV": "Négy része érintett (fej, nyak, tuberositas majus és minor)"
        },
        "Distalis humerus": {
            "I": "Medial Epicondyle",
            "II": "Lateral Epicondyle",
            "III": "Capitellum",
            "IV": "Trochlea"
        },
        "Humerus diaphysis": {
            "I": "Spirális törés",
            "II": "Ferde törés",
            "III": "Keresztirányú törés",
            "IV": "Komplex törés"
        },
        "Proximalis femur": {
            "I": "Subcapitalis törés",
            "II": "Transcervicalis törés",
            "III": "Basicervicalis törés",
            "IV": "Intertrochanterikus törés"
        },
        "Distalis femur": {
            "I": "Condylar törés",
            "II": "Intercondylar törés",
            "III": "Supracondylar törés",
            "IV": "Complex törés"
        }
    }

    neer_type = st.selectbox("Neer osztályozás típusa", neer_classes.get(sub_sub_reg, {}).keys())
    neer_description = neer_classes.get(sub_sub_reg, {}).get(neer_type, "")
    
    classification_name = "Neer osztályozás"
    severity = neer_type
    description = neer_description
    
    return classification_name, severity, description

def gartland_classification():
    gartland_types = {
        "I": "Nem elmozdult törés",
        "II": "Elmozdult törés, intakt hátsó cortex",
        "III": "Teljes elmozdult törés, nincs érintkezés a cortikálisok között",
        "IV": "Elmozdult törés instabil minden síkban"
    }
    
    gartland_type = st.selectbox("Gartland osztályozás", gartland_types.keys())
    gartland_description = gartland_types.get(gartland_type, "")
    
    classification_name = "Gartland osztályozás"
    severity = gartland_type
    description = gartland_description
    
    return classification_name, severity, description
