import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(page_title="Pandas Profiling App", layout="wide")
st.title("📊 Automated EDA with ydata-profiling")

# Upload CSV
uploaded_file = st.file_uploader("📁 Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("✅ Data Preview")
    st.dataframe(df.head())

    # Generate Profile
    st.info("⏳ Generating Profile Report... Please wait.")
    profile = ProfileReport(df, title="🔍 EDA Report", explorative=True)
    st_profile_report(profile)
else:
    st.warning("👆 Please upload a CSV file to continue.")
