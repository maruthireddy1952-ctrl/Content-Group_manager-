import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from run_pipeline import run_pipeline


st.title("📊 YouTube Trend Dashboard")

if st.button("Run Analysis"):

    trends = run_pipeline()

    st.subheader("🔥 Trending Topics")

    for t in trends:
        st.write(f"{t['topic']} → Score: {t['trend_score']}")