import streamlit as st

st.set_page_config(page_title="Right Sidebar Menu", layout="wide")

st.markdown("""
    <style>
    /* Main content style */
    .css-1v3fvcr {
        padding-left: 20%;
        padding-right: 20%;
    }

    /* Right sidebar container */
    .right-sidebar {
        position: fixed;
        top: 0;
        right: 0;
        height: 100%;
        width: 250px;
        background-color: #eee;
        padding: 20px;
        color: white;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }           

    /* Sidebar item */
    .sidebar-item {
        margin: 10px 0;
        padding: 10px;
        background-color: #eee;
        border-radius: 5px;
        text-align: left;
    }

    /* Sidebar item links */
    .sidebar-item a {
        color: white;
        text-decoration: none;
    }

    /* Sidebar item link hover effect */
    .sidebar-item a:hover {
        text-decoration: underline;
    }

    .timeline {
        display: flex;
        flex-direction: column;
        align-items: start;
        padding-bottom: 150px;
    }
    .timeline-item {
        display: flex;
        align-items: center;
        margin: 5px 0;
    }
    .circle {
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background-color: green;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        margin-right: 10px;
    }
    .line {
        width: 2px;
        height: 50px;
        background-color: black;
        margin-left: 9px;
    }
    div{
        color: black;    
    }

    </style>
    """, unsafe_allow_html=True)

st.write("Main content goes here.")

st.markdown("""
    <div class="right-sidebar">
        <div class="sidebar-item">
            <h3 style="font-size: 20px;">Logout</h3>
        </div>
        <div class="timeline">
        <div class="timeline-item">
            <div class="circle">✔</div>
            <div>Free form text</div>
        </div>
        <div class="line"></div>
        <div class="timeline-item">
            <div class="circle">✔</div>
            <div>Job Description<button>View</button></div>
        </div>
        <div class="line"></div>
        <div class="timeline-item">
            <div class="circle">✔</div>
            <div>Find Resource</div>
            </div>
        </div>
    <div class="bottom-menu">
        <div class="sidebar-item">
            <h3 style="font-size: 20px;">Settings</h3>
        </div>
        <div class="sidebar-item">
                <h3 style="font-size: 20px;">About Us</h3>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    r"""
    <style>
    .stDeployButton {
            visibility: hidden;
        }
    </style>
    """, unsafe_allow_html=True
)
