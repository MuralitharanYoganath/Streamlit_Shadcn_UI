import streamlit as st
import streamlit_shadcn_ui as ui

st.header("Input Select Option")

choice = ui.select(options=["Apple", "Banana", "Orange"])

st.markdown(f"Currrent value: {choice}")