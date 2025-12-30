import streamlit as st
import pandas as pd

st.title("📊 TrojanChat Metrics")

data = pd.DataFrame({
    "latency_ms": [420, 390, 410],
    "tokens": [120, 135, 128]
})

st.line_chart(data)