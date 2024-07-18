import streamlit as st
from firebase_helpers import get_counts, get_progress_summary
import sqlite3
import os

DB_PATH = 'status.db'

def create_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS status (
            id INTEGER PRIMARY KEY,
            main_region TEXT,
            sub_region TEXT,
            view_type TEXT,
            count INTEGER,
            percentage REAL
        )
    ''')
    conn.commit()
    conn.close()

def update_db(data):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM status')  # Clear the table before inserting new data
    for row in data:
        c.execute('INSERT INTO status (main_region, sub_region, view_type, count, percentage) VALUES (?, ?, ?, ?, ?)', row)
    conn.commit()
    conn.close()

def fetch_from_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM status')
    rows = c.fetchall()
    conn.close()
    return rows

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
        .view-type {
            margin-left: 40px;
            font-style: italic;
        }
        .update-note {
            font-size: 16px;
            text-align: center;
            color: red;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="tracker-title">Státusz követése</div>', unsafe_allow_html=True)
    st.markdown('<div class="update-note">Kérjük, várjon kb. 10 másodpercet a frissítéshez</div>', unsafe_allow_html=True)

    if not os.path.exists(DB_PATH):
        create_db()
        update_data = True
    else:
        update_data = False

    if st.button('Frissítés'):
        update_data = True

    if update_data:
        counts, data = get_counts()
        summary = get_progress_summary(counts)
        update_db(data)
    else:
        rows = fetch_from_db()
        counts = {row[1]: {row[2]: {row[3]: row[4] for row in rows if row[1] == row[1] and row[2] == row[2]}} for row in rows}
        summary = get_progress_summary(counts)

    # Calculate grand total progress correctly using count values
    total_done = 0
    for region in summary:
        for sub_region in summary[region]["subregions"]:
            total_done += summary[region]["subregions"][sub_region]["count"]

    total_tasks = 4600  # Set the total number of tasks to 4600 as required

    if total_tasks > 0:
        grand_total_progress = (total_done / total_tasks) * 100
    else:
        grand_total_progress = 0

    st.markdown(f"**Fázis 1 Státusz: {total_done}/{int(total_tasks)} ({grand_total_progress:.1f}%)**")
    st.progress(grand_total_progress / 100)

    # Region and subregion progress
    for main_region, sub_regions in counts.items():
        main_done = sum(summary[main_region]["subregions"][sub]["count"] for sub in sub_regions)  # Use count instead of progress
        main_total_tasks = len(sub_regions) * 200  # Each subregion should have 200 tasks in total
        if main_total_tasks > 0:
            main_progress = (main_done / main_total_tasks) * 100
        else:
            main_progress = 0

        st.subheader(main_region)
        st.markdown(f"**{main_region} Státusz: {main_done}/{main_total_tasks} ({main_progress:.1f}%)**")
        st.progress(main_progress / 100)  # st.progress expects a value between 0 and 1
        
        for sub_region, view_types in sub_regions.items():
            sub_done = sum(view_types.values())
            sub_total_tasks = 200  # Each subregion has 200 tasks
            if sub_total_tasks > 0:
                sub_progress = (sub_done / sub_total_tasks) * 100
            else:
                sub_progress = 0

            st.markdown(f"**{sub_region} Státusz: {sub_done}/{sub_total_tasks} ({sub_progress:.1f}%)**")
            st.progress(sub_progress / 100)  # st.progress expects a value between 0 and 1
            
            for view_type, count in view_types.items():
                percentage = (count / 50) * 100  # Assuming each view type within a subregion has 50 tasks
                if count > 0:
                    st.markdown(f"{view_type}: {count}/50 ({percentage:.1f}%)")

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
