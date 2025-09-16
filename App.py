import streamlit as st
import pandas as pd
import os



def load_model():
    import joblib
    model = joblib.load('packages/lr_car_pred_model.h5')
    return model


st.header("Car Prediction App")
st.subheader("Let's predict the selling price....")

with st.form("car_form"):
    Present_Price = st.number_input("Enter present price of the car", min_value=0.0, step=1000.0)
    fuel_type = st.selectbox("Select Fuel Type", ["Petrol", "Diesel", "CNG"])
    seller_type = st.selectbox("Select Seller Type", ["Dealer", "Individual"])
    Transmission = st.selectbox("Select Transmission Type", ["Manual", "Automatic"])

    Submit_button = st.form_submit_button("Predict Price")

if Submit_button:
    #load the model
    model = load_model()

    # Create a Dataframe for the input data
    input_data = {
        'Predict_Price': [Present_Price],
        'Fuel_Type': [Fuel_Type],
        'Seller_Type': [seller_type],
        'Transmission': [Transmission]
    }
    df=pd.Dataframe(input_data)


    df["Transmission_encode"]= df["Transmission"].map({'Manual': 0, 'Automatic': 1})
    df["Seller_type_encode"]= df["Seller_Type"].map({'  Dealer': 0, 'Individual': 1})
    df["Fuel_type_encode"]= df["Fuel_Type"].map({'Petrol': 0, 'Diesel': 1, 'CNG': 2})
    X =df[["Present_Price", 'Fuel_type_encode', 'Seller_type_encode', 'Transmission_encode']]

    # Predicting
    selling_price = model.predict(X)
    st.write(f"selling_price: {seller_price}")