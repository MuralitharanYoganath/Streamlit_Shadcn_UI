import streamlit as st
import streamlit_shadcn_ui as ui

st.header("Input Select Option")

with open("Streamlit-Components/Select.md", "r") as f:
    
    st.markdown(f.read())

choice = ui.select(options=["Apple", "Banana", "Orange"])

st.markdown(f"Currrent value: {choice}")

st.write(ui.alert_dialog)