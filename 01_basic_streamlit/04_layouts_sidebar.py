import streamlit as st
import pandas as pd 

# Columns layout example
st.write("**Columns Layout:**")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**Column 1**")
    st.info('This is column 1 content')
with col2:
    st.markdown("**Column 2**")
    st.warning('This is column 2 content')
with col3:
    st.markdown("**Column 3**")
    st.error('This is column 3 content')

# Multi-select and slider
st.write("**Multiple Selection:**")
multiselect = st.multiselect('Select multiple options:', ['Option 1', 'Option 2', 'Option 3', 'Option 4'])
if multiselect:
    st.write(f'You selected: {", ".join(multiselect)}')

st.write("**Value Slider:**")
slider = st.slider('Select a value:', 0, 100, 50, help="Drag to select a value between 0 and 100")
st.write(f'Selected value: {slider}')

st.markdown("---")



# Tabs example
st.write("**Tabs Layout:**")
tab1, tab2, tab3 = st.tabs(['Data', 'Visualization', 'Settings'])
with tab1:
    st.markdown("**Data Tab**")
    st.write('This tab would contain your data tables')
    st.dataframe({'Name': ['John', 'Anna', 'Peter'], 'Age': [28, 34, 41]})
with tab2:
    st.markdown("**Visualization Tab**")
    st.write('This tab would contain your charts and plots')
    chart_data = pd.DataFrame({"col1": [1, 2, 3, 4], "col2": [10, 20, 30, 40]})
    st.line_chart(chart_data)
with tab3:
    st.markdown("**Settings Tab**")
    st.write('This tab would contain your app settings')
    st.checkbox('Enable dark mode')
    st.checkbox('Enable notifications')
