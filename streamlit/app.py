import streamlit as st
import requests

# FastAPI endpoint
API_URL = 'http://127.0.0.1:8000/predict'

# Streamlit UI
st.title("Fraud Detection System")
st.write("Enter transaction details to predict if it's a fraud.")

tx_amount = st.number_input("Transaction Amount", min_value=0.0, format="%.2f")
tx_time_seconds = st.number_input("Transaction Time (Seconds)", min_value=0, help="The total of seconds since the first recorded transaction.")
tx_time_days = st.number_input("Transaction Time (Days)", min_value=0, help="The number of days since the first recorded transaction.")

if st.button("Check Fraud"):
    input_data = {
        'TX_AMOUNT': tx_amount,
        'TX_TIME_SECONDS': tx_time_seconds,
        'TX_TIME_DAYS': tx_time_days
    }

    # Send request to FastAPI
    response = requests.post(API_URL, json=input_data)
    
    if response.status_code == 200:
        result = response.json()['fraud_prediction']
        if result == 1:
            st.error("Fraud Detected!")
        else:
            st.success("Transaction is Legitimate.")
    else:
        st.warning("Error: Could not get a prediction.")
