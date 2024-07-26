import streamlit as st
# CSS stílus a navigációs sávhoz
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
            padding: 20px;
            border: 2px solid #000;
            border-radius: 10px;
        }
        .sidebar .sidebar-content .selectbox {
            font-size: 18px;
        }
        .sidebar .sidebar-content .stSelectbox {
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

class MultiPage:
    def __init__(self):
        self.pages = []

    def add_page(self, title, func, icon=None):
        self.pages.append({
            "title": title,
            "function": func,
            "icon": icon
        })

    def run(self):
        selected_page = st.sidebar.selectbox(
            'Navigáció',
            self.pages,
            format_func=lambda page: f"{page['icon']} {page['title']}" if page['icon'] else page['title']
        )
        selected_page['function']()
