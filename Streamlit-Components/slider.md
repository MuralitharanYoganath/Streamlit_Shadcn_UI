# Slider Increament and Decreament

```py
import streamlit as st
import streamlit_shadcn_ui as ui

st.header("Slider Component")

# Slider Component
slider_value = ui.slider(default_value=[20], min_value=0, max_value=100, step=2, label="Select a Value", key="slider1")
st.write("Slider Value:", slider_value)

slider_range = ui.slider(default_value=[10, 90], min_value=0, max_value=100, step=2, label="Select a Range", key="slider2")
st.write("Slider Range:", slider_range)
```