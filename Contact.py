import streamlit as st
from firebase_helpers import initialize_firebase, save_comment, get_comments
import random
import datetime

# Ensure Firebase is initialized
initialize_firebase()
def add_custom_css():
    st.markdown("""
    <style>
    @keyframes fadeIn {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }
    .fade-in {
        animation: fadeIn 2s;
    }
    .hover-effect:hover {
        color: #007BFF;
        transform: scale(1.05);
    }
    .loading-spinner {
        border: 8px solid #f3f3f3;
        border-top: 8px solid #007BFF;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        animation: spin 1s linear infinite;
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    </style>
    """, unsafe_allow_html=True)
    
def generate_funny_name():
    first_parts = ["Fluffy", "Sparkly", "Wiggly", "Silly", "Funky", "Giggles", "Cheery", "Dizzy", "Bouncy", "Jumpy",
                   "Zippy", "Snazzy", "Bubbly", "Quirky", "Jolly", "Peppy", "Giddy", "Chirpy", "Frisky", "Perky",
                   "Whizzy", "Fizzy", "Nifty", "Ducky", "Zappy", "Chipper", "Jazzy", "Snappy", "Zany"]
    second_parts = ["Penguin", "Banana", "Unicorn", "Muffin", "Pickle", "Cupcake", "Bunny", "Monkey", "Noodle", "Puppy",
                    "Sprout", "Pancake", "Mango", "Gizmo", "Taco", "Bubble", "Pudding", "Doodle", "Coconut", "Waffle",
                    "Marshmallow", "Pepper", "Sundae", "Snickers", "Button", "Tinker", "Pebble", "Cookie", "Biscuit"]
    return f"{random.choice(first_parts)} {random.choice(second_parts)}"

def main():
    add_custom_css()
    
    st.markdown('<h1 class="fade-in">Elérhetőség</h1>', unsafe_allow_html=True)

    st.markdown("""
    ### Kapcsolat
    - **<span class="hover-effect">Email:</span>** aba.lorincz@gmail.com
    - **<span class="hover-effect">Telefon:</span>** +36 30 954 2176
    - **<span class="hover-effect">Cím:</span>** Department of Thermophysiology, Institute for Translational Medicine, Medical School, University of Pécs, 12 Szigeti Street, 7624 Pécs, Hungary
    """, unsafe_allow_html=True)

    st.write("### Kommentszekció")
    
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

    # Display last comments with navigation
    st.write("### Legutóbbi Kommentek")
    
    if 'page' not in st.session_state:
        st.session_state.page = 0

    page = st.session_state.page
    comments = get_comments(page * 2, 2)

    if comments:
        for c in comments:
            timestamp = c['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
            st.write(f"**{c['name']}**: {c['comment']} *(Posted on: {timestamp})*")
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
