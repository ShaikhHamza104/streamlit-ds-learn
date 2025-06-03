import streamlit as st
import pandas as pd

st.title("📁 Upload and Display CSV")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("CSV Loaded Successfully!")
    st.write("🔍 Preview of Data:")
    st.dataframe(df)
else:
    st.info("Upload a CSV to get started.")
