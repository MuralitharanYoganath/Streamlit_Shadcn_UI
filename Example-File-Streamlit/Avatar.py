import streamlit as st
import streamlit_shadcn_ui as ui

with open("Streamlit-Components/Avatar.md", "r") as f:
    st.markdown(f.read())
    
ui.avatar(src="https://your_image_url") # type: ignore

st.write(ui.alert_dialog)