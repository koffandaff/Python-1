import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="LJU Python Master App", layout="wide")

# --- 712: SIDEBAR CONFIGURATION ---
st.sidebar.header("Global Health Tracker")
# Sidebar dropdown for country selection 
country = st.sidebar.selectbox("Select Country", ["India", "USA", "UK", "Canada"])

# --- 711: USER PROFILE SECTION ---
st.header("👤 User Profile Section")
col_profile_1, col_profile_2 = st.columns(2)

with col_profile_1:
    # Text input for Name 
    name = st.text_input("Enter Name")
    # Radio buttons for Gender 
    gender = st.radio("Choose Gender", ["Male", "Female", "Other"])
    # Multiselect for Hobbies 
    hobbies = st.multiselect("Select multiple Hobbies", ["Reading", "Coding", "Sports", "Music"])

with col_profile_2:
    # File uploader for profile picture 
    uploaded_pic = st.file_uploader("Upload a profile picture", type=["jpg", "png", "jpeg"])
    if uploaded_pic is not None:
        st.image(uploaded_pic, caption=f"{name}'s Profile Picture", width=200)

st.divider()

# --- 712: VACCINATION CALCULATOR ---
st.header(f"💉 Vaccination Analysis: {country}")
# Number inputs for population and vaccinated individuals 
total_pop = st.number_input("Total Population", min_value=1, value=1000)
vac_people = st.number_input("Vaccinated People", min_value=0, value=500)

# Button to trigger calculation 
if st.button("Calculate Vaccination %"):
    vac_percent = (vac_people / total_pop)
    st.write(f"Results for {country}: {vac_percent*100:.2f}%")
    # Progress bar display 
    st.progress(vac_percent if vac_percent <= 1.0 else 1.0)
    
    # Success/Warning message based on percentage 
    if vac_percent >= 0.7:
        st.success("Immunity Goal Reached! (Above 70%)")
    else:
        st.warning("Vaccination rate is below the 70% target.")

st.divider()

# --- 713: MARKS CALCULATOR (COLUMNS) ---
st.header("📝 Student Marks Calculator")
# Creating 5 columns for subject inputs [cite: 756]
m_col = st.columns(5)
with m_col[0]: sub1 = st.number_input("Subject 1", 0, 100, step=1)
with m_col[1]: sub2 = st.number_input("Subject 2", 0, 100, step=1)
with m_col[2]: sub3 = st.number_input("Subject 3", 0, 100, step=1)
with m_col[3]: sub4 = st.number_input("Subject 4", 0, 100, step=1)
with m_col[4]: sub5 = st.number_input("Subject 5", 0, 100, step=1)

# Button to calculate Total and Average [cite: 757]
if st.button("Calculate Marks"):
    total = sub1 + sub2 + sub3 + sub4 + sub5
    avg = total / 5
    st.info(f"Total Marks: {total}")
    st.info(f"Average Marks: {avg}")

st.divider()

# --- 715: MATPLOTLIB INTEGRATION ---
st.header("📊 Random Data Scatter Plot")
# Input for number of points 
n = st.number_input("Enter number of random points (n)", min_value=1, value=50)

if st.button("Generate Scatter Plot"):
    # Generate n random values [cite: 763]
    x_data = np.random.rand(n)
    y_data = np.random.rand(n)
    
    # Create Matplotlib figure [cite: 763]
    fig, ax = plt.subplots()
    ax.scatter(x_data, y_data, color='purple', alpha=0.6)
    ax.set_title(f"Scatter Plot of {n} Random Points")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    
    # Display in Streamlit 
    st.pyplot(fig)