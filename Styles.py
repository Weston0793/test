import streamlit as st

def home_background():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
        
        .stApp {
            background: linear-gradient(to bottom right, #f0f4f7, #d9e2ec);
            background-attachment: fixed;
            color: #212121;
            font-family: 'Roboto', sans-serif;
        }
        .title {
            font-size: 48px;
            font-weight: 700;
            color: #ffffff;
            text-align: center;
            padding: 20px;
            background: rgba(0, 150, 136, 0.8);
            border-radius: 10px;
            margin-top: 20px;
            text-shadow: 2px 2px 4px #000000;
            animation: fadeInDown 1.5s;
        }
        .subheader {
            font-size: 28px;
            color: #ffffff;
            background: #00796B;
            padding: 10px;
            border-radius: 10px;
            margin-top: 30px;
            margin-bottom: 10px;
        }
        .subsubheader {
            font-size: 22px;
            color: #ffffff;
            background: #004D40;
            padding: 8px;
            border-radius: 8px;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .content {
            font-size: 16px;
            line-height: 1.2;
            text-align: justify;
            margin: 20px;
            padding: 20px;
            background: #ffffff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .content ul {
            margin-left: 20px;
        }
        .content li {
            margin-bottom: 10px;
        }
        .content p {
            margin-bottom: 10px;
        }
        .content a {
            color: #00796B;
            text-decoration: none;
        }
        .content a:hover {
            text-decoration: underline;
        }
        @keyframes fadeInDown {
            0% {
                opacity: 0;
                transform: translateY(-20px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }
        @keyframes fadeIn {
            0% {
                opacity: 0;
            }
            100% {
                opacity: 1;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def search_markdown():
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
        .formatted-data {
            font-family: Arial, sans-serif;
            line-height: 1.5;
            color: #333;
        }
        .formatted-data h4 {
            margin-top: 10px;
            margin-bottom: 5px;
            color: #444;
        }
        .formatted-data p {
            margin: 0;
            padding: 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
def upload_markdown():
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
def upload_markdown():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

        .stApp {
            background: linear-gradient(to bottom right, #e0f7fa, #c8e6c9);
            background-attachment: fixed;
            color: #333333;
            font-family: 'Roboto', sans-serif;
        }
        .upload-title {
            font-size: 36px;
            font-weight: 700;
            color: #ffffff;
            text-align: center;
            padding: 15px;
            background: rgba(0, 150, 136, 0.8);
            border-radius: 8px;
            margin-top: 20px;
            text-shadow: 1px 1px 3px #000000;
            animation: fadeInDown 1.5s;
        }
        .file-upload-instruction {
            font-size: 16px;
            color: #ffffff;
            background: #4caf50;
            padding: 10px;
            border-radius: 8px;
            margin-top: 20px;
            margin-bottom: 10px;
            text-align: center;
        }
        .content {
            font-size: 14px;
            line-height: 1.2;
            text-align: justify;
            margin: 10px;
            padding: 10px;
            background: #ffffff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .content ul {
            margin-left: 20px;
        }
        .content li {
            margin-bottom: 10px;
        }
        .content p {
            margin-bottom: 10px;
        }
        .content a {
            color: #00796B;
            text-decoration: none;
        }
        .content a:hover {
            text-decoration: underline;
        }
        @keyframes fadeInDown {
            0% {
                opacity: 0;
                transform: translateY(-20px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }
        @keyframes fadeIn {
            0% {
                opacity: 0;
            }
            100% {
                opacity: 1;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def status_markdown():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

        .stApp {
            background: linear-gradient(to bottom right, #e0f7fa, #ffccbc);
            background-attachment: fixed;
            color: #333333;
            font-family: 'Roboto', sans-serif;
        }
        .tracker-title {
            font-size: 48px;
            font-weight: 700;
            color: #ffffff;
            text-align: center;
            padding: 20px;
            background: rgba(0, 150, 136, 0.8);
            border-radius: 10px;
            margin-top: 20px;
            text-shadow: 2px 2px 4px #000000;
            animation: fadeInDown 1.5s;
        }
        .update-note {
            font-size: 20px;
            color: #ffffff;
            background: #ff7043;
            padding: 10px;
            border-radius: 10px;
            margin-top: 30px;
            margin-bottom: 10px;
        }
        .grand-total {
            font-size: 26px;
            color: #ffffff;
            background: #00897b;
            padding: 10px;
            border-radius: 10px;
            margin-top: 20px;
            margin-bottom: 20px;
            text-align: center;
        }
        .subheader {
            font-size: 24px;
            color: #ffffff;
            background: #00796B;
            padding: 10px;
            border-radius: 10px;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .subsubheader {
            font-size: 20px;
            color: #ffffff;
            background: #004D40;
            padding: 8px;
            border-radius: 8px;
            margin-top: 10px;
            margin-bottom: 5px;
        }
        .content {
            font-size: 14px;
            line-height: 1.2;
            text-align: justify;
            margin: 10px;
            padding: 10px;
            background: #ffffff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .content ul {
            margin-left: 20px;
        }
        .content li {
            margin-bottom: 10px;
        }
        .content p {
            margin-bottom: 10px;
        }
        .content a {
            color: #00796B;
            text-decoration: none;
        }
        .content a:hover {
            text-decoration: underline;
        }
        .hover-effect:hover {
            color: #007BFF;
            transform: scale(1.05);
        }
        @keyframes fadeInDown {
            0% {
                opacity: 0;
                transform: translateY(-20px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }
        @keyframes fadeIn {
            0% {
                opacity: 0;
            }
            100% {
                opacity: 1;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
