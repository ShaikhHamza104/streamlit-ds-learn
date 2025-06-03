import streamlit as st
import pandas as pd
import numpy as np  
import seaborn as sns
import matplotlib.pyplot as plt

st.title("EDA-APP")

file_uploader = st.file_uploader("Choose a CSV file", type="csv")

if file_uploader is not None:
    df = pd.read_csv(file_uploader)
    st.write("📊 Original Data:")
    st.dataframe(df)

    # Data overview 
    st.subheader("Data Overview")
    st.write("Number of rows:", df.shape[0])
    st.write("Number of columns:", df.shape[1])
    st.write("Column names:", df.columns.tolist())

    # Data summary
    st.subheader("Data Summary")
    st.write(df.describe())

    
    col = st.selectbox("Select column to filter", df.columns)
    unique_vals = df[col].unique()

    selected_val = st.selectbox(f"Filter by `{col}`:", unique_vals)
    filtered_df = df[df[col] == selected_val]

    st.write(f"🧪 Filtered Data ({col} = {selected_val}):")
    st.dataframe(filtered_df)

    # Data cleaning
    st.subheader("Data Cleaning")
    st.write("Number of missing values:", df.isnull().sum().sum())
    st.write("Number of duplicate rows:", df.duplicated().sum())
    
    # Handle duplicates
    if st.checkbox("Drop duplicate rows"):
        df.drop_duplicates(inplace=True)
        st.write("Number of duplicate rows after dropping:", df.duplicated().sum())
    
    # Handle missing values
    missing_option = st.selectbox('Handle Missing values', ['None', 'Drop', 'Fill'])
    
    if missing_option == 'Drop':
        col_to_drop = st.selectbox('Select column to drop nulls from', df.columns)
        if st.button("Apply Drop"):
            df.dropna(subset=[col_to_drop], inplace=True)
            st.write("Number of missing values after dropping:", df.isnull().sum().sum())
    
    elif missing_option == 'Fill':
        col_to_fill = st.selectbox('Select column to fill', df.columns)
        fill_method = st.selectbox('Fill method', ['Mean', 'Median', 'Mode', 'Custom Value'])
        
        if st.button("Apply Fill"):
            if fill_method == 'Mean' and pd.api.types.is_numeric_dtype(df[col_to_fill]):
                df[col_to_fill].fillna(df[col_to_fill].mean(), inplace=True)
            elif fill_method == 'Median' and pd.api.types.is_numeric_dtype(df[col_to_fill]):
                df[col_to_fill].fillna(df[col_to_fill].median(), inplace=True)
            elif fill_method == 'Mode':
                df[col_to_fill].fillna(df[col_to_fill].mode()[0], inplace=True)
            elif fill_method == 'Custom Value':
                custom_value = st.text_input("Enter custom value")
                if custom_value:
                    df[col_to_fill].fillna(custom_value, inplace=True)
            
            st.write("Number of missing values after filling:", df.isnull().sum().sum())

    # Data visualization
    st.subheader("Data Visualization")
    
    viz_type = st.selectbox(
        "Select Visualization Type", 
        ["Correlation Matrix", "Scatter Plot", "Bar Plot", "Histogram", "Box Plot"]
    )
    
    if viz_type == "Correlation Matrix":
        corr_matrix = df.corr()
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
        
    elif viz_type == "Scatter Plot":
        scatter_x = st.selectbox("Select x-axis column for scatter plot", df.columns)
        scatter_y = st.selectbox("Select y-axis column for scatter plot", df.columns)
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.scatterplot(data=df, x=scatter_x, y=scatter_y, ax=ax)
        st.pyplot(fig)
        
    elif viz_type == "Bar Plot":
        bar_x = st.selectbox("Select x-axis column for bar plot", df.columns)
        bar_y = st.selectbox("Select y-axis column for bar plot", df.columns)
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.barplot(data=df, x=bar_x, y=bar_y, ax=ax)
        st.pyplot(fig)
        
    elif viz_type == "Histogram":
        hist_col = st.selectbox("Select column for histogram", df.columns)
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.histplot(data=df, x=hist_col, ax=ax)
        st.pyplot(fig)
        
    elif viz_type == "Box Plot":
        box_col = st.selectbox("Select column for box plot", df.columns)
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.boxplot(data=df, x=box_col, ax=ax)
        st.pyplot(fig)

    # Download the cleaned data
    st.subheader("Download the cleaned data")
    st.write("Download the cleaned data as a CSV file")
    st.download_button("Download CSV", df.to_csv(index=False), "cleaned_data.csv", "text/csv")

