import streamlit as st
from firebase_helpers import get_counts

def tracker_section():
    st.markdown(
        """
        <style>
        .tracker-box {
            border: 2px solid black;
            padding: 20px;
            margin-bottom: 20px;
        }
        .tracker-title {
            font-size: 24px;
            font-weight: bold;
        }
        .sub-region-title {
            margin-left: 20px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="tracker-box">', unsafe_allow_html=True)
    st.markdown('<div class="tracker-title">Státusz követése</div>', unsafe_allow_html=True)

    counts, data = get_counts()
    for main_region, sub_regions in counts.items():
        st.subheader(main_region)
        for sub_region, view_types in sub_regions.items():
            st.markdown(f'<div class="sub-region-title">{sub_region}</div>', unsafe_allow_html=True)
            for view_type, percentage in view_types.items():
                if percentage > 0:
                    st.text(f"{view_type}: {percentage:.2f}%")
    st.markdown('</div>', unsafe_allow_html=True)
