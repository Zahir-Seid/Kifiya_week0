import pandas as pd
import streamlit as st

# Load dataset
try:
    data = pd.read_csv('data/cleaned_combined_data.csv')
except FileNotFoundError:
    st.error("Dataset not found! Ensure 'cleaned_combined_data.csv' is in the 'data/' directory.")
    st.stop()

# Streamlit app layout
st.title("Solar Data Dashboard")
st.sidebar.header("Filter Data")

# Location filter
location = st.sidebar.selectbox("Select Location", data['location'].unique())
filtered_data = data[data['location'] == location]

# Display filtered data
st.write(f"Showing data for: {location}")
st.dataframe(filtered_data)

# Visualizations
st.line_chart(filtered_data['GHI'])
st.bar_chart(filtered_data['DNI'])
