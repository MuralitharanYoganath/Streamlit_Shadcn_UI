import streamlit as st
import pandas as pd
import requests

# Function to fetch data from the REST API
def fetch_data():
    url = 'http://127.0.0.1:8000/api/v1/candidate/'  # Replace with your REST API endpoint
    response = requests.get(url)
    data = response.json()  # Assuming the response is in JSON format
    return data

# Fetch data from the API
data = fetch_data()

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

# Display the table in Streamlit
st.title("Table from MongoDB via REST API")
st.table(df)