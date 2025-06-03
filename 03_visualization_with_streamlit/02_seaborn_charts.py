import pandas as pd
import streamlit as st 
import seaborn as sns

def numric_plot(df,select_column):
    plot = st.selectbox('select a plot',['line','bar','histogram','box'])
    if plot =='line':
        fig = sns.lineplot(df,x=select_column)
        st.pyplot(fig)

    elif plot =='bar':
        fig = sns.barplot(df,x=select_column,)
        st.pyplot(fig)
    
    elif plot =='histogram':
        fig = sns.histplot(df,x=select_column)
        st.pyplot(fig)
    
    else:
        fig = sns.boxplot(df,x=select_column)
        st.pyplot(fig)

def category_plot(df,select_column):
    plot = st.selectbox('select a plot',['countplot','pie chart','bar plot'])
    if plot =='countplot':
        fig = sns.countplot(df,x=select_column)
        st.pyplot(fig)

    elif plot =='pie chart':
        fig = sns.pieplot(df,x=select_column)
        st.pyplot(fig)

    else:
        fig = sns.barplot(df,x=select_column)
        st.pyplot(fig)
        
st.title("Seaborn Charts")
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