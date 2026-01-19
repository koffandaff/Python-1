import streamlit as st

st.set_page_config(
    page_title='Rizzing up',
    page_icon='😏',
    layout='centered'
)


st.header('animaton Widget Demo')

options = ['Option 1', 'Option 2', 'Option 3']

choice = st.selectbox('Choose an option:', options)

choices = st.multiselect('Choose some options:', options)

if st.button('Submit'):
    st.write(f"You chose: {choice}")
    for choice in choices:
        st.write(f"You chose: {choice}")