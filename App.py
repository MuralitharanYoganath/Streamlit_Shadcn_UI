import streamlit as st
import requests
from pymongo import MongoClient
from streamlit_modal import Modal

# MongoDB configuration
MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)
db = client["recruiter_ai"]
collection = db["job_descriptions"]

# Streamlit configuration
st.set_page_config(page_title="Recruiter AI")

# Initialize modal for job description viewing/editing
modal = Modal("Job Description", key="job_description_modal", max_width=600, padding=10)

# CSS for modal content customization
modal_css = """
<style>
    .modal-content {
        height: 90vh;  /* Adjust the height as needed */
        overflow-y: auto; /* Ensure the modal content is scrollable */
    }
</style>
"""
st.markdown(modal_css, unsafe_allow_html=True)

# Initialize session state variables
if 'job_description' not in st.session_state:
    st.session_state['job_description'] = ""
    st.session_state['disable_text_area'] = False
if 'current_job_description' not in st.session_state:
    st.session_state['current_job_description'] = ""
if 'selected_job_id' not in st.session_state:
    st.session_state['selected_job_id'] = None
if 'modal_open' not in st.session_state:
    st.session_state['modal_open'] = False
if 'unsaved_changes' not in st.session_state:
    st.session_state['unsaved_changes'] = False
if 'modal_content' not in st.session_state:
    st.session_state['modal_content'] = ""
if 'edit_mode' not in st.session_state:
    st.session_state['edit_mode'] = False

# Function to fetch job descriptions from MongoDB
def fetch_job_descriptions():
    return list(collection.find({}, {"_id": 1, "prompt": 1, "job_description": 1}))

# Function to handle New Job Description button
def new_job_description():
    st.session_state['current_job_description'] = ""
    st.session_state['selected_job_id'] = None
    st.session_state['disable_text_area'] = False

# Function to handle submit action
def submit_job_description():
    if 'job_description' in st.session_state and st.session_state['job_description'].strip():
        job_description = st.session_state['job_description']
        # API endpoint
        api_url = "http://localhost:8000/api/v1/jd"
        # Payload to send to the API
        payload = {"prompt": job_description}
        # Make the POST request
        response = requests.post(api_url, json=payload)
        if response.status_code == 201:
            # Parse the response
            jd_response = response.json()
            # Extract the job ID, prompt, and job description
            job_id = jd_response.get("id")
            prompt_saved = job_description
            job_description_created = jd_response.get("job_description")
            if job_id and job_description_created:
                # Store job ID, prompt, and job description in MongoDB
                collection.insert_one({"_id": job_id, "prompt": prompt_saved, "job_description": job_description_created})
                # Update session state to select the newly created job
                st.session_state['selected_job_id'] = job_id
                st.session_state['current_job_description'] = prompt_saved
                # Display success message
                st.success(f"Job description created successfully with Job ID: {job_id}")
                # Disable the text area after submission
                st.session_state['disable_text_area'] = True
                # Update job descriptions in sidebar
                st.experimental_rerun()
            else:
                st.error("Failed to retrieve job ID or job description from response.")
        else:
            st.error("Failed to create job description. Please try again.")
    else:
        st.warning("Please enter a job description before submitting.")

# Function to handle update action
def update_job_description():
    try:
        if st.session_state['selected_job_id'] is not None:
            api_url = f"http://localhost:8000/api/v1/jd/{st.session_state['selected_job_id']}"
            job_description = st.session_state['modal_content'] if st.session_state['modal_open'] else st.session_state['job_description']
            payload = {"job_description": job_description}
            response = requests.put(api_url, json=payload)
            if response.status_code == 200:
                st.success("Job description updated successfully.")
                # Update MongoDB document with the new job description
                collection.update_one({"_id": st.session_state['selected_job_id']}, {"$set": {"job_description": job_description}})
                st.session_state['modal_open'] = False
                st.experimental_rerun()
            else:
                st.error("Failed to update job description. Please try again.")
        else:
            st.error("No job description selected.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error during the request: {e}")

