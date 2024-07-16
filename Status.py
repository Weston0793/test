import streamlit as st
from firebase_helpers import get_counts, get_progress_summary
import uuid
import sqlite3
import time

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
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="tracker-title">Státusz követése</div>', unsafe_allow_html=True)

    counts, data = get_counts()
    summary = get_progress_summary(counts)

    # Grand total progress
    total_done = sum(summary[region]["progress"] for region in summary)
    total_tasks = sum(summary[region]["total"] for region in summary)
    if total_tasks > 0:
        total_progress = (total_done / total_tasks) * 100
    else:
        total_progress = 0

    st.markdown(f"**Grand Total Progress: {total_done}/{total_tasks} ({int(total_progress)}%)**")
    st.progress(total_progress / 100)

    # Region and subregion progress
    for main_region, sub_regions in counts.items():
        main_done = summary[main_region]["progress"]
        main_total = summary[main_region]["total"]
        if main_total > 0:
            main_progress = (main_done / main_total) * 100
        else:
            main_progress = 0

        st.subheader(main_region)
        st.markdown(f"**{main_region} Progress: {main_done}/{main_total} ({int(main_progress)}%)**")
        st.progress(main_progress / 100)  # st.progress expects a value between 0 and 1
        
        for sub_region, view_types in sub_regions.items():
            sub_done = sum(view_types.values())
            sub_total = len(view_types) * 100  # Assuming each view type is out of 100
            if sub_total > 0:
                sub_progress = (sub_done / sub_total) * 100
            else:
                sub_progress = 0

            st.markdown(f'<div class="sub-region-title">{sub_region} Progress: {int(sub_done)}/{sub_total} ({int(sub_progress)}%)</div>', unsafe_allow_html=True)
            st.progress(sub_progress / 100)  # st.progress expects a value between 0 and 1
            
            for view_type, percentage in view_types.items():
                if percentage > 0:
                    st.markdown(f'<div class="view-type">{view_type}: {int(percentage)}%</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
