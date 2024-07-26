import streamlit as st


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
