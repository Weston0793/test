import streamlit as st
from firebase_helpers import initialize_firebase, save_comment, get_comments
import random
import datetime

# Ensure Firebase is initialized
initialize_firebase()
def set_background():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
        
        .stApp {
            background: linear-gradient(to bottom right, #e0eafc, #cfdef3);
            background-attachment: fixed;
            color: #333333;
            font-family: 'Roboto', sans-serif;
        }
        .title {
            font-size: 48px;
            font-weight: 700;
            color: #ffffff;
            text-align: center;
            padding: 20px;
            background: rgba(103, 58, 183, 0.8);
            border-radius: 10px;
            margin-top: 20px;
            text-shadow: 2px 2px 4px #000000;
            animation: fadeInDown 1.5s;
        }
        .subheader {
            font-size: 28px;
            color: #ffffff;
            background: #673AB7;
            padding: 10px;
            border-radius: 10px;
            margin-top: 30px;
            margin-bottom: 10px;
        }
        .subsubheader {
            font-size: 22px;
            color: #ffffff;
            background: #4527A0;
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
            color: #673AB7;
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

def generate_funny_name():
    first_parts = ["Fluffy", "Sparkly", "Wiggly", "Silly", "Funky", "Giggles", "Cheery", "Dizzy", "Bouncy", "Jumpy",
                   "Zippy", "Snazzy", "Bubbly", "Quirky", "Jolly", "Peppy", "Giddy", "Chirpy", "Frisky", "Perky",
                   "Whizzy", "Fizzy", "Nifty", "Ducky", "Zappy", "Chipper", "Jazzy", "Snappy", "Zany"]
    second_parts = ["Penguin", "Banana", "Unicorn", "Muffin", "Pickle", "Cupcake", "Bunny", "Monkey", "Noodle", "Puppy",
                    "Sprout", "Pancake", "Mango", "Gizmo", "Taco", "Bubble", "Pudding", "Doodle", "Coconut", "Waffle",
                    "Marshmallow", "Pepper", "Sundae", "Snickers", "Button", "Tinker", "Pebble", "Cookie", "Biscuit"]
    return f"{random.choice(first_parts)} {random.choice(second_parts)}"

def main():
    set_background()
    
    st.markdown('<h1 class="title">Elérhetőség</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="content">
        <h2 class="subheader">Kapcsolat</h2>
        <p><strong>Email:</strong> aba.lorincz@gmail.com</p>
        <p><strong>Telefon:</strong> +36 30 954 2176</p>
        <p><strong>Cím:</strong> Department of Thermophysiology, Institute for Translational Medicine, Medical School, University of Pécs, 12 Szigeti Street, 7624 Pécs, Hungary</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<h2 class="subheader">Kommentszekció</h2>', unsafe_allow_html=True)
    
    if 'name' not in st.session_state:
        st.session_state.name = generate_funny_name()

    col1, col2 = st.columns([4, 1])
    with col1:
        name = st.text_input("Név", value=st.session_state.name)
    with col2:
        if st.button("Új nevet kérek!"):
            with st.spinner('Generating a new name...'):
                st.session_state.name = generate_funny_name()
                name = st.session_state.name

    comment = st.text_area("Komment")

    if st.button("Küldés"):
        if comment:
            with st.spinner('Saving your comment...'):
                save_comment(name, comment)
            st.success("Köszönjük a hozzászólást!", icon="✅")
        else:
            st.error("A komment mező nem lehet üres!", icon="❌")

    st.markdown('<h3 class="subsubheader">Legutóbbi Kommentek</h3>', unsafe_allow_html=True)
    
    if 'page' not in st.session_state:
        st.session_state.page = 0

    page = st.session_state.page
    comments = get_comments(page * 2, 2)

    if comments:
        for c in comments:
            timestamp = c['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
            st.markdown(f"<div class='content'><strong>{c['name']}</strong>: {c['comment']} <em>(Posted on: {timestamp})</em></div>", unsafe_allow_html=True)
    else:
        st.write("Nincsenek kommentek.")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("<< Előző", key="prev"):
            if page > 0:
                st.session_state.page -= 1
    with col2:
        st.write(f"Oldal: {page + 1}")
    with col3:
        if st.button("Következő >>", key="next"):
            if len(comments) == 2:
                st.session_state.page += 1

if __name__ == "__main__":
    main()
