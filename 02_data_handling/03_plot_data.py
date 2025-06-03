import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Plot CSV Data")

uploaded_file = st.file_uploader("Upload a CSV to plot", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("📋 Data Preview:")
    st.dataframe(df)

    numeric_cols = df.select_dtypes(include=['int', 'float']).columns.tolist()

    if len(numeric_cols) >= 2:
        x_col = st.selectbox("X-axis", numeric_cols)
        y_col = st.selectbox("Y-axis", numeric_cols, index=1)

        fig = px.scatter(df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}")
        st.plotly_chart(fig)
    else:
        st.warning("Need at least 2 numeric columns to plot.")
