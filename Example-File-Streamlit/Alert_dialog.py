import streamlit as st
import streamlit_shadcn_ui as ui

with open("Streamlit-Components/Alert-dialog.md", "r") as f:
    st.markdown(f.read())

trigger_btn = ui.button(text="Trigger Button", key="trigger_btn_1")
ui.alert_dialog(show=trigger_btn, title="Alert Dialog", description="This is an alert dialog", confirm_label="OK", cancel_label="Cancel", key="alert_dialog_1")   

st.write(ui.alert_dialog)