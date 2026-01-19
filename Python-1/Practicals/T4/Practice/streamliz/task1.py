import streamlit as st

st.set_page_config(
    page_title='Rizzing up',
    page_icon='😏',
    layout='centered'
)



st.title('Faculty Profile')

st.sidebar.header('Profile Settings')

name = st.sidebar.text_input('Enter your name')



dep = st.sidebar.selectbox('Enter Your department',['cse','ce','it'])
st.write('Enter Subjects you teach: ')
subs = {'Python':0, 'Fsd': 0, 'mern': 0}

for i,j in subs.items():
    temp = st.sidebar.checkbox(i)
    j = temp
st.write(subs)
exp = st.sidebar.slider('Enter Your Experience in years: ',0,14,3)
col1,col2 = st.columns([1,2])

with col1:

    st.write(f'Your Name: {name}')
    st.write(f'Your Department: {dep}')
    st.write(f'Your experience: {exp}')

with col2:
    st.markdown('## About')

with st.expander("Subject tought"):
    
    for i,j in subs.items():
        if j>0:
            st.write(i)

