from os import name

import streamlit as st  # pyright: ignore[reportMissingImports]

st.title("Telecommunication Customer Prediction System")

st.header("Powered by Ikechukwu ML")
st.write("This system predicts whether a telecommunication customer is likely to churn or not based on their usage patterns and demographic information. Please input the required data below to get a prediction.")
name = st.text_input("Enter your name:")
st.write(f'Welcome {name}')
gender = st.selectbox("Select your gender:", ["Male", "Female"])
usage_data = st.file_uploader("Upload your usage data (CSV format):", type=["csv"])  
terms_agreed = st.checkbox("I agree to the terms and conditions")
promotional_offers = st.radio("Do you want to receive promotional offers?", ["Yes", "No"])
age = st.slider('Select your age:', 18, 100, 25)
date = st.date_input("Select the date of prediction:")
time = st.time_input("Select the time of prediction:")
st.number_input("Enter your monthly bill amount:", min_value=0.0, step=0.01)
st.color_picker("Pick a color for the prediction result display:")

internet = st.selectbox("Select your internet usage level:", ["Low", "Medium", "High"])
birthday = st.date_input("Enter your birthday:")

st.button("Predict")
