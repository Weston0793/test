import streamlit as st
from firebase_helpers import initialize_firebase, save_comment, get_comments
import random

def generate_funny_name():
    first_parts = ["Fluffy", "Sparkly", "Wiggly", "Silly", "Funky", "Giggles", "Cheery", "Dizzy", "Bouncy", "Jumpy"]
    second_parts = ["Penguin", "Banana", "Unicorn", "Muffin", "Pickle", "Cupcake", "Bunny", "Monkey", "Noodle", "Puppy"]
    return f"{random.choice(first_parts)} {random.choice(second_parts)}"

def main():
    st.title("Elérhetőség")

    st.write("""
    ### Kapcsolat
    - **Email:** aba.lorincz@gmail.com
    - **Telefon:** +36 30 954 2176
    - **Cím:** Department of Thermophysiology, Institute for Translational Medicine, Medical School, University of Pécs, 12 Szigeti Street, 7624 Pécs, Hungary
    """)

    st.write("### Kommentek")
    
    name = st.text_input("Név", value=generate_funny_name())
    comment = st.text_area("Komment")

    if st.button("Küldés"):
        if comment:
            save_comment(name, comment)
            st.success("Köszönjük a hozzászólást!")
        else:
            st.error("A komment mező nem lehet üres!")

    # Display last 5 comments with navigation
    st.write("### Legutóbbi Kommentek")
    page = st.session_state.get("page", 0)
    comments = get_comments(page * 5, 5)

    for c in comments:
        st.write(f"**{c['name']}**: {c['comment']}")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("<< Előző", key="prev"):
            if page > 0:
                st.session_state.page = page - 1
    with col2:
        st.write(f"Oldal: {page + 1}")
    with col3:
        if st.button("Következő >>", key="next"):
            if len(comments) == 5:
                st.session_state.page = page + 1

if __name__ == "__main__":
    main()
