import streamlit as st

st.title('Media display')

st.header('Media display')

st.logo('../src/img/logo.jpg')
st.subheader('Image')
st.image('../src/img/cat.jpg')

st.subheader('Video')
st.video('../src/video/cat.mp4')

st.subheader('Audio')
st.audio('../src/audio/cat.mp3')
