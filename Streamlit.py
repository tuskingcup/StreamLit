import streamlit as st
import joblib

# Step 11: Load the trained model
model = joblib.load('house_price_regression_model.joblib')

# Step 12: Create a Streamlit app
st.title("House Price Prediction")
st.write("Enter the number of bedrooms, bathrooms, and square footage to predict the house price.")

bedrooms = st.slider("Bedrooms", 1, 10, 3, 1)
bathrooms = st.slider("Bathrooms", 1, 10, 2, 1)
sqft_living = st.slider("Sqft Living", 500, 8000, 2000, 100)

if st.button("Predict"):
    # Prepare the input data for prediction
    input_data = [[bedrooms, bathrooms, sqft_living]]

    # Use the loaded model to make predictions
    predicted_price = model.predict(input_data)
    st.success(f"Predicted Price: ${predicted_price[0]:,.2f}")
