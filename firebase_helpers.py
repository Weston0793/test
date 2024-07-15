import os
import uuid
import io
import zipfile
import firebase_admin
from firebase_admin import credentials, firestore, storage
import streamlit as st

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

# Create ZIP of selected files
def create_zip(files):
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for file_url in files:
            arcname = os.path.basename(file_url)
            zip_file.writestr(arcname, file_url)
    zip_buffer.seek(0)
    return zip_buffer
