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

    total_progress = sum(summary[region]["progress"] for region in summary) / sum(summary[region]["total"] for region in summary) * 100
    st.markdown(f"**Grand Total Progress: {total_progress:.2f}%**")
    st.progress(total_progress / 100)

    for main_region, sub_regions in counts.items():
        st.subheader(main_region)
        main_progress = summary[main_region]["progress"] / summary[main_region]["total"] * 100
        st.markdown(f"**{main_region} Progress: {main_progress:.2f}%**")
        st.progress(main_progress / 100)  # st.progress expects a value between 0 and 1
        
        for sub_region, view_types in sub_regions.items():
            st.markdown(f'<div class="sub-region-title">{sub_region}</div>', unsafe_allow_html=True)
            
            for view_type, percentage in view_types.items():
                if percentage > 0:
                    st.markdown(f'<div class="view-type">{view_type}: {percentage:.2f}%</div>', unsafe_allow_html=True)
            
            total_progress = sum(view_types.values()) / (len(view_types) * 100) * 100
            st.progress(total_progress / 100)  # st.progress expects a value between 0 and 1

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
