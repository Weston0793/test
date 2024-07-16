import streamlit as st
from firebase_helpers import get_counts, get_progress_summary
import uuid
import sqlite3
import time


# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('progress.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS progress
                 (main_region TEXT, sub_region TEXT, view_type TEXT, type TEXT, percentage REAL)''')
    conn.commit()
    conn.close()

# Save progress to SQLite database
def save_progress_to_db(data):
    conn = sqlite3.connect('progress.db')
    c = conn.cursor()
    c.execute('DELETE FROM progress')  # Clear existing data
    for row in data:
        c.execute('INSERT INTO progress VALUES (?,?,?,?,?)', row)
    conn.commit()
    conn.close()

# Load progress from SQLite database
def load_progress_from_db():
    conn = sqlite3.connect('progress.db')
    c = conn.cursor()
    c.execute('SELECT * FROM progress')
    data = c.fetchall()
    conn.close()
    return data

# Get progress from Firestore and save to SQLite
def update_progress():
    counts, data = get_counts()
    save_progress_to_db(data)
    return counts

# Display progress
def display_progress(counts):
    data = load_progress_from_db()
    summary = get_progress_summary(counts)

    progress_dict = {}
    for row in data:
        main_region, sub_region, view_type, type, percentage = row
        if main_region not in progress_dict:
            progress_dict[main_region] = {}
        if sub_region not in progress_dict[main_region]:
            progress_dict[main_region][sub_region] = {}
        progress_dict[main_region][sub_region][f"{type}_{view_type}"] = percentage

    grand_total = 0
    grand_completed = 0
    for main_region, sub_regions in progress_dict.items():
        st.subheader(main_region)
        main_progress = summary[main_region]["progress"] / summary[main_region]["total"] * 100
        st.progress(main_progress / 100)
        st.text(f"Teljesítés: {summary[main_region]['progress']} / {summary[main_region]['total']} ({main_progress:.2f}%)")

        grand_total += summary[main_region]["total"]
        grand_completed += summary[main_region]["progress"]

        for sub_region, view_types in sub_regions.items():
            st.markdown(f'<div class="sub-region-title">{sub_region}</div>', unsafe_allow_html=True)
            total_progress = sum(view_types.values()) / (len(view_types) * 100) * 100
            st.progress(total_progress / 100)
            st.text(f"Teljesítés: {sum(view_types.values())} / {len(view_types) * 100} ({total_progress:.2f}%)")

    grand_total_progress = grand_completed / grand_total * 100 if grand_total else 0
    st.subheader("Összesített Teljesítés")
    st.progress(grand_total_progress / 100)
    st.text(f"Teljesítés: {grand_completed} / {grand_total} ({grand_total_progress:.2f}%)")

def main():
    st.markdown(
        """
        <style>
        .tracker-title {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            border: 2px solid black;
            padding: 10px;
            margin-bottom: 20px;
        }
        .sub-region-title {
            margin-left: 20px;
            font-weight: bold;
            margin-top: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="tracker-title">Státusz követése</div>', unsafe_allow_html=True)

    # Initialize database
    init_db()

    # Option to update progress
    if st.button("Frissítés"):
        with st.spinner('Frissítés folyamatban...'):
            counts = update_progress()
            time.sleep(2)
        st.success('Frissítés kész!')
    else:
        counts, _ = get_counts()

    # Display progress
    display_progress(counts)

if __name__ == "__main__":
    main()
