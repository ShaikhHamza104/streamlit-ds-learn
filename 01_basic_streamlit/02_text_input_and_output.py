import streamlit as st 

st.title('text input and output')

st.header('input')
name = st.text_input('Enter your name:')
age = st.number_input('Enter your age:', min_value=0, max_value=120, value=25)
st.write('Your name is:', name)
st.write('Your age is:', age)

st.header('output')
st.write('Hello, ' + name + '!')
st.write('Your name is', name, 'and you are', age, 'years old.')