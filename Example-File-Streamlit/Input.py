import streamlit as st
import streamlit_shadcn_ui as ui

st.header("Input Component")
    
with open("Streamlit-Components/Input.md", "r") as f:
    
    st.markdown(f.read())

# Input Component
input_value = ui.input(default_value="Hello, Streamlit!", type='text', placeholder="Enter text here", key="input1")
st.write("Input Value:", input_value)

st.write(ui.alert_dialog)