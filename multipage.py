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
            }

            .topnav a {
                float: left;
                display: block;
                color: #f2f2f2;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
                font-size: 17px;
            }

            .topnav a:hover {
                background-color: #ddd;
                color: black;
            }

            .topnav a.active {
                background-color: #04AA6D;
                color: white;
            }

            .topnav #nav-title {
                background-color: #04AA6D;
                color: white;
                font-weight: bold;
            }
            </style>
            """, unsafe_allow_html=True
        )

        # Create the navigation bar
        st.markdown(
            """
            <div class="topnav">
              <a id="nav-title">Navigáció</a>
              <div id="nav-links">
                {}
              </div>
            </div>
            """.format(''.join([f'<a href="#" id="page-{i}">{page["title"]}</a>' for i, page in enumerate(self.pages)])), unsafe_allow_html=True
        )

        # Render the selected page
        if 'active_page' not in st.session_state:
            st.session_state['active_page'] = 'page-0'
        
        for i, page in enumerate(self.pages):
            if st.session_state['active_page'] == f'page-{i}':
                page['function']()

        # Add JavaScript to handle button active state and communicate with Streamlit backend
        st.markdown(
            """
            <script>
            const links = document.querySelectorAll('.topnav a:not(#nav-title)');
            links.forEach(link => {
                link.addEventListener('click', function(event) {
                    event.preventDefault();
                    links.forEach(l => l.classList.remove('active'));
                    this.classList.add('active');
                    const pageId = this.id;
                    window.parent.postMessage({isStreamlitNavigation: true, pageId: pageId}, "*");
                });
            });
            window.addEventListener("message", (event) => {
                if (event.data.isStreamlitNavigation) {
                    const pageId = event.data.pageId;
                    links.forEach(l => l.classList.remove('active'));
                    document.getElementById(pageId).classList.add('active');
                    Streamlit.setComponentValue(pageId);
                }
            });
            </script>
            """, unsafe_allow_html=True
        )
