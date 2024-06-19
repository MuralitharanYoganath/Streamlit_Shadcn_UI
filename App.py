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
st.button("Submit")

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