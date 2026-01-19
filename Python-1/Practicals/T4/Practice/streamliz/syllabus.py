import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 1. PAGE CONFIGURATION [cite: 608]
# Must be the first Streamlit command in your script 
st.set_page_config(
    page_title="Comprehensive Syllabus Demo",
    page_icon="🐍",
    layout="wide"  # Options: "centered" or "wide" 
)

# 2. TEXT & DISPLAY ELEMENTS 
st.title("Streamlit Syllabus Master Code") # Largest heading [cite: 610]
st.header("This is a Header") # Section heading [cite: 610]
st.subheader("This is a Subheader") # Subsection heading [cite: 610]
st.text("This is standard pre-formatted text.") # Simple text [cite: 611]
st.markdown("### Markdown Support\nStreamlit supports **bold**, *italics*, and [links](https://streamlit.io).") 

# st.write can display text, dataframes, charts, and variables together 
st.write("st.write is versatile:", {"Key": "Value"}, 12345) 

# Displaying code snippets [cite: 611]
st.code("""
def greet():
    return "Hello Streamlit!"
""", language="python")

# 3. INTERACTIVE INPUT WIDGETS 
st.header("Input Widgets")

# Text Input (single line) and Text Area (multi-line) [cite: 613]
user_name = st.text_input("Enter your name:")
feedback = st.text_area("Enter your feedback:")

# Selection widgets [cite: 614, 615]
gender = st.radio("Select Gender", ["Male", "Female", "Other"]) # Single select radio [cite: 614]
course = st.selectbox("Select Course", ["Python", "Java", "C++"]) # Dropdown select [cite: 614]
hobbies = st.multiselect("Hobbies", ["Reading", "Coding", "Gaming", "Travel"]) # Multi-select [cite: 615]

# Slider & Number Input [cite: 614]
age = st.slider("Select Age", 0, 100, 25) # Returns value selected on slider [cite: 624]
marks = st.number_input("Enter Marks", 0, 100) # Manual number entry [cite: 614]

# Checkbox [cite: 615]
if st.checkbox("Agree to terms"):
    st.write("Thank you for agreeing!")

# 4. FILE HANDLING & MEDIA [cite: 616, 617, 618, 619]
st.header("Files & Media")

# Uploading files (CSV, Image, PDF) [cite: 616, 617]
uploaded_file = st.file_uploader("Upload a file", type=["csv", "png", "jpg", "pdf"]) 
if uploaded_file is not None:
    st.success("File Uploaded Successfully!") 
# Download button [cite: 618]
st.download_button(label="Download Sample Data", data="Hello World", file_name="sample.txt")

# Image display [cite: 619]
# st.image("path_to_image.jpg") # Use this to show images [cite: 619]

# 5. BUTTONS & MESSAGES [cite: 618, 620, 621]
if st.button("Submit"): # Logic executes only when clicked [cite: 621]
    st.success("Action Completed!") # Green message [cite: 620]
    st.info("This is an information message.") # Blue message [cite: 620]
    st.warning("This is a warning.") # Yellow/Orange message [cite: 712]

# 6. LAYOUTS & CONTAINERS [cite: 612, 626]
# Sidebar layout [cite: 612]
st.sidebar.header("Sidebar Menu")
side_choice = st.sidebar.selectbox("Sidebar Option", ["Dashboard", "Settings"])

# Columns layout [cite: 756]
col1, col2 = st.columns(2)
with col1:
    st.write("Column 1 Content")
with col2:
    st.write("Column 2 Content")

# Expander (collapsible section) [cite: 626]
with st.expander("See More Details"):
    st.write("Here is the hidden information that can be toggled.") 

# 7. MATPLOTLIB INTEGRATION [cite: 622]
st.header("Charts")
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [10, 20, 30])
st.pyplot(fig) # Displays Matplotlib figures in the app [cite: 622]

