import streamlit as st
import pandas as pd

def load_model():
    import joblib
    model = joblib.load('packages/lr_car_pred_model.h5')
    return model

st.header("Car prediction App")
st.subheader("Let's predict the selling price...")

with st.form("Car_form"):
    present_price = st.number_input("Enter Present Price of the car", min_value=0.0, step=1000.0)
    fuel_type = st.selectbox("Select Fuel Type", ["Petrol", "Diseal", "CNG"])
    seller_type = st.selectbox("Select Seller Type", ["Dealer", "Individual"])
    transmission = st.selectbox("Select Transmission Type", ["Manual", "Automatic"])

    submit_button = st.form_submit_button("Predict Price")

if submit_button:
    # Load the model
    model = load_model()

    # Create a DataFrame for the input data
    input_data = {
        'Present_Price': [present_price],
        'Fuel_Type': [fuel_type],
        'Seller_Type': [seller_type],
        'Transmission': [transmission]
    }
    df = pd.DataFrame(input_data)

    # Encode categorical variablses
    df["Transmission_encoded"] = df["Transmission"].map({"Manual":0, "Automatic":1})
    df["Seller_Type_encoded"] = df["Seller_Type"].map({"Dealer":0, "Individual":1})
    df["Fuel_Type_encodeded"] = df["Fuel_Type"].map({"Petrol":0, "Diesel":1,"CNG":2})
    x = df[["Present_Price","Fuel_Type_encodeded","Seller_Type_encoded","Transmission_encoded"]]
    st.write(x)
    # Predicting 
    selling_price = model.predict(x)
    st.write(f"Selling price: {round(selling_price[0],2)}")



 







 
