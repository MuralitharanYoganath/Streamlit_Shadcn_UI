import streamlit as st
import streamlit_shadcn_ui as ui
import pandas as pd
from streamlit_option_menu import option_menu


# Page configuration
st.header("Recruiter AI")

# Sidebar
with st.sidebar:
    selected = option_menu(
        menu_title= None,
        options=["Home","Project","Details"],
    )

# Job description input
job_description = st.text_area("Describe to Job Profile")

# Submit button
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    ui.button('Submit', key='btn1')
with col2:
    ui.button('View', key='btn2')
with col3:
    ui.button('Resources', key='btn3')

# Candidates table
st.subheader("Candidates")
candidates = {
    "Name": ["", "", "", ""],
    "Job ID": ["", "", "", ""],
    "Mobile": ["", "", "", ""],
    "View more": ["", "", "", ""],
    "Status": ["", "", "", ""]
}

df = pd.DataFrame(candidates)

st.dataframe(df)


# Schedule interview button

st.button("Schedule interview")  