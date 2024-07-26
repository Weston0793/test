import streamlit as st

class MultiPage:
    def __init__(self):
        self.pages = []

    def add_page(self, title, func):
        self.pages.append({
            "title": title,
            "function": func
        })

    def run(self):
        # Custom CSS to style the navigation bar
        st.markdown(
            """
            <style>
            .topnav {
                overflow: hidden;
                background-color: #333;
                position: -webkit-sticky; /* Safari */
                position: sticky;
                top: 0;
                width: 100%;
                z-index: 1000;
                padding: 10px;
                display: flex;
                align-items: center;
            }

            .topnav .nav-title {
                background-color: #04AA6D;
                color: white;
                font-weight: bold;
                padding: 14px 16px;
                margin-right: 20px;
                pointer-events: none;
            }

            .topnav a {
                display: block;
                color: #f2f2f2;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
                font-size: 17px;
                margin-right: 10px;
                cursor: pointer;
            }

            .topnav a:hover {
                background-color: #ddd;
                color: black;
            }

            .topnav a.active {
                background-color: #04AA6D;
                color: white;
            }
            </style>
            """, unsafe_allow_html=True
        )

        # Create the navigation bar
        nav_links = ''.join([f'<a id="page-{i}" onclick="setPage(\'page-{i}\')">{page["title"]}</a>' for i, page in enumerate(self.pages)])
        st.markdown(
            f"""
            <div class="topnav">
              <div class="nav-title">Navigáció</div>
              {nav_links}
            </div>
            """, unsafe_allow_html=True
        )

        # Set the active page
        if 'active_page' not in st.session_state:
            st.session_state['active_page'] = 'page-0'

        # Render the selected page
        for i, page in enumerate(self.pages):
            if st.session_state['active_page'] == f'page-{i}':
                page['function']()

        # Add JavaScript to handle button active state and communicate with Streamlit backend
        st.markdown(
            """
            <script>
            function setPage(pageId) {
                const links = document.querySelectorAll('.topnav a');
                links.forEach(link => {
                    link.classList.remove('active');
                    if (link.id === pageId) {
                        link.classList.add('active');
                    }
                });
                const url = new URL(window.location);
                url.searchParams.set('page', pageId);
                window.location.href = url.href;
            }

            window.addEventListener("message", (event) => {
                if (event.data.isStreamlitNavigation) {
                    const pageId = event.data.pageId;
                    const links = document.querySelectorAll('.topnav a');
                    links.forEach(link => {
                        link.classList.remove('active');
                        if (link.id === pageId) {
                            link.classList.add('active');
                        }
                    });
                    Streamlit.setComponentValue(pageId);
                }
            });
            </script>
            """, unsafe_allow_html=True
        )

        # Handle the page change event from JavaScript
        query_params = st.experimental_get_query_params()
        if 'page' in query_params:
            js_page_id = query_params['page'][0]
            if st.session_state['active_page'] != js_page_id:
                st.session_state['active_page'] = js_page_id
                st.experimental_rerun()

# Save this as multipage.py
