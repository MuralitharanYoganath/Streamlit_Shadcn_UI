import streamlit as st
import streamlit_shadcn_ui as ui


with open("Streamlit-Components/Button.md", "r") as f:
    st.markdown(f.read())

clicked = ui.button("Click", key="clk_btn")
ui.button("Reset", key="reset_btn")
st.write("UI Button Clicked:", clicked)

st.write(ui.alert_dialog)