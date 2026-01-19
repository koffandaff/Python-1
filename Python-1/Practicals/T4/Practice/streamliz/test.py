import streamlit as st

st.markdown(''' # Page Configuration
    IT has: 
        1. Page_title
        2. Page_icon: emoji
        3. layout: centered , wide

''')

st.markdown(''' ##### use st. everywhere
    ## TO write in streamlit Page layout
    ext: title
    1. Headers
    2. SubHeader
    3. text
    4. write ( can take input as fig, dict or whatever)
    5. markdown
    6. code
''')

st.set_page_config(
    page_title='Rizzing up',
    page_icon='😏',
    layout='centered'
)

# Title
st.title('This is a title')

# Headers
st.header("This is a header")

# SubHeader
st.subheader("This is a sub-header")

# Text
st.text("This is some text.")

st.write("This is write function")
st.write(1234567890)  # numbers
st.write([1, 2, 3, 4, 5])  # lists

st.markdown("# This is a markdown header")
st.markdown("## This is a smaller markdown header")

code = """
def hello():
    print("Hello, Streamlit!")
"""
st.code(code, language='python')
