import streamlit as st

import streamlit_shadcn_ui as ui

st.header("Link Button")
with open("Streamlit-Components/LinkButton.md", "r") as f:
    
    st.markdown(f.read())

ui.link_button(text="Swayaan digital", url="https://swayaan.com/index.html", key="link_btn")

st.write(ui.alert_dialog)