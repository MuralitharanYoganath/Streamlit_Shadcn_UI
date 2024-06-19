# CheckBox Option

```py
import streamlit as st

import streamlit_shadcn_ui as ui

st.header("CheckBox")

checkbox_Value = [True,False,False]

checkbox_Value[0] = ui.checkbox(default_checked=True, label="I am a Checkbox 1")
checkbox_Value[1] = ui.checkbox(default_checked=False, label="I am a Checkbox 2")
checkbox_Value[2] = ui.checkbox(default_checked=False, label="I am a Checkbox 3")

st.markdown(f"""
+ checkbox 1 value: {checkbox_Value[0]}
+ checkbox 2 value: {checkbox_Value[1]}
+ checkbox 3 value: {checkbox_Value[2]}
""")
```