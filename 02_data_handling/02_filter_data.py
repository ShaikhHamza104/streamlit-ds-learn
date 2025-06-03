import streamlit as st
import pandas as pd

st.title("🔎 Filter Data")

uploaded_file = st.file_uploader("Upload CSV to Filter", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("📊 Original Data:")
    st.dataframe(df)

    col = st.selectbox("Select column to filter", df.columns)
    unique_vals = df[col].unique()

    selected_val = st.selectbox(f"Filter by `{col}`:", unique_vals)
    filtered_df = df[df[col] == selected_val]

    st.write(f"🧪 Filtered Data ({col} = {selected_val}):")
    st.dataframe(filtered_df)
