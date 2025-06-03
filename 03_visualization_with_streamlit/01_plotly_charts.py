import pandas as pd 
import numpy as np 
import plotly.express as px 
import streamlit as st 

def numric_plot(df,select_column):
    plot = st.selectbox('select a plot',['line','bar','histogram','box'])
    if plot =='line':
        fig = px.line(df,x=select_column)
        st.plotly_chart(fig)

    elif plot =='bar':
        fig = px.bar(df,x=select_column,)
        st.plotly_chart(fig)

    elif plot =='histogram':
        fig = px.histogram(df,x=select_column)
        st.plotly_chart(fig)

    else:
        fig = px.box(df,x=select_column)
        st.plotly_chart(fig)
def category_plot(df,select_column):
    plot = st.selectbox('select a plot',['countplot','pie chart','bar plot'])
    if plot =='countplot':
        fig = px.bar(df,x=select_column)
        st.plotly_chart(fig)

    elif plot =='pie chart':
        fig = px.pie(df,x=select_column)
        st.plotly_chart(fig)

    else:
        fig = px.bar(df,x=select_column)
        st.plotly_chart(fig)
st.title("Plotly Charts")
df = pd.read_csv('https://raw.githubusercontent.com/ShaikhHamza104/Pandas-for-beginner/refs/heads/main/datasets/courses.csv')

column_type =st.selectbox('select a column type ',['numric','category'])
if column_type =='numric':
    numric = df.select_dtypes(include=['int','float']).columns.tolist()
    select_column = st.selectbox('select a column ',numric)
    numric_plot(df,select_column)
else:

    category = df.select_dtypes(include=['category','object']).columns.tolist()
    select_column = st.selectbox('select a column ',category)
    category_plot(df,select_column)