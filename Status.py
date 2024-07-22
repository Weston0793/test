import streamlit as st
import sqlite3
import os
from Styles import status_markdown
from statuslocaldb import create_db, update_db, fetch_from_db, fetch_summary_from_db

DB_PATH = 'status.db'

def get_counts():
    counts = {
        "Felső végtag": {"Váll": {},  "Humerus": {}, "Könyök": {},"Alkar": {}, "Csukló": {}, "Kéz": {}},
        "Alsó végtag": {"Medence": {}, "Pelvis": {}, "Femur": {}, "Térd": {}, "Lábszár": {}, "Boka": {}, "Láb": {}},
        "Gerinc": {"Cervicalis": {}, "Thoracalis": {}, "Lumbaris": {}, "Sacralis": {}, "Coccygealis": {}},
        "Koponya": {"Arckoponya": {}, "Agykoponya": {}, "Mandibula": {}},
        "Mellkas": {"Borda": {}, "Sternum": {}},
    }
    views = ["AP", "Lateral"]
    main_types = ["Normál", "Törött"]

    data = []

    for main_region in counts:
        for sub_region in counts[main_region]:
            for view in views:
                for main_type in main_types:
                    docs = db.collection('images').where('main_region', '==', main_region).where('sub_region', '==', sub_region).where('view', '==', view).where('main_type', '==', main_type).stream()
                    count = len(list(docs))
                    counts[main_region][sub_region][f"{main_type}_{view}"] = count
                    data.append([main_region, sub_region, view, main_type, count])
    return counts, data
    
def get_progress_summary(counts):
    summary = {}
    for main_region, sub_regions in counts.items():
        summary[main_region] = {"total": 0, "progress": 0, "subregions": {}}
        for sub_region, view_types in sub_regions.items():
            sub_region_total = 0
            sub_region_progress = 0
            for view_type, count in view_types.items():
                sub_region_total += 50
                sub_region_progress += count
            summary[main_region]["total"] += sub_region_total
            summary[main_region]["progress"] += sub_region_progress
            summary[main_region]["subregions"][sub_region] = {"total": sub_region_total, "count": sub_region_progress}
    return summary

def main():
    status_markdown()
    st.markdown('<div class="tracker-title">Státusz követése</div>', unsafe_allow_html=True)
    st.markdown('<div class="update-note">Kérjük, várjon kb. 10 másodpercet a frissítéshez</div>', unsafe_allow_html=True)

    # Check if the local database exists
    if not os.path.exists(DB_PATH):
        create_db()
        data_exists = False
    else:
        data_exists = True

    if st.button('Frissítés') or not data_exists:
        counts, data = get_counts()
        summary = get_progress_summary(counts)
        update_db(data)
        st.success('Adatok frissítve!')
    else:
        counts, summary = fetch_summary_from_db()

    # Calculate grand total progress correctly using count values
    total_done = 0
    total_tasks = 0
    for region in summary:
        for sub_region in summary[region]["subregions"]:
            total_done += summary[region]["subregions"][sub_region]["count"]
            total_tasks += 200  # Each subregion has 200 tasks

    if total_tasks > 0:
        grand_total_progress = (total_done / total_tasks) * 100
    else:
        grand_total_progress = 0

    st.markdown(f'<div class="grand-total">Fázis 1 Státusz: {total_done}/{int(total_tasks)} ({grand_total_progress:.1f}%)</div>', unsafe_allow_html=True)
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

        sub_regions_sorted = sorted(sub_regions.items(), key=lambda x: x[0])
        grid_size = 2
        for i in range(0, len(sub_regions_sorted), grid_size):
            cols = st.columns(grid_size)
            for idx, (sub_region, view_types) in enumerate(sub_regions_sorted[i:i + grid_size]):
                with cols[idx]:
                    sub_done = sum(view_types.values())
                    sub_total_tasks = 200  # Each subregion has 200 tasks
                    if sub_total_tasks > 0:
                        sub_progress = (sub_done / sub_total_tasks) * 100
                    else:
                        sub_progress = 0

                    st.markdown(f"**{sub_region} Státusz: {sub_done}/{sub_total_tasks} ({sub_progress:.1f}%)**")
                    st.progress(sub_progress / 100)  # st.progress expects a value between 0 and 1

                    view_types_sorted = sorted(view_types.items(), key=lambda x: x[0])
                    for view_type, count in view_types_sorted:
                        percentage = (count / 50) * 100  # Assuming each view type within a subregion has 50 tasks
                        st.markdown(f"{view_type}: {count}/50 ({percentage:.1f}%)")

if __name__ == "__main__":
    main()
