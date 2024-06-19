# Experiment Card

```py
import streamlit as st
import streamlit_shadcn_ui as ui

st.header("Experiment(Cool)")

with ui.card(key="base_ele_card_l1"):
    with ui.card(key="base_ele_card_l2"):
    # with ui.element("card", key="base_ele1") as card2:
        ui.element("input", key="nst2_input")
        ui.element("button", key="nst2_btn", text="First Submmit", variant="outline")

    ui.element("button", key="nst_btn", text="Hello World")
```