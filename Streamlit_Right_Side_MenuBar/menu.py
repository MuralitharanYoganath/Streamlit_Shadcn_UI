import streamlit as st
from streamlit_extras import stylable_container

with stylable_container(
    key="Upload_Data",
    css_styles="""
    button{
        display: flex;
        justify-content: flex-end;
        width: 100%;
    }
    """
):
    st.button("Upload Data")