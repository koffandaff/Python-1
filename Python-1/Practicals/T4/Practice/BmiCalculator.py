import streamlit as st

st.set_page_config(
    layout='centered',
    page_title='BMI calculator'
)

st.title('BMI Calculator')
st.header('Your data: ')

st.sidebar.title('Enter Data')

weight = st.sidebar.number_input('Enter Weight in (kg)')
if weight:
    st.text(f'Weight: {weight}')
height = st.sidebar.number_input('Enter height in (cm)')
if height:
    st.text(f'Height: {height}')

cta = st.sidebar.button("Calculate")


if cta and weight and height:
    BMI = weight / ((height/100) **2)
    st.text(f'BMI: {BMI}')
    st.success('Calculated Successfully')