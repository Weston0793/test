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
        "Alsó végtag": ["", "Pelvis", "Femur", "Térd", "Lábszár", "Boka", "Láb"],
        "Gerinc": ["", "Cervicalis", "Thoracalis", "Lumbalis", "Sacralis"],
        "Koponya": ["", "Arckoponya", "Mandibula", "Calvaria", "Koponyaalap", "Fog"],
        "Mellkas": ["", "Thorax", "Tüdő", "Szív", "Mell"],
        "Has": ["", "Gyomor", "Vékonybél", "Vastagbél", "Vese", "Húgyhólyag", "Máj", "Epehólyag", "Pancreas", "Lép"]
    }
    return st.selectbox("Régió", regions.get(main_reg, [""]))

def select_sub_subregion(sub_reg):
    sub_regions = {
        "Váll": ["", "Clavicula", "Scapula", "Proximális humerus"],
        "Humerus": ["", "Humerus diaphysis"],
        "Könyök": ["", "Distalis humerus", "Proximalis ulna", "Proximalis radius"],
        "Alkar": ["", "Ulna diaphysis", "Radius diaphysis", "Nightstick", "Essex-Lopresti", "Galeazzi", "Monteggia"],
        "Csukló": ["", "Distalis radius", "Distalis ulna", "Scaphoideum", "Lunatum", "Capitatum", "Triquetrum", "Pisiforme", "Hamatum", "Trapesoideum", "Trapesium"],
        "Kéz": ["", "Metacarpus", "Pollex", "Phalanx"],
        "Pelvis": ["", "Medencegyűrű",  "Acetabulum", "Anterior inferior csípőtövis avulsio",  "Anterior superior csípőtövis avulsio", "Duverney", "Malgaigne", "Windswept pelvis", "Pelvic bucket handle", "Medencei elégtelenség"],
        "Femur": ["","Proximalis femur", "Femur diaphysis", "Bisphosphonáthoz kapcsolódó"],
        "Térd": ["", "Distalis femur", "Avulsio", "Patella",  "Proximalis tibia", "Proximalis fibula"],
        "Lábszár": ["", "Tibia diaphysis", "Fibula diaphysis", "Tuberositas tibiae avulsio", "Maisonneuve"],
        "Boka": ["", "Distalis tibia", "Distalis fibula", "Malleolaris", "Talus"],
        "Láb": ["", "Calcaneus", "Naviculare", "Cuneiforme mediale", "Cuneiforme intermedium", "Cuneiforme laterale", "Cuboideum", "Metatarsus", "Hallux", "Lábujj"],
        "Cervicalis": ["", "C1", "C2", "C3", "C4", "C5", "C6", "C7"],
        "Thoracalis": ["", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10", "T11", "T12"],
        "Lumbalis": ["", "L1", "L2", "L3", "L4", "L5"], 
        "Sacralis": ["", "Sacrum", "Coccyx"], 
        "Arckoponya": ["", " Orrcsont", "Orbita", "Zygomaticum", "Arcus zygomaticus", "Processus alveolaris", "Panfacialis"], 
        "Mandibula": ["", "Corpus mandibulae", "Symphysis", "Szemfogtájék", "Szemfog és angulus között", "Angulus mandibulae", "Ramus mandibulae", "Processus articularis", "Processus muscularis"],  
        "Calvaria": ["", "Frontale", "Parietale", "Temporale", "Occipitale"], 
        "Koponyaalap": ["","Condylus occipitalis", "Fossa anterior", "Fossa mediale", "Fossa posterior"],
        "Fog": ["", "Szemfog", "Metszőfog", "Kisörlő", "Nagyörlő"],
        "Thorax": ["", "Borda", "Sternum"]
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
        "Scaphoideum": ["", "De Quervain"],
        "Hamatum": ["", "Hamulus"],
        "Metacarpus": ["",  "Boxer", "Fordított Bennett"],
        "Pollex": ["", "Distalis phalanx", "Proximalis phalanx", "Gamekeeper's Thumb", "Epibasalis", "Rolando", "Bennett"],
        "Phalanx": ["", "Distalis phalanx", "Középső phalanx", "Proximalis phalanx"],
        "Medencegyűrű": ["", "Nyitott könyv", "Ramus pubicus"],
        "Proximalis femur": ["", "Femur fej", "Femur nyak", "Trochanterikus"],
        "Avulsio": ["", "Lig. cruciatum anterior", " Lig. cruciatum posterior", "Arcuatus komplex (arcuatus jel)", "Biceps femoris", "Lig. iliotibiale", "Semimembranosus ín", "Segond", "Fordított Segond", "Stieda (MCL avulsiós törés)"],
        "Proximalis tibia": ["", "Tibia plateau"],
        "Proximalis fibula": ["", "Fibula fej", "Fibula nyak"],
        "Distalis tibia": ["", "Pilon"],
        "Malleolaris": ["",  "Bimalleolaris", "Trimalleolaris", "Triplane", "Tillaux", "Bosworth", "Wagstaffe-Le Fort"],
        "Calcaneus": ["", "Lover's", "Calcaneus tuberositas avulsio"],
        "Talus": ["", "Talus test", "Talus nyak", "Talus fej", "Talus kupola", "Posterior talus processus", "Lateralis talus processus", "Aviator astragalus"],
        "Cuboideum": ["", "Nutcracker"],
        "Metatarsus": ["", "March", "Lisfranc törés-luxatio", "V. metatarsus stressz törés", "Jones", "Pseudo-Jones", "V. metatarsus proximalis avulsio"],
        "C1": ["","Jefferson"],
        "C2": ["", "Dens axis", "Csigolyatest", "Hangman"],
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
        "Distalis phalanx": ["", "Basis", "Corpus", "Caput", "Jersey Finger", "Mallet Finger", "Seymour"],
        "Középső phalanx": ["", "Basis", "Corpus", "Caput", "Volar Plate avulsio", "Pilon"],
        "Proximalis phalanx": ["", "Basis", "Corpus", "Caput"],
        "Femur nyak": ["", "Subcapitalis", "Transcervicalis", "Basicervicalis"],
        "Trochanterikus": ["", "Pertrochanterikus", "Intertrochanterikus", "Subtrochanterikus"],
        "Dens axis": ["", "Dens csúcs", "Dens basis", "Csigolyatestre terjedő"]
    }
    return st.selectbox("Legpontosabb régió", sub_sub_sub_regions.get(sub_sub_sub_reg, [""]))  
    
def select_finger(sub_sub_regions):
    side = st.selectbox("Oldal", ["Bal", "Jobb"])
    
    finger = None
    if sub_sub_regions in ["Metacarpus", "Phalanx", "Metatarsus", "Lábujj", "Pollex", "Hallux"]:
        if sub_sub_regions in ["Pollex", "Hallux"]:
            finger = "I"
        elif sub_sub_regions in ["Phalanx", "Lábujj"]:
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
         "Scapula": {
            "14A": "Processus",
            "14B": "Corpus",
            "14C": "Fossa glenoidale"
        }, 
         "Clavicula": {
            "15.1": "Proximalis/medialis",
            "15.2": "Diaphysealis",
            "15.3": "Distalis/lateralis"
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
        },
        "Proximalis femur": {
            "31A": "Trochanter régió",
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
        "Patella": {
            "34A": "Extraarticularis",
            "34B": "Részleges ízületi, sagittalis",
            "34C": "Teljes ízületi, frontalis/coronalis"
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
        "Proximalis fibula": {
            "4F1A": "Egyszeres",
            "4F1B": "Többszörös",
        },
        "Fibula diaphysis": {
            "4F2A": "Egyszeres",
            "4F2B": "Ék vagy többszörös",
        },
        "Distalis fibula": {
            "4F3A": "Egyszeres",
            "4F3B": "Ék vagy többszörös",
        },
        "Malleolaris": {
            "44A": "Infrasyndesmoticus fibula",
            "44B": "Transsyndesmoticus fibula",
            "44C": "Suprasyndesmoticus fibula"
        },
        "Medencegyűrű": {
            "61A": "Ép posterior ív",
            "61B": "Inkomplett posterior ív disruptio",
            "61C": "Komplett posterior ív disruptio"
        },
        "Acetabulum": {
            "62A": "Részleges ízületi, izolált oszlop és/vagy fal",
            "62B": "Részleges ízületi, haránt",
            "62C": "Teljes ízületi, mindkét oszlop"
        },
        "Lunatum": {
            "71A": "Avulsiós",
            "71B": "Egyszerű",
            "71C": "Többszörös"
        }, 
        "Scaphoideum": {
            "72A": "Avulsiós",
            "72B": "Egyszerű",
            "72C": "Többszörös"
        },
        "Capitatum": { 
            "73A": "Avulsiós",
            "73B": "Egyszerű",
            "73C": "Többszörös"
        }, 
        "Hamatum": {
            "74A": "Avulsiós",
            "74B": "Egyszerű",
            "74C": "Többszörös"
        },
        "Trapesium": {
            "75A": "Avulsiós",
            "75B": "Egyszerű",
            "75C": "Többszörös"
        },
        "Pisiforme": {
            "76.1.A": "Avulsiós",
            "76.1.B": "Egyszerű",
            "76.1.C": "Többszörös"
        },
        "Triquetrum": {
            "76.2.A": "Avulsiós",
            "76.2.B": "Egyszerű",
            "76.2.C": "Többszörös"
        },
        "Trapesoideum": {
            "76.3.A": "Avulsiós",
            "76.3.B": "Egyszerű",
            "76.3.C": "Többszörös"
        },
        "Metacarpus": {
            "77.X.1": "Proximalis",
            "77.X.2": "Diaphysealis",
            "77.X.3": "Distalis"
        },
        "Phalanx": {
            "78.X.X.1": "Proximalis",
            "78.X.X.2": "Diaphysealis",
            "78.X.X.3": "Distalis"
        },
        "Talus": {
            "81.1": "Corpus",
            "81.2": "Collum",
            "81.3": "Caput"
        },
        "Calcaneus": {
            "82A": "Extraarticularis",
            "82B": "Nyelv-típusú, facies talaris posteriorig terjedő",
            "82C": "Teljes ízületi"
        },
        "Naviculare": {
            "83A": "Avulsiós",
            "83B": "Részleges ízületi",
            "83C": "Teljes ízületi"
        },
        "Cuboideum": {
            "84A": "Avulsiós",
            "84B": "Részleges ízületi",
            "84C": "Teljes ízületi"
        },
        "Cuneiforme mediale": {
            "85.1.A": "Avulsiós",
            "85.1.B": "Részleges ízületi",
            "85.1.C": "Teljes ízületi"
        },
        "Cuneiforme intermedium": {
            "85.2.A": "Avulsiós",
            "85.2.B": "Részleges ízületi",
            "85.2.C": "Teljes ízületi"
        },
        "Cuneiforme laterale": {
            "85.3.A": "Avulsiós",
            "85.3.B": "Részleges ízületi",
            "85.3.C": "Teljes ízületi"
        },
        "Metatarsus": {
            "87.X.1": "Proximalis",
            "87.X.2": "Diaphysealis",
            "87.X.3": "Distalis"
        },
        "Lábujj": {
            "88.X.1": "Proximalis",
            "88.X.2": "Diaphysealis",
            "88.X.3": "Distalis"
        },
        **{f"C{i}": {
            f"51.{i}.A": "Corpus vertebrae, kompressziós sérülés",
            f"51.{i}.B": "Tension band injury",
            f"51.{i}.C": "Elmozdulás/Translational"      
        } for i in range(1, 8)},
        **{f"T{i}": {
            f"52.{i}.A": "Corpus vertebrae, kompressziós sérülés",
            f"52.{i}.B": "Tension band injury",
            f"52.{i}.C": "Elmozdulás/Translational"      
        } for i in range(1, 13)},
        **{f"L{i}": {
            f"53.{i}.A": "Corpus vertebrae, kompressziós sérülés",
            f"53.{i}.B": "Tension band injury",
            f"53.{i}.C": "Elmozdulás/Translational"      
        } for i in range(1, 6)},

        "Sacrum": {
            "54A": "Sacroiliacalis ízület ép, alsó szegmens sérülés",
            "54B": "Sacroiliacalis ízület károsodott, felső szegmens sérülés",
            "54C": "Spino-pelvicalis instabilitás"      
         },
        "Borda": {
            "16.X.1": "Posterior (costotransversalis ízületek)",
            "16.X.2": "Diaphysealis",
            "16.X.3": "Anterior (costochondralis porc)"
        },
        "Sternum": {
            "16.3.1": "Manubrium",
            "16.3.2": "Corpus",
            "16.3.3": "Xyphoideus"
        }
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
            "1": "Spirál",
            "2": "Ferde (≥ 30°)",
            "3": "Haránt (< 30°)"
        },
        "12B": {
            "2": "Ép ék",
            "3": "Darabos ék"
        },
        "12C": {
            "2": "Ép szegmentális",
            "3": "Darabos szegmentális"
        },
        "13A": {
            "1": "Avulsio",
            "2": "Egyszeres",
            "3": "Ék vagy többszörös"
        },
        "13B": {
            "1": "Laterális sagittális",
            "2": "Mediális sagittális",
            "3": "Frontalis/coronalis"
        },
        "13C": {
            "1": "Egyszerű ízületi, egyszerű metaphysealis",
            "2": "Egyszerű ízületi, ék vagy többszörös metaphysealis",
            "3": "Többszörös ízületi, ék vagy többszörös metaphysealis"
        },
        "14A": {
            "1": "Coracoideus",
            "2": "Acromion",
            "3": "Spina scapulae"
        },        
        "14B": {
            "1": "A törésvonal max. 2 helyen hagyja el a corpust",
            "2": "A törésvonal 3 vagy több helyen hagyja el a corpust"
        }, 
        "14F": {
            "0": "Az extraarticularis, subchondralis fossán át (glenoid neck)",
            "1": "Egyszeres",
            "2": "Többszörös (3 vagy több törésvonal)"           
        },        
        "15.1": {
            "A": "Extraarticularis, epiphysealis lemezt is beleértve!",
            "B": "Részleges ízületi",
            "C": "Teljes ízületi"
        },
        "15.2": {
            "A": "Egyszeres",
            "B": "Ék",
            "C": "Többszörös"
        },
        "15.3": {
            "A": "Extraarticularis, epiphysealis lemezt is beleértve!",
            "B": "Részleges ízületi",
            "C": "Teljes ízületi"
        },
        "2R1A": {
            "1": "Tuberositas bicipitalis avulsiós törés",
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
            "3": "Darabos ék"
        },
        "2R2C": {
            "1": "Ép szegmentális",
            "2": "Darabos szegmentális"
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
            "1": "Spirál",
            "2": "Ferde(≥ 30°)",
            "3": "Haránt (< 30°)"
        },
        "2U2B": {
            "2": "Ép ék",
            "3": "Darabos ék"
        },
        "2U2C": {
            "2": "Ép szegmentális",
            "3": "Darabos szegmentális"
        },
        "2U3A": {
            "1": "Processus styloideus avulsiós törés",
            "2": "Egyszeres",
            "3": "Többszörös"
        },
        "31A": {
            "1": "Egyszerű pertrochanter",
            "2": "Többszörös pertrochanter (lateralis fal elégtelen)",
            "3": "Intertrochanter (fordított dőlésszög)"
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
            "1": "Spirál",
            "2": "Ferde (≥ 30°)",
            "3": "Haránt (< 30°)"
        },
        "32B": {
            "2": "Ép ék",
            "3": "Darabos ék"
        },
        "32C": {
            "2": "Ép szegmentális",
            "3": "Darabos szegmentális"
        },
        "33A": {
            "1": "Avulsio",
            "2": "Egyszeres",
            "3": "Ék vagy többszörös"
        },
        "33B": {
            "1": "Lateralis condylus, sagittalis",
            "2": "Medialis condylus, sagittal",
            "3": "Frontalis/coronalis"
        },
        "33C": {
            "1": "Egyszerű ízületi, egyszerű metaphysealis",
            "2": "Egyszerű ízületi, ék vagy többszörös metaphysealis",
            "3": "Többszörös ízületi, egyszerű, ék vagy többszörös metafízis"
        },
        "34A": {
            "1": "Avulsio",
        },
        "34B": {
            "2": "Lateralis",
            "3": "Medialis"
        },
        "34C": {
            "1": "Frontalis/coronalis, egyszeres",
            "2": "Ék",
            "3": "Többszörös"
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
            "1": "Egyszerű ízületi, egyszerű metaphysealis",
            "2": "Egyszerű ízületi, többszörös metaphysealis",
            "3": "Többszörös ízületi és többszörös metaphysealis"
        },
        "42A": {
            "1": "Spirál",
            "2": "Ferde (≥ 30°)",
            "3": "Haránt (< 30°)"
        },
        "42B": {
            "2": "Ép ék",
            "3": "Darabos ék"
        },
        "42C": {
            "2": "Ép szegmentális",
            "3": "Darabos szegmentális"
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
            "1": "Egyszerű ízületi, egyszerű metaphysealis",
            "2": "Egyszerű ízületi, többszörös metaphysealis",
            "3": "Többszörös ízületi és többszörös metaphysealis"
        },
        "4F1A": {
            "n": "Extraarticularis",
            "o": "Intraarticularis",
        },
        "4F1B": {
            "n": "Extraarticularis",
            "o": "Intraarticularis",
        },
        "4F2A": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "4F2B": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "44A": {
            "1": "Izolált fibula",
            "2": "Medialis malleolus",
            "3": "Posteromedialis"
        },
        "44B": {
            "1": "Izolált fibula",
            "2": "Medialis sérüléssel",
            "3": "Medialis sérüléssel és posterolateralis peremtöréssel (Volkmann fragmentum)"
        },
        "44C": {
            "1": "Egyszerű diaphysealis fibula",
            "2": "Ék vagy többszörös fibula",
            "3": "Proximalis fibula"
        },
        **{f"51.{i}.A": {
            "0": "Minor, nonstruktúrális sérülés",
            "1": "Kompresszió vagy egy véglemez impaktált fractura, nem érintett a gerinc test posterior fal",
            "2": "Coronalis hasadás (split), harapófogó (pincer) típusú fractúrája mindkét véglemeznek, nem érintett a gerinc test posterior fal",
            "3": "Inkomplett burst fractura, egy véglemez és gerinc test posterior fal sérült",
            "4": "Komplett burst fractura, mindkét véglemez és gerinc test posterior fal sérült"
        } for i in range(1, 8)},
        **{f"51.{i}.B": {
            "1": "Monosegmentalis ossealis elégtelensége a posterior tension band-nek, ami érinti a gerinc testet (Chance)",
            "2": "Posterior tension band disruptio (csont, szalag, tok, vagy kombinációjuk)",
            "3": "Anterior tension band sérülés, fizikai disruptio vagy separatio az anterior struktúrákban és posterior tethering fractura, egy véglemez és gerinc test posterior fal sérült"
        } for i in range(1, 8)},
        **{f"51.{i}.C": {
            "F1": "Elmozdulás nélküli ízfelszín sérülés (fragment < 1cm és <40%-a a lateralis tömegnek)",
            "F2": "Ízfelszín fractura, potenciális instabilitás (fragment > 1cm és >40%-a a lateralis tömegnek vagy elmozdult)",
            "F3": "Lebegő lateralis tömeg (Floating lateral mass)",
            "F4": "Peremes (perched) vagy dislocált ízfelszin subluxatio)"
        } for i in range(1, 8)},
        **{f"52.{i}.A": {
            "0": "Minor, nonstruktúrális sérülés",
            "1": "Kompresszió vagy egy véglemez impaktált fractura, nem érintett a gerinc test posterior fal",
            "2": "Coronalis hasadás (split), harapófogó (pincer) típusú fractúrája mindkét véglemeznek, nem érintett a gerinc test posterior fal",
            "3": "Inkomplett burst fractura, egy véglemez és gerinc test posterior fal sérült",
            "4": "Komplett burst fractura, mindkét véglemez és gerinc test posterior fal sérült"
        } for i in range(1, 13)},
        **{f"52.{i}.B": {
            "1": "Monosegmentalis ossealis elégtelensége a posterior tension band-nek, ami érinti a gerinc testet (Chance)",
            "2": "Posterior tension band disruptio (csont, szalag, tok, vagy kombinációjuk)",
            "3": "Anterior tension band sérülés, fizikai disruptio vagy separatio az anterior struktúrákban és posterior tethering fractura, egy véglemez és gerinc test posterior fal sérült"
        } for i in range(1, 13)},
        **{f"52.{i}.C": {
            "NX": "Nem vizsgálható",
            "N0": "Neurológiailag ép",
            "N1": "Transiens neurológiai deficit",
            "N2": "Ideggyök sérülés",
            "N3": "Cauda equina sérülés vagy inkomplett gerincvelő sérülés",
            "N4": "Komplett gerincvelő sérülés"
        } for i in range(1, 13)},
        **{f"53.{i}.A": {
            "0": "Minor, nonstruktúrális sérülés",
            "1": "Kompresszió vagy egy véglemez impaktált fractura, nem érintett a gerinc test posterior fal",
            "2": "Coronalis hasadás (split), harapófogó (pincer) típusú fractúrája mindkét véglemeznek, nem érintett a gerinc test posterior fal",
            "3": "Inkomplett burst fractura, egy véglemez és gerinc test posterior fal sérült",
            "4": "Komplett burst fractura, mindkét véglemez és gerinc test posterior fal sérült"
        } for i in range(1, 6)},
        **{f"53.{i}.B": {
            "1": "Monosegmentalis ossealis elégtelensége a posterior tension band-nek, ami érinti a gerinc testet (Chance)",
            "2": "Posterior tension band disruptio (csont, szalag, tok, vagy kombinációjuk)",
            "3": "Anterior tension band sérülés, fizikai disruptio vagy separatio az anterior struktúrákban és posterior tethering fractura, egy véglemez és gerinc test posterior fal sérült"
        } for i in range(1, 6)},
        **{f"53.{i}.C": {
            "NX": "Nem vizsgálható",
            "N0": "Neurológiailag ép",
            "N1": "Transiens neurológiai deficit",
            "N2": "Ideggyök sérülés",
            "N3": "Cauda equina sérülés vagy inkomplett gerincvelő sérülés",
            "N4": "Komplett gerincvelő sérülés"
        } for i in range(1, 6)},
        "54A": {
            "1": "Coccygealis vagy sacralis kompresszió",
            "2": "Haránt fractura, nincs elmozdulás",
            "3": "Haránt fractura, elmozdulással"
        },
       "54B": {
            "1": "Izolált verticalis centralis fractura, medialisan a foramina-tól, érinti a gerinccsatornát (Dennis III)",
            "2": "Transalaris fractura, lateralisan a foramina-tól vagy a gerinccsatornától (Dennis I)",
            "3": "Transforaminalis fractura, érintve a foraminát de nem a gerinccsatornát (Dennis II)"
        },       
        "54C": {
            "0": "Elmozdulás nélküli, U-variáns (alacsony energiájú elégtelenség fractura)",
            "1": "U-variáns, posterior elégtelenség nélkül",
            "2": "Bilateralis B-típusú sérülés, haránt fractura nélkül",
            "3": "Elmozdult U-variáns",            
        },
        "61A": {
            "1": "Avulsio",
            "2": "Fractura",
            "3": "Haránt törés (S3,4,5 és coccyx)"
        },
        "61B": {
            "1": "Nincs rotációs instabilitás",
            "2": "Rotációs instabilitás, unilateralis posterior sérülés",
            "3": "Rotációs instabilitás, bilateralis sérülés"
        },
        "61C": {
            "1": "Unilateralis posterior sérülés (APC3, vertikális nyírás (shear))",
            "2": "Bilateralis posterior sérülés, hemipelvicus komplett disruptio, contralateralis hemipelvicus inkomplett disruptio (LC3)",
            "3": "Bilateralis posterior sérülés, bilateralis komplett disruptio (APC3, vertikális nyírás (shear))"
        },
        "62A": {
            "1": "Posterior fal",
            "2": "Posterior oszlop (columna)",
            "3": "Anterior oszlop (columna) vagy fal"
        },
        "62B": {
            "1": "Haránt fractura",
            "2": "T fractura",
            "3": "Anterior oszlop (columna) és posterior hemitransversalis fractura"
        },
        "62C": {
            "1": "Felső anterior oszlop (columna)(a crista iliacán át)",
            "2": "Alsó anterior oszlop (columna) (SIAS alatt)",
            "3": "Sacroiliacalis ízületet érintő"
        },
        "72B": {
            "a": "Proximalis pólus",
            "b": "Derék",
            "c": "Distalis pólus"
        },
        "72C": {
            "a": "Proximalis pólus",
            "b": "Derék",
            "c": "Distalis pólus"
        },
        "77.X.1": {
            "A": "Extraarticularis",
            "B": "Részleges ízületi",
            "C": "Teljes ízületi"
        },
        "77.X.2": {
            "A": "Egyszeres",
            "B": "Ék",
            "C": "Többszörös"
        },
        "77.X.3": {
            "A": "Extraarticularis",
            "B": "Részleges ízületi",
            "C": "Teljes ízületi"
        },
        "78.X.X.1": {
            "A": "Extraarticularis",
            "B": "Részleges ízületi",
            "C": "Teljes ízületi"
        },
        "78.X.X.2": {
            "A": "Egyszeres",
            "B": "Ék",
            "C": "Többszörös"
        },
        "78.X.X.3": {
            "A": "Extraarticularis",
            "B": "Részleges ízületi",
            "C": "Teljes ízületi"
        },
        "81.1": {
            ".A": "Avulsio",
            ".B": "Részleges ízületi",
            ".C": "Teljes ízületi"
        },  
        "81.2": {
            ".A": "Nincs elmozdulás (Hawkins 1)",
            ".B": "Elmozdult és subtalaris ízület subluxatio/dislocatio (Hawkins 2)",
            ".C": "Elmozdult talus nyak és talus test dislocatio (Hawkins 3)",
            ".D": "Elmozdult talus nyak, test és fej dislocatióval (Hawkins 4)"
        },  
        "81.3": {
            ".A": "Avulsio",
            ".B": "Részleges ízületi",
            ".C": "Teljes ízületi"
        },  
        "82A": {
            "1": "Avulsio, tuberositas posterior fractura vagy extraarticularis nyelv fractura",
            "2": "Test fractura"
        },  
        "82B": {
            "1": "Nyelv-típusú, egyszeres fractura",
            "3": "Többszörös fractura"
        },  
        "82C": {
            "1": "Ízületi depressióval (Sanders 2)",
            "2": "Ízületi depressióval (Sanders 3)",
            "3": "Többszörös fractura (Sanders 4)"
        },  
        "83B": {
            "a": "Egyszeres",
            "b": "Többszörös "
        },
        "83C": {
            "a": "Egyszeres",
            "b": "Többszörös "
        },
        "84B": {
            "a": "Egyszeres",
            "b": "Többszörös "
        },
        "84C": {
            "a": "Egyszeres",
            "b": "Többszörös "
        },
        "87.X.1": {
            "A": "Extraarticularis",
            "B": "Részleges ízületi",
            "C": "Teljes ízületi"
        },
        "87.X.2": {
            "A": "Egyszeres",
            "B": "Ék",
            "C": "Többszörös"
        },
        "87.X.3": {
            "A": "Extraarticularis",
            "B": "Részleges ízületi",
            "C": "Teljes ízületi"
        },
        "88.X.1": {
            "A": "Extraarticularis",
            "B": "Részleges ízületi",
            "C": "Teljes ízületi"
        },
        "88.X.2": {
            "A": "Egyszeres",
            "B": "Ék",
            "C": "Többszörös"
        },
        "88.X.3": {
            "A": "Extraarticularis",
            "B": "Részleges ízületi",
            "C": "Teljes ízületi"
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
            ".1": "Valgus impressiós",
            ".3": "Izolált collum anatomicum"
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
            "j": "Tisztán diaphysealis",
            "k": "Distalis diaphysealis-metaphysealis"
        },
        "12C3": {
            "i": "Proximalis diaphysealis-metaphysealis",
            "j": "Tisztán diaphysealis",
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
            "2": "Töredezett ék",
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
            "2": "Darabos ék",
            "3": "Többszörös"
        },
        "13C3": {
            "1": "Egyszerű metapysealis",
            "2": "Ék metapysealis",
            "3": "Többszörös metapysealis"
        },
        "14B1": {
            "l": "Lateralis határon át lép ki a törés",
            "m": "Medialis határon át lép ki a törés",
            "s": "Superior határon át lép ki a törés",
            "g": "A lateralis basisát érinti a coracoideusnak (glenoid site exit)",
            "x": "Coracoid P1",
            "y": "Acromion P2",
            "x": "Mindkettő P3"
        },        
        "14B2": {
            "l": "Lateralis határon át lép ki a törés",
            "m": "Medialis határon át lép ki a törés",
            "s": "Superior határon át lép ki a törés",
            "g": "A lateralis basisát érinti a coracoideusnak (glenoid site exit)",
            "x": "Coracoid P1",
            "y": "Acromion P2",
            "x": "Mindkettő P3"
        },  
        "14F1": {
            ".1": "Anterior perem",
            ".2": "Posterior perem",
            ".3": "Haránt vagy rövid ferde"       
        },
        "14F2": {
            ".1": "Fossa glenoidale",
            ".2": "Centralis dislocált fractura",
        },
         "15.3A": {
            "a": "Ép, chostocondralis ligamentalis complexum",
            "b": "Partialisan károdosott, chostocondralis ligamentalis complexum",
            "c": "Komplett disruptio, chostocondralis ligamentalis complexum"       
        },       
        "2U1B1": {
            "d": "Egyszeres",
            "e": "Többszörös"
        },
        "2U1B2": {
            "n": "Involving sublime facet",
            "o": "Csúcs (avulsio)",
            "p": "<50%",
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
            "j": "Tisztán diaphysealis",
            "k": "Distalis diaphysealis-metaphysealis"
        },
        "2R2C3": {
            "i": "Proximalis diaphysealis-metaphysealis",
            "j": "Tisztán diaphysealis",
            "k": "Distalis diaphysealis-metaphysealis"
        },
        "2U2C2": {
            "i": "Proximalis diaphysealis-metaphysealis",
            "j": "Tisztán diaphysealis",
            "k": "Distalis diaphysealis-metaphysealis"
        },
        "2U2C3": {
            "i": "Proximalis diaphysealis-metaphysealis",
            "j": "Tisztán diaphysealis",
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
            ".2": "Frontalis/coronalis",
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
            ".1": "Izolált egyszerű trochanter",
            ".2": "Két-darab",
            ".3": "Lateralis fal ép (>20.5 mm)"
        },
        "31A2": {
            ".2": "Egy középső fragmentum",
            ".3": "Kettő vagy több középső fragmentum"
        },
        "31A3": {
            ".1": "Egyszerű ferde",
            ".2": "Egyszerű haránt",
            ".3": "Ék vagy darabos"
        },
        "31B1": {
            ".1": "Valgus impaktált",
            ".2": "Elmozdulás nélküli",
            ".3": "Elmozdult"
        },
        "31B2": {
            ".1": "Egyszeres",
            ".2": "Többszörös",
            ".3": "Nyíró (shear)"
        },
        "31C1": {
            ".1": "Lig. teres avulsio",
            ".2": "Repedt, infrafovealis",
            ".3": "Repedt, suprafovealis"
        },
        "31C2": {
            ".1": "Chondralis laesio",
            ".2": "Benyomódott, impaktált",
            ".3": "Repedt, benyomódott"
        },
        "32A1": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "32A2": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "32A3": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "32B2": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "32B3": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "32C2": {
            "i": "Proximalis diaphysealis-metaphysealis",
            "j": "Tisztán diaphysealis",
            "k": "Distalis diaphysealis-metaphysealis"
        },
        "32C3": {
            "i": "Proximalis diaphysealis-metaphysealis",
            "j": "Tisztán diaphysealis",
            "k": "Distalis diaphysealis-metaphysealis"
        },
        "33A1": {
            ".1": "Lateralis epicondylus",
            ".2": "Medialis epicondylus"
        },
        "33A2": {
            ".1": "Spirál",
            ".2": "Ferde (≥ 30°)",
            ".3": "Haránt (< 30°)"
        }, 
        "33A3": {
            ".1": "Ép ék",
            ".2": "Darabos ék",
            ".3": "Többszörös"
        },
        "33B1": {
            ".1": "Egyszeres, a bevágáson (notch) keresztül",
            ".2": "Egyszeres, teherviselő felszín",
            ".3": "Darabos"
        },
        "33B2": {
            ".1": "Egyszeres, a bevágáson (notch) keresztül",
            ".2": "Egyszeres, teherviselő felszín",
            ".3": "Darabos"
        },
        "33B3": {
            ".1": "Anterior és lateralis darabka (flake)",
            ".2": "Posterior, unicondylaris (Hoffa)",
            ".3": "Posterior, bicondylaris (bilateralis Hoffa)"
        },
        "33C1": {
            ".1": "A transcondylaris tengely felett",
            ".3": "A transcondylaris tengelyen át vagy alatt"
        },
        "33C2": {
            ".1": "Ép ék, metaphysealis",
            ".2": "Darabos ék, metaphysealis",
            ".3": "Többszörös, metaphysealis"
        },
        "33C3": {
            ".1": "Egyszerű metaphysealis",
            ".2": "Ék, metaphysealis",
            ".3": "Többszörös, metaphysealis"
        },
        "34A1": {
            "a": "Proximalis pólus",
            "b": "Distalis pólus",
            "c": "Lateralis oldal",
            "d": "Medialis oldal"
        },
        "34B1": {
            ".1": "Egyszeres",
            ".2": "Darabos"
        },
        "34B2": {
            ".1": "Egyszeres",
            ".2": "Darabos"
        },
        "34C1": {
            ".1": "Középső 1/3",
            ".2": "Proximalis 1/3",
            ".3": "Distalis 1/3"
        },
        "41A1": {
            ".1": "A tok függelékei",
            ".2": "Tuberculum tibiae",
            ".3": "Tibia gerinc (spine - lig. cruciatum kapcsolódás)"
        },
        "41A2": {
            ".1": "Spirál",
            ".2": "Ferde (≥ 30°)",
            ".3": "Haránt (< 30°)"
        },
        "41A3": {
            ".1": "Ép ék",
            ".2": "Darabos ék",
            ".3": "Többszörös"
        },
        "41B1": {
            ".1": "Lateralis plateu",
            ".2": "Medialis plateu",
            ".3": "Ferde, érinti a tibia gerincét (spine) és egy plateut"
        },
        "41B2": {
            ".1": "Lateralis plateu",
            ".2": "Medialis plateu"
        },
        "41B3": {
            ".1": "Lateralis plateu",
            ".2": "Medialis plateu",
            ".3": "Ferde, érinti a tibia gerincét (spine) és egy plateut"
        },
        "41C1": {
            ".1": "Intercondylaris eminentia érintettség nélkül",
            ".2": "Intercondylaris eminentia érintettséggel",
        },
        "41C2": {
            ".1": "Ép ék",
            ".2": "Darabos ék",
            ".3": "Többszörös metaphysealis"
        },  
        "41C3": {
            ".1": "Darabos lateralis plateu",
            ".2": "Darabos medialis plateu",
            ".3": "Többszörös lateralis és medialis plateu"
        }, 
        "42A1": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "42A2": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "42A3": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "42B2": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "42B3": {
            "a": "Proximalis 1/3",
            "b": "Középső 1/3",
            "c": "Distalis 1/3"
        },
        "42C3": {
            "i": "Proximalis diaphysealis-metaphysealis",
            "j": "Tisztán diaphysealis",
            "k": "Distalis diaphysealis-metaphysealis"
        },
        "43A1": {
            ".1": "Spirál",
            ".2": "Ferde (≥ 30°)",
            ".3": "Haránt (< 30°)"
        },
        "43A2": {
            ".1": "Posterolateralis impaktált",
            ".2": "Anteromedialis ék",
            ".3": "Diaphysist is érintő"
        },
        "43A2": {
            ".1": "Három középső darab",
            ".2": "Több mint három középső darab",
            ".3": "Diaphysist is érintő"
        },
        "43B1": {
            ".1": "Frontalis/coronalis",
            ".2": "Sagittalis",
            ".3": "Darabos metaphysealis"
        },
        "43B2": {
            ".1": "Frontalis/coronalis",
            ".2": "Sagittalis",
            ".3": "Centrális fragmentum"
        },
        "43B3": {
            ".1": "Frontalis/coronalis",
            ".2": "Sagittalis",
            ".3": "Darabos metaphysealis"
        },
        "43C1": {
            ".1": "Impaktációmentes",
            ".2": "Epiphysealis benyomódás",
            ".3": "Diaphysist is érintő"
        },
        "43C2": {
            ".1": "Asszimetrikus impaktáció",
            ".2": "Asszimetrikus impaktációmentes",
            ".3": "Diaphysist is érintő"
        },
        "43C3": {
            ".1": "Epiphysealis",
            ".2": "Epiphysealis-metaphysealis",
            ".3": "Epiphysealis-metaphysealis-diaphysisealis"
        },
        "44A1": {
            ".1": "Lig. collaterale laterale ruptúra",
            ".2": "Lateralis malleolus csúcs avulsiós törés",
            ".3": "Lateralis malleolus haránt törés"
        },
        "44A2": {
            ".1": "Lig. collaterale laterale ruptúra",
            ".2": "Lateralis malleolus csúcs avulsiós törés",
            ".3": "Lateralis malleolus haránt törés"
        },
        "44A3": {
            ".1": "Lig. collaterale laterale ruptúra és posteromedialis törés",
            ".2": "Lateralis malleolus csúcs avulsiós és posteromedialis törés",
            ".3": "Lateralis malleolus haránt és posteromedialis törés"
        },
        "44B1": {
            ".1": "Egyszeres fibula",
            ".2": "Anterior syndesmosis ruptúra",
            ".3": "Ék vagy többszörös fibula"
        },
        "44B2": {
            ".1": "Anterior syndesmosis és lig. deltoideum ruptúra",
            ".2": "Medialis malleolus törés s anterior syndesmosis ruptúra",
            ".3": "Ék vagy többszörös fibula törés medialis sérüléssel"
        },
        "44B3": {
            ".1": "Egyszerű, lig. deltoideum ruptúra",
            ".2": "Medialis malleolus töréssel",
            ".3": "Ék vagy többszörös fibula törés, medialis malleolus töréssel"
        },
        "44C1": {
            ".1": "Egyszerű, lig. deltoideum ruptúra",
            ".2": "Medialis malleolus töréssel",
            ".3": "Medialis s posterior malleolus törésekkel"
        },
        "44C2": {
            ".1": "Egyszerű, lig. deltoideum ruptúra",
            ".2": "Medialis malleolus töréssel",
            ".3": "Medialis s posterior malleolus törésekkel"
        },
        "44C3": {
            ".1": "Medialis oldal sérüléssel",
            ".2": "Rövidülés s medialis oldal sérüléssel",
            ".3": "Medialis oldal sérüléssel s posterior malleolus törésekkel"
        },
        "61A1": {
            ".1": "Anterior superior spina iliaca",
            ".2": "Anterior inferior spina iliaca",
            ".3": "Tuber ischiadicum"
        },
        "61A2": {
            ".1": "Ala ossis ili",
            ".2": "Unilateralis anterior ív fractura",
            ".3": "Bilateralis anterior ív fractura"
        },
        "61B1": {
            ".1": "Lateralis kompressziós (LC1)",
            ".2": "Open book (APC1)",
        },
        "61B2": {
            ".1": "Lateralis kompressziós sacrum fractura (LC1), berotációs instabilitással (LC1)",
            ".2": "Lateralis kompressziós ilium (crescent) fractura (LC2), berotációs instabilitással (LC1)",
            ".3": "Open book vagy kirotációs instabilitás (APC2)"
        },
        "61B3": {
            ".1": "Unilateralis berotációs instabilitás, contralateralis kirotációs instabilitással (LC3)",
            ".2": "Bilateralis kompressziós sacrum fractura",
            ".3": "Open book vagy kirotációs instabilitás (bilateralis APC2)"
        },
        "61C1": {
            ".1": "Ilium fracturával",
            ".2": "Sacroiliacalis ízületen át",
            ".3": "Sacrum fracturával"
        },
        "61C2": {
            ".1": "Teljes disruptio az iliumon át",
            ".2": "Teljes disruptio a sacroiliacalis ízületen át",
            ".3": "Sacrumon át"
        },
        "61C3": {
            ".1": "Extrasacralis bilateralisan berotációs",
            ".2": "Sacralis unilateralisan, extrasacralis contralateralisan",
            ".3": "Sacralis bilateralisan"
        },
        "62A1": {
            ".1": "Egyszeres",
            ".2": "Többszörös"
        },
        "62A2": {
            ".1": "Ischiumon át",
            ".2": "Obturator gyűrűn át",
            ".3": "Posterior fal sérüléssel"
        },
        "62A3": {
            ".1": "Anterior fal",
            ".2": "Felső anterior oszlop (columna) (crista ilicán át)",
            ".3": "Alsó anterior oszlop (columna) (SIAS-on át)"
        },
        "62B1": {
            ".1": "Infratectalis",
            ".2": "Juxtatectalis",
            ".3": "Transtectalis"
        },
        "62B2": {
            ".1": "Infratectalis haránt komponensel",
            ".2": "Juxtatectalis haránt komponensel",
            ".3": "Transtectalis haránt komponensel"
        },
        "62B3": {
            ".1": "Anterior fallal asszociált",
            ".2": "Felső anterior oszlop (columna) (crista ilicán át)",
            ".3": "Alsó anterior oszlop (columna) (SIAS-on át)"
        },
        "62C1": {
            "d": "Mindkét oszlop (columna)",
            "e": "Többszörös, anterior oszlop (columna)",
            "f": "Többszörös, posterior oszlop (columna)",
            "g": "Többszörös, mindkét oszlop (columna)"
        },
        "62C2": {
            "d": "Mindkét oszlop (columna)",
            "e": "Többszörös, anterior oszlop (columna)",
            "f": "Többszörös, posterior oszlop (columna)",
            "g": "Többszörös, mindkét oszlop (columna)"
        },
        "62C3": {
            "d": "Mindkét oszlop (columna)",
            "e": "Többszörös, anterior oszlop (columna)",
            "f": "Többszörös, posterior oszlop (columna)",
            "g": "Többszörös, mindkét oszlop (columna)"
        },
        "81.2.B": {
            "a": "Egyszeres",
            "b": "Többszörös"
        },        
        "81.2.C": {
            "a": "Egyszeres",
            "b": "Többszörös"
        },  
        "81.2.D": {
            "a": "Egyszeres",
            "b": "Többszörös"
        },   
        "81.3.B": {
            "a": "Egyszeres",
            "b": "Többszörös"
        },  
        "81.3.C": {
            "a": "Egyszeres",
            "b": "Többszörös"
        },   
        "87.X.1A": {
            "a": "Egyszeres",
            "b": "Többszörös"
        },
        "87.X.1B": {
            "a": "Egyszeres",
            "b": "Többszörös"
        },
        "87.X.1C": {
            "a": "Egyszeres",
            "b": "Többszörös"
        },
        "87.X.3A": {
            "a": "Egyszeres",
            "b": "Többszörös"
        },
        "87.X.3B": {
            "a": "Egyszeres",
            "b": "Többszörös"
        },
        "87.X.3C": {
            "a": "Egyszeres",
            "b": "Többszörös"
        },

        "87.X.3": {
            "A": "Extraarticularis",
            "B": "Részleges ízületi",
            "C": "Teljes ízületi"
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
            "l": "Darabos",
            "u": "Ép ék"
        },
        "14F1.1": {
            "f": "Infraequatorialis perem az alsó kvadránsban",
            "r": "A max. glenoidalis meridiántól anterior vagy posterior peremtörés, amely superior vagy inferior lép ki a középvonaltól",
            "t": "Törés 2 infraequatorialis anterior vagy posterior kvadránsban, melynek oldalait a törés középvonal határozza meg",
            "x": "Coracoid P1",
            "y": "Acromion P2",
            "x": "Mindkettő P3"
        },        
        "14F1.2": {
            "f": "Infraequatorialis perem az alsó kvadránsban",
            "r": "A max. glenoidalis meridiántól anterior vagy posterior peremtörés, amely superior vagy inferior lép ki a középvonaltól",
            "t": "Törés 2 infraequatorialis anterior vagy posterior kvadránsban, melynek oldalait a törés középvonal határozza meg",
            "x": "Coracoid P1",
            "y": "Acromion P2",
            "x": "Mindkettő P3"
        },   
        "14F1.3": {
            "i": "Infraequatorialis ",
            "e": "Középvonali",
            "p": "Supraequatorialis",
            "x": "Coracoid P1",
            "y": "Acromion P2",
            "x": "Mindkettő P3"
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
            "n": "Trochanter major",
            "o": "Trochanter minor",
        },
        "31B2.1": {
            "p": "Pauwels 1 (<30°)",
            "q": "Pauwels 2 (30–70°)",
            "r": "Pauwels 3 (>70°)"
        },
        "33B3.2": {
            "f": "Lateralis condylus",
            "h": "Medialis condylus"
        },
        "33C2.1": {
            "f": "Lateralis condylus",
            "h": "Medialis condylus"
        },
        "33C2.2": {
            "f": "Lateralis condylus",
            "h": "Medialis condylus"
        },
        "33C3.2": {
            "f": "Lateralis condylus",
            "h": "Medialis condylus",
            "s": "Ép ék",
            "l": "Darabos ék"
        },
        "41A1.1": {
            "n": "Lateralis (Segond)",
            "h": "Medialis"
        },
        "41A1.3": {
            "o": "Anterior",
            "p": "Posterior"
        },
        "41A3.1": {
            "f": "Lateralis",
            "h": "Medialis"
        },
        "41A3.2": {
            "f": "Lateralis",
            "h": "Medialis"
        },
        "41B1.3": {
            "f": "Lateralis",
            "h": "Medialis"
        },
        "41B2.1": {
            "t": "Anterolateralis (AL)",
            "u": "Posterolateralis (PL)",
            "x": "Centralis"          
        },
        "41B2.2": {
            "v": "Anteromedialis (AM)",
            "w": "Posteromedialis (PM)",
            "x": "Centralis"          
        },
        "41B3.1": {
            "t": "Anterolateralis (AL)",
            "u": "Posterolateralis (PL)",
            "x": "Centralis"          
        },
        "41B3.2": {
            "v": "Anteromedialis (AM)",
            "w": "Posteromedialis (PM)",
            "x": "Centralis"          
        },
        "41B3.3": {
            "f": "Lateralis",
            "h": "Medialis"
        },
        "41C2.1": {
            "f": "Lateralis",
            "h": "Medialis"
        },
        "41C2.2": {
            "f": "Lateralis",
            "h": "Medialis"
        },
        "41C3.1": {
            "d": "Egyszerű metaphysealis",
            "u": "Többszörös metaphysealis",
            "v": "Meta-diaphysealis kiterjedés",            
            "t": "Anterolateralis (AL)",
            "u": "Posterolateralis (PL)",
            "v": "Anteromedialis (AM)",
            "w": "Posteromedialis (PM)",
            "x": "Centralis"  
        },
        "41C3.2": {
            "d": "Egyszerű metaphysealis",
            "u": "Többszörös metaphysealis",
            "v": "Meta-diaphysealis kiterjedés",            
            "t": "Anterolateralis (AL)",
            "u": "Posterolateralis (PL)",
            "v": "Anteromedialis (AM)",
            "w": "Posteromedialis (PM)",
            "x": "Centralis"  
        },
        "41C3.3": {
            "d": "Egyszerű metaphysealis",
            "u": "Többszörös metaphysealis",
            "v": "Meta-diaphysealis kiterjedés",            
            "t": "Anterolateralis (AL)",
            "u": "Posterolateralis (PL)",
            "v": "Anteromedialis (AM)",
            "w": "Posteromedialis (PM)",
            "x": "Centralis"  
        },
        "43B1.1": {
            "o": "Anterior",
            "y": "Posterior Volkmann"
        },
        "43B1.2": {
            "f": "Lateralis",
            "z": "Medialis ízületi felszín, medialis malleolust érintve"
        },
        "43B2.1": {
            "o": "Anterior",
            "y": "Posterior Volkmann"
        },
        "43B2.2": {
            "f": "Lateralis",
            "h": "Medialis"
        },
        "43B3.1": {
            "o": "Anterior",
            "y": "Posterior Volkmann"
        },
        "43B3.2": {
            "f": "Lateralis",
            "h": "Medialis"
        },
        "43C1.1": {
            "q": "Frontalis/coronalis sík",
            "r": "Sagittalis sík"
        },
        "43C2.1": {
            "q": "Frontalis/coronalis sík",
            "r": "Sagittalis sík"
        },
        "44B1.1": {
            "n": "Tillaux-Chaput",
            "o": "Wagstaffe-Le Fort",
            "u": "Instabil syndesmosis",
        },
        "44B1.2": {
            "n": "Tillaux-Chaput",
            "o": "Wagstaffe-Le Fort",
            "u": "Instabil syndesmosis",
        },
        "44B1.3": {
            "n": "Tillaux-Chaput",
            "o": "Wagstaffe-Le Fort",
            "u": "Instabil syndesmosis",
        },
        "44B2.1": {
            "n": "Tillaux-Chaput",
            "o": "Wagstaffe-Le Fort",
            "u": "Instabil syndesmosis",
        },
        "44B2.2": {
            "n": "Tillaux-Chaput",
            "o": "Wagstaffe-Le Fort",
            "u": "Instabil syndesmosis",
        },
        "44B2.3": {
            "r": "Lig. deltoideum ruptúra",
            "s": "Medialis malleolus töréssel",
            "u": "Instabil syndesmosis"
        },
        "44B3.1": {
            "n": "Tillaux-Chaput",
            "o": "Wagstaffe-Le Fort",
            "u": "Instabil syndesmosis"
        },
        "44B3.2": {
            "n": "Tillaux-Chaput",
            "o": "Wagstaffe-Le Fort",
            "u": "Instabil syndesmosis"
        },
        "44B3.3": {
            "n": "Tillaux-Chaput",
            "o": "Wagstaffe-Le Fort",
            "u": "Instabil syndesmosis"
        },
        "44C1.1": {
            "t": "Stabil syndesmosis",
            "u": "Instabil syndesmosis"
        },
        "44C1.2": {
            "t": "Stabil syndesmosis",
            "u": "Instabil syndesmosis"
        },
        "44C1.3": {
            "t": "Stabil syndesmosis",
            "u": "Instabil syndesmosis"
        },
        "44C2.1": {
            "t": "Stabil syndesmosis",
            "u": "Instabil syndesmosis"
        },
        "44C2.2": {
            "t": "Stabil syndesmosis",
            "u": "Instabil syndesmosis"
        },
        "44C2.3": {
            "t": "Stabil syndesmosis",
            "u": "Instabil syndesmosis"
        },
        "44C3.1": {
            "p": "Fibula nyak törés",
            "q": "Proximalis tibio-fibularis dislocatio",
            "r": "Lig. deltoideum ruptúra",
            "s": "Medialis malleolus törés"
        },
        "44C3.2": {
            "p": "Fibula nyak törés",
            "q": "Proximalis tibio-fibularis dislocatio",
            "r": "Lig. deltoideum ruptúra",
            "s": "Medialis malleolus törés"
        },
        "44C3.3": {
            "p": "Fibula nyak törés",
            "q": "Proximalis tibio-fibularis dislocatio",
            "r": "Lig. deltoideum ruptúra",
            "s": "Medialis malleolus törés"
        },
        "61B1.1": {
            "a": "Ipsilateralis vagy unilateralis ramus pubicus",
            "b": "Bilateralis ramus pubicus",
            "c": "Contralateralis ramus pubicus",
            "e": "Parasymphysealis",
            "f": "Dőlt (Tilt)",
            "g": "Zárt (locked) symphysis"
        },     
        "61B2.1": {
            "a": "Ipsilateralis vagy unilateralis ramus pubicus",
            "b": "Bilateralis ramus pubicus",
            "c": "Contralateralis ramus pubicus",
            "d": "Symphysis disruptio",
            "e": "Parasymphysealis",
            "f": "Dőlt (Tilt)",
            "g": "Zárt (locked) symphysis"
        },
        "61B2.2": {
            "a": "Ipsilateralis vagy unilateralis ramus pubicus",
            "b": "Bilateralis ramus pubicus",
            "c": "Contralateralis ramus pubicus",
            "d": "Symphysis disruptio",
            "e": "Parasymphysealis",
            "f": "Dőlt (Tilt)",
            "g": "Zárt (locked) symphysis"
        }, 
        "61B2.3": {
            "a": "Ipsilateralis vagy unilateralis ramus pubicus",
            "b": "Bilateralis ramus pubicus",
            "c": "Contralateralis ramus pubicus",
            "d": "Symphysis disruptio",
            "e": "Parasymphysealis",
            "f": "Dőlt (Tilt)",
            "g": "Zárt (locked) symphysis"
        }, 
        "61B3.1": {
            "a": "Ipsilateralis vagy unilateralis ramus pubicus",
            "b": "Bilateralis ramus pubicus",
            "d": "Symphysis disruptio",
            "e": "Parasymphysealis",
            "f": "Dőlt (Tilt)",
            "g": "Zárt (locked) symphysis"
        },
        "61B3.2": {
            "a": "Ipsilateralis vagy unilateralis ramus pubicus",
            "b": "Bilateralis ramus pubicus",
            "d": "Symphysis disruptio",
            "e": "Parasymphysealis",
            "f": "Dőlt (Tilt)",
            "g": "Zárt (locked) symphysis"
        }, 
        "61B3.3": {
            "a": "Ipsilateralis vagy unilateralis ramus pubicus",
            "b": "Bilateralis ramus pubicus",
            "d": "Symphysis disruptio",
            "e": "Parasymphysealis",
            "f": "Dőlt (Tilt)",
            "g": "Zárt (locked) symphysis"
        }, 
        "61C1.1": {
            "a": "Ipsilateralis vagy unilateralis ramus pubicus",
            "b": "Bilateralis ramus pubicus",
            "c": "Contralateralis ramus pubicus",
            "d": "Symphysis disruptio",
            "e": "Parasymphysealis",
            "f": "Dőlt (Tilt)",
            "g": "Zárt (locked) symphysis",
            "j": "Sacroiliacalis ízület fractura s dislocatio"            
        },
        "61C1.2": {
            "a": "Ipsilateralis vagy unilateralis ramus pubicus",
            "b": "Bilateralis ramus pubicus",
            "c": "Contralateralis ramus pubicus",
            "d": "Symphysis disruptio",
            "e": "Parasymphysealis",
            "f": "Dőlt (Tilt)",
            "g": "Zárt (locked) symphysis",
            "j": "Sacroiliacalis ízület fractura s dislocatio"   
        }, 
        "61C1.3": {
            "a": "Ipsilateralis vagy unilateralis ramus pubicus",
            "b": "Bilateralis ramus pubicus",
            "c": "Contralateralis ramus pubicus",
            "d": "Symphysis disruptio",
            "e": "Parasymphysealis",
            "f": "Dőlt (Tilt)",
            "g": "Zárt (locked) symphysis",
            "j": "Sacroiliacalis ízület fractura s dislocatio"   
        }, 
        "61C2.1": {
            "a": "Ipsilateralis vagy unilateralis ramus pubicus",
            "b": "Bilateralis ramus pubicus",
            "c": "Contralateralis ramus pubicus",
            "d": "Symphysis disruptio",
            "e": "Parasymphysealis",
            "f": "Dőlt (Tilt)",
            "g": "Zárt (locked) symphysis",
            "k": "Sacrum contralateralis posterior lateralis compressios laesio",           
            "l": "Ilium (crescent) contralateralis posterior lateralis compressios laesio", 
            "k": "Sacroiliacalis, contralateralis posterior kirotációs laesio",           
            "l": "Dislocált fractura, contralateralis posterior kirotációs laesio"    
        },
        "61C2.2": {
            "a": "Ipsilateralis vagy unilateralis ramus pubicus",
            "b": "Bilateralis ramus pubicus",
            "c": "Contralateralis ramus pubicus",
            "d": "Symphysis disruptio",
            "e": "Parasymphysealis",
            "f": "Dőlt (Tilt)",
            "g": "Zárt (locked) symphysis",
            "k": "Sacrum contralateralis posterior lateralis compressios laesio",           
            "l": "Ilium (crescent) contralateralis posterior lateralis compressios laesio", 
            "k": "Sacroiliacalis, contralateralis posterior kirotációs laesio",           
            "l": "Dislocált fractura, contralateralis posterior kirotációs laesio"    
        },
        "61C2.3": {
            "a": "Ipsilateralis vagy unilateralis ramus pubicus",
            "b": "Bilateralis ramus pubicus",
            "c": "Contralateralis ramus pubicus",
            "d": "Symphysis disruptio",
            "e": "Parasymphysealis",
            "f": "Dőlt (Tilt)",
            "g": "Zárt (locked) symphysis",
            "k": "Sacrum contralateralis posterior lateralis compressios laesio",           
            "l": "Ilium (crescent) contralateralis posterior lateralis compressios laesio", 
            "k": "Sacroiliacalis, contralateralis posterior kirotációs laesio",           
            "l": "Dislocált fractura, contralateralis posterior kirotációs laesio"    
        }, 
        "61C3.1": {
            "a": "Ipsilateralis vagy unilateralis ramus pubicus",
            "b": "Bilateralis ramus pubicus",
            "c": "Contralateralis ramus pubicus",
            "d": "Symphysis disruptio",
            "e": "Parasymphysealis",
            "f": "Dőlt (Tilt)",
            "g": "Zárt (locked) symphysis",
            "h": "Ala ossis ili",            
            "j": "Sacroiliacalis ízület disruptio"             
        },
        "61C3.2": {
            "a": "Ipsilateralis vagy unilateralis ramus pubicus",
            "b": "Bilateralis ramus pubicus",
            "c": "Contralateralis ramus pubicus",
            "d": "Symphysis disruptio",
            "e": "Parasymphysealis",
            "f": "Dőlt (Tilt)",
            "g": "Zárt (locked) symphysis",
            "h": "Ala ossis ili",            
            "j": "Sacroiliacalis ízület disruptio"   
        }, 
        "61C3.3": {
            "a": "Ipsilateralis vagy unilateralis ramus pubicus",
            "b": "Bilateralis ramus pubicus",
            "c": "Contralateralis ramus pubicus",
            "d": "Symphysis disruptio",
            "e": "Parasymphysealis",
            "f": "Dőlt (Tilt)",
            "g": "Zárt (locked) symphysis",
            "h": "Ala ossis ili",            
            "j": "Sacroiliacalis ízület disruptio"   
        }, 
        "62A2.3": {
            "h": "Egyszeres, posterior fal",
            "i": "Többszörös, posterior fal",
            "j": "Posterior fal és marginalis impactatio"
        },
        "62A3.1": {
            "a": "Marginalis impactatio"
        },
        "62A3.2": {
            "a": "Marginalis impactatio"
        },
        "62A3.3": {
            "a": "Marginalis impactatio"
        },
        "62B1.1": {
            "b": "Posterior fal",
            "c": "Posterior fal és marginalis impactatio"
        },
        "62B1.2": {
            "b": "Posterior fal",
            "c": "Posterior fal és marginalis impactatio"
        },
        "62B1.3": {
            "b": "Posterior fal",
            "c": "Posterior fal és marginalis impactatio"
        },
        "62B2.1": {
            "b": "Posterior fal",
            "c": "Posterior fal és marginalis impactatio"
        },
        "62B2.2": {
            "b": "Posterior fal",
            "c": "Posterior fal és marginalis impactatio"
        },
        "62B2.3": {
            "b": "Posterior fal",
            "c": "Posterior fal és marginalis impactatio"
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
            "I": "Medialis epicondylus",
            "II": "Lateralis epicondylus",
            "III": "Capitellum",
            "IV": "Trochlea"
        },
        "Humerus diaphysis": {
            "I": "Spirál",
            "II": "Ferde",
            "III": "Haránt",
            "IV": "Komplex"
        },
        "Proximalis femur": {
            "I": "Subcapitalis",
            "II": "Transcervicalis",
            "III": "Basicervicalis",
            "IV": "Intertrochanterikus"
        },
        "Distalis femur": {
            "I": "Condylaris",
            "II": "Intercondylaris",
            "III": "Supracondylaris",
            "IV": "Komplex"
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
