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
            'Navigation',
            self.pages,
            format_func=lambda page: page['title']
        )
        st.title(selected_page['title'])
        st.sidebar.markdown(f"# {selected_page['icon']} {selected_page['title']}")
        selected_page['function']()
