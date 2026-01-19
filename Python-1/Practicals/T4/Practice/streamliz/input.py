import streamlit as st

st.set_page_config(
    page_title='Rizzing up',
    page_icon='😏',
    layout='centered'
)


st.header('Input Demo')

a = st.text_input('Enter Name')

b = st.text_area('Text area')


st.write('Live op')

if a:
    st.write(f'Your name: {a}')
if b:
    st.write(f'Comment: {b}')


st.title('Number Input')

number = st.number_input('Enter a number',min_value=0,max_value=80)

s = st.slider('SLide',0,100,0,step=2)


st.write(number)
st.write(s, type(s))