import streamlit as st
from streamlit.components.v1 import html

class MultiPage:
    def __init__(self):
        self.pages = []

    def add_page(self, title, func):
        self.pages.append({
            "title": title,
            "function": func,
            "slug": title.lower().replace(" ", "_")
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

            .topnav button {
                display: block;
                color: #f2f2f2;
                background-color: transparent;
                border: none;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
                font-size: 17px;
                margin-right: 10px;
                cursor: pointer;
            }

            .topnav button:hover {
                background-color: #ddd;
                color: black;
            }

            .topnav button.active {
                background-color: #04AA6D;
                color: white;
            }
            </style>
            """, unsafe_allow_html=True
        )

        # Create the navigation bar
        nav_links = ''.join([f'<button onclick="setPage(\'{page["slug"]}\')">{page["title"]}</button>' for page in self.pages])
        st.markdown(
            f"""
            <div class="topnav">
              <div class="nav-title">Navigáció</div>
              {nav_links}
            </div>
            """, unsafe_allow_html=True
        )

        # Render the selected page
        query_params = st.experimental_get_query_params()
        if 'page' in query_params:
            selected_page = query_params['page'][0]
            for page in self.pages:
                if page["slug"] == selected_page:
                    page["function"]()

        # Add JavaScript to handle button clicks and navigate to the correct page
        st.markdown(
            """
            <script>
            function setPage(page) {
                const url = new URL(window.location);
                url.searchParams.set('page', page);
                window.location.href = url.href;
            }
            </script>
            """, unsafe_allow_html=True
        )

# Function to navigate to a different page
def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("button");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].textContent === page_name) {
                        links[i].click();
                        return;
                    }
                }
                var elapsed = new Date() - start_time;
                if (elapsed < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)
