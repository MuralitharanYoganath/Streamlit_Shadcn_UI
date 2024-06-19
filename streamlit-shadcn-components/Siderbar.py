import streamlit as st
from streamlit_option_menu import option_menu

# as sidebar menu
# with st.sidebar:
    # selected = option_menu(
        # menu_title= "Main Menu",
        # options=["Home","Project","Details"],
        # icons=["house", "book", "envelope"],
        # menu_icon="cast",
        # default_index=0,
    # )

# horizontal menu
selected = option_menu(
        menu_title= None,
        options=["Home","Project","Details"],
        icons=["house", "book", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color":"white"},
            "icon": {"color": "orgige", "font-size": "25px"},
            "nav-link": {
                "font-size": "25px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "green"},
        },
    )

if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Project":
    st.title(f"You have selected {selected}")
if selected == "Details":
    st.title(f"You have selected {selected}")


