import streamlit as st
import os
import uuid
import io
import zipfile
import firebase_admin
from firebase_admin import credentials, firestore, storage
from PIL import Image

# Initialize Firebase
def initialize_firebase():
    if not firebase_admin._apps:
        firebase_config = {
            "type": st.secrets["firebase"]["type"],
            "project_id": st.secrets["firebase"]["project_id"],
            "private_key_id": st.secrets["firebase"]["private_key_id"],
            "private_key": st.secrets["firebase"]["private_key"].replace('\\n', '\n'),
            "client_email": st.secrets["firebase"]["client_email"],
            "client_id": st.secrets["firebase"]["client_id"],
            "auth_uri": st.secrets["firebase"]["auth_uri"],
            "token_uri": st.secrets["firebase"]["token_uri"],
            "auth_provider_x509_cert_url": st.secrets["firebase"]["auth_provider_x509_cert_url"],
            "client_x509_cert_url": st.secrets["firebase"]["client_x509_cert_url"]
        }
        
        cred = credentials.Certificate(firebase_config)
        firebase_admin.initialize_app(cred, {
            'storageBucket': f"{firebase_config['project_id']}.appspot.com"
        })

initialize_firebase()
db = firestore.client()
bucket = storage.bucket()

# Upload file to Firebase Storage
def upload_to_storage(file_path, destination_blob_name):
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(file_path)
    blob.make_public()
    return blob.public_url

# Download file from Firebase Storage
def download_from_storage(source_blob_name, destination_file_name):
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

# Save image and metadata to Firestore and Firebase Storage
def save_image(patient_id, file, type, view, main_region, sub_region, age, comment):
    filename = file.name
    unique_filename = f"{uuid.uuid4()}_{filename}"
    file_path = os.path.join("/tmp", unique_filename)

    with open(file_path, "wb") as f:
        f.write(file.getbuffer())

    public_url = upload_to_storage(file_path, unique_filename)

    doc_ref = db.collection('images').document(unique_filename)
    doc_ref.set({
        'patient_id': patient_id,
        'filename': unique_filename,
        'type': type,
        'view': view,
        'main_region': main_region,
        'sub_region': sub_region,
        'age': age,
        'comment': comment,
        'url': public_url
    })

# Streamlit app
st.title("Kép feltöltése és címkézése")

# Create or select patient ID
patient_id = st.text_input("Beteg azonosító (hagyja üresen új beteg esetén)", str(uuid.uuid4()))

uploaded_file = st.file_uploader("Válassz egy képet", type=["jpg", "jpeg", "png"])

# Select image details
type = st.selectbox("Típus", ["Törött", "Normál", "Egyéb"])
if type == "Egyéb":
    type_comment = st.text_input("Specifikálás (Egyéb)")
else:
    type_comment = ""

view = st.selectbox("Nézet", ["AP", "Lateral", "Egyéb"])
if view == "Egyéb":
    view_comment = st.text_input("Specifikálás (Egyéb Nézet)")
else:
    view_comment = ""

main_region = st.selectbox("Fő régió", ["Felső végtag", "Alsó végtag", "Gerinc", "Koponya"])

if main_region == "Felső végtag":
    sub_region = st.selectbox("Alrégió", ["Clavicula", "Scapula", "Váll", "Felkar", "Könyök", "Radius", "Ulna", "Csukló", "Kéz"])
elif main_region == "Alsó végtag":
    sub_region = st.selectbox("Alrégió", ["Csípő", "Comb", "Térd", "Tibia", "Fibula", "Boka", "Láb"])
elif main_region == "Gerinc":
    sub_region = st.selectbox("Alrégió", ["Nyaki", "Háti", "Ágyéki", "Kereszt- és farokcsonti"])
elif main_region == "Koponya":
    sub_region = st.selectbox("Alrégió", ["Arckoponya", "Agykoponya", "Állkapocs"])
else:
    sub_region = ""

age = st.slider("Életkor", min_value=0, max_value=120, step=1, format="%d", value=0)
comment = st.text_area("Megjegyzés", key="comment", value="")

if st.button("Feltöltés"):
    if uploaded_file and type and view and main_region and sub_region:
        try:
            full_comment = comment + " " + type_comment + " " + view_comment
            save_image(patient_id, uploaded_file, type, view, main_region, sub_region, age, full_comment)
            st.success("Kép sikeresen feltöltve!")
        except Exception as e:
            st.error(f"Hiba a kép mentésekor: {e}")
    else:
        st.error("Tölts fel egy képet és add meg a szükséges információkat.")

# Search and display images
st.header("Képek keresése")
search_labels = st.text_input("Keresés címkék alapján (vesszővel elválasztva)")

search_type = st.selectbox("Típus keresése", ["", "Törött", "Normál"])
search_view = st.selectbox("Nézet keresése", ["", "AP", "Lateral"])
search_main_region = st.selectbox("Fő régió keresése", ["", "Felső végtag", "Alsó végtag", "Gerinc", "Koponya"])

if search_main_region == "Felső végtag":
    search_sub_region = st.selectbox("Alrégió keresése", ["", "Clavicula", "Scapula", "Váll", "Felkar", "Könyök", "Radius", "Ulna", "Csukló", "Kéz"])
elif search_main_region == "Alsó végtag":
    search_sub_region = st.selectbox("Alrégió keresése", ["", "Csípő", "Comb", "Térd", "Tibia", "Fibula", "Boka", "Láb"])
elif search_main_region == "Gerinc":
    search_sub_region = st.selectbox("Alrégió keresése", ["", "Nyaki", "Háti", "Ágyéki", "Kereszt- és farokcsonti"])
elif search_main_region == "Koponya":
    search_sub_region = st.selectbox("Alrégió keresése", ["", "Arckoponya", "Agykoponya", "Állkapocs"])
else:
    search_sub_region = ""

if st.button("Keresés"):
    results = db.collection('images')

    if search_labels:
        for label in search_labels.split(","):
            results = results.where('type', '==', label.strip())

    if search_type:
        results = results.where('type', '==', search_type)
    if search_view:
        results = results.where('view', '==', search_view)
    if search_main_region:
        results = results.where('main_region', '==', search_main_region)
    if search_sub_region:
        results = results.where('sub_region', '==', search_sub_region)

    docs = results.stream()
    file_paths = []

    for doc in docs:
        data = doc.to_dict()
        st.image(data['url'], caption=f"{data['type']}, {data['view']}, {data['main_region']}, {data['sub_region']}")
        file_paths.append(data['url'])

    if file_paths:
        zip_buffer = create_zip(file_paths)
        st.download_button(
            label="Képek letöltése ZIP-ben",
            data=zip_buffer,
            file_name="images.zip",
            mime="application/zip"
        )

# Create ZIP of selected files
def create_zip(files):
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for file_path in files:
            arcname = os.path.basename(file_path)
            zip_file.write(file_path, arcname)
    zip_buffer.seek(0)
    return zip_buffer
