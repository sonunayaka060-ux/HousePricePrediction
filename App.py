import streamlit as st
import pandas as pd
import joblib
st.set_page_config(page_title="House Price Prediction",page_icon="🏠",layout="wide")

st.title("🏠 Bengaluru House Price Prediction")
st.image("C:\\sonu nayaka\\ML project\\project\\house.jpg", width=230)

grid = joblib.load('rf_model.joblib')

location = st.selectbox( "Location", [ "Electronic City", "Whitefield", "Marathahalli", "Indiranagar", "HSR Layout" ])

sqft = st.number_input("Square Feet",min_value=300,max_value=10000,step=100,value=1500)

bath = st.selectbox("Bathrooms",[1, 2, 3, 4, 5])

bhk = st.selectbox("BHK", [1, 2, 3, 4, 5])

if st.button("Predict Price"):
    
    price = sqft * 6000

    st.success(f"Predicted Price: ₹ {price:,.0f}")