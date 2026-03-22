
import streamlit as st
import requests

st.title("Customer Subscription Prediction") # Title for the subscription prediction app

# Input fields for the features expected by the backend API
month_options = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
day_of_week_options = ['mon', 'tue', 'wed', 'thu', 'fri']
job_options = ['admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed', 'unknown']
housing_options = ['yes', 'no', 'unknown']
loan_options = ['yes', 'no', 'unknown']

month = st.selectbox("Month of Last Contact", month_options)
day_of_week = st.selectbox("Day of Week of Last Contact", day_of_week_options)
duration = st.number_input("Last Contact Duration (seconds)", min_value=0, value=100)
job = st.selectbox("Job Type", job_options)
housing = st.selectbox("Has Housing Loan?", housing_options)
loan = st.selectbox("Has Personal Loan?", loan_options)

# Prepare data for API request
prediction_data = {
    "Month": month,
    "Day_of_Week": day_of_week,
    "Duration": duration,
    "job": job,
    "housing": housing,
    "loan": loan
}

if st.button("Predict Subscription", type='primary'):
    # IMPORTANT: Replace <user_name> and <space_name> with your Hugging Face username and backend space name
    # The repo_id for the backend is dcsamuel/SuperMarketing
    api_endpoint = "https://dcsamuel-SuperMarketing.hf.space/v1/predict"

    response = requests.post(api_endpoint, json=prediction_data)

    if response.status_code == 200:
        result = response.json()
        prediction = result["Subscription"]

        if prediction == 1:
            st.success("**Prediction: The customer will likely subscribe!**")
        else:
            st.info("**Prediction: The customer will likely NOT subscribe.**")

    else:
        st.error(f"Error in API request: {response.status_code} - {response.text}")
        st.write("Please ensure the backend API is running and accessible.")