# Function to display candidates table
def show_candidates_table(candidates):
    st.write("### Candidates")
    # Create table headers
    st.write(
        "| Select | Name | Email | Job ID | Mobile No | Status |",
        "|--------|------|-------|--------|------------|--------|"
    )
    # Populate table rows
    for candidate in candidates:
        checkbox_id = f"checkbox_{candidate['id']}"
        is_checked = st.checkbox("", key=checkbox_id)
        st.write(
            f"| {is_checked} | {candidate['name']} | {candidate['email']} | {candidate['job_id']} | {candidate['mobile_no']} | {candidate['status']} |"
        )

# Sidebar
with st.sidebar:
    st.sidebar.markdown("### Saved Job Descriptions")
    # Fetch job descriptions from MongoDB
    job_descriptions = fetch_job_descriptions()
    # Display existing job descriptions as clickable links
    for job in job_descriptions:
        if st.sidebar.button(f"Job ID: {job['_id']}"):
            st.session_state['selected_job_id'] = job['_id']
            st.session_state['current_job_description'] = job['prompt']
            st.session_state['disable_text_area'] = True
    # New Job Description button
    if st.sidebar.button("New Job Description"):
        new_job_description()
    # Edit Job Description button
    if st.sidebar.button("Edit Job Description"):
        st.session_state['disable_text_area'] = False
        st.session_state['edit_mode'] = True

# Main job description input area
if st.session_state['disable_text_area']:
    st.text_area("Describe the Job Profile", value=st.session_state['current_job_description'], disabled=True, key="desc_disabled")
else:
    job_description = st.text_area("Describe the Job Profile", value=st.session_state['current_job_description'], key="job_desc")
    st.session_state['unsaved_changes'] = job_description != st.session_state['current_job_description']

# Create columns for buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.session_state['edit_mode']:
        # Update button for editing mode
        if st.button("Update", key="update_button"):
            update_job_description()
    else:
        # Submit button for new job description
        if st.button("Submit", key="submit_button"):
            submit_job_description()

with col2:
    # View Job Description button
    if st.button("View Job Description", key="view_button"):
        try:
            if st.session_state['selected_job_id'] is not None:
                # API endpoint for fetching the job description
                api_url = f"http://localhost:8000/api/v1/jd/{st.session_state['selected_job_id']}"
                # Make the GET request
                response = requests.get(api_url)
                if response.status_code == 200:
                    # Parse the response
                    jd_response = response.json()
                    # Display the job description in a modal
                    if 'job_description' in jd_response:
                        st.session_state['modal_open'] = True
                        st.session_state['modal_content'] = jd_response['job_description']
                        modal.open()
                    else:
                        st.error("Job description field not found in the response.")
                else:
                    st.error("Failed to fetch job description. Please try again.")
            else:
                st.warning("No job description selected.")
        except requests.exceptions.RequestException as e:
            st.error(f"Error during the request: {e}")

with col3:
    # View Candidates button
    view_candidates_key = "view_candidates_button"
    if st.button("View Candidates", key=view_candidates_key):
        try:
            if st.session_state['selected_job_id'] is not None:
                # API endpoint for fetching the candidates
                api_url = f"http://localhost:8000/api/v1/candidates/{st.session_state['selected_job_id']}"
                # Make the GET request
                response = requests.get(api_url)
                if response.status_code == 200:
                    # Parse the response
                    candidates_response = response.json()
                    # Display the candidates in a table
                    if 'candidates' in candidates_response:
                        show_candidates_table(candidates_response['candidates'])
                    else:
                        st.error("Candidates field not found in the response.")
                else:
                    st.error("Failed to fetch candidates. Please try again.")
            else:
                st.warning("No job description selected.")
        except requests.exceptions.RequestException as e:
            st.error(f"Error during the request: {e}")

# Modal for viewing and editing job description
if modal.is_open():
    with modal.container():
        edited_job_description = st.text_area("Edit Job Description", value=st.session_state['modal_content'], key="modal_desc")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Save Edit", key="save_edit_button"):
                st.session_state['modal_content'] = edited_job_description
        with col2:
            if st.button("Update", key="modal_update_button"):
                update_job_description()
