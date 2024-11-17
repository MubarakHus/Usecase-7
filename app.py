import streamlit as st
import requests

# Set up the Streamlit app
st.title("Players Clusters")
   
# User inputs
appearance = st.number_input("appearance", min_value=0, max_value=150, value=0)
minutes_played = st.number_input("minutes played", min_value=0, max_value=5000, value=0)
highest_value = st.number_input("highest_value", min_value=100000, max_value=5000000, value=100000)  # Add other types as necessary
price_category_encoded = st.selectbox("price_category", ["High_price", "Good_price", "Cheap_price"])  # Add other makes as needed

# Prediction button
if st.button("Predict"):
    # API request URL
    url = "https://usecase-7-cpsr.onrender.com/predict"
    
    if price_category_encoded == "High_price":
        price_category_encoded = 2
    elif price_category_encoded == "Good_price":
        price_category_encoded = 1
    else:
        price_category_encoded = 0
        
    # Data for the POST request
    data = {
        "appearance" : appearance,
        "minutes_played" : minutes_played,
        "highest_value" : highest_value,
        "price_category_encoded" : price_category_encoded
    }

    # Send the POST request
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Check for request errors
        prediction = response.json()  # Parse JSON response
        # {'Cheap_Price': 0, 'Good_Price': 1, 'High_Price': 2}            
        st.write(f"Estimated cluster: {prediction}")
    except requests.exceptions.RequestException as e:
        st.error("Error requesting prediction from API. Please try again.")
        st.write(e)