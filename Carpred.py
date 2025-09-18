import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Smart Car AutoPrice",
    page_icon="🚗",
    layout="wide"
)

st.title("Smart Car AutoPrice")
st.markdown("### Let’s estimate the best selling price for your car.")

# ---- Global styles: font + background colour ----
st.markdown("""
<style>
/* Apply font everywhere */
html, body, [class*="st-"] {
    font-family: 'Lato', sans-serif;
}

/* Set a dark background and white text */
.stApp {
    background-color: #293636;      /* ← change hex to any colour you like */
    color: white;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>
/* Apply it to the whole app */
html, body, [class*="st-"] {
    font-family: 'Lato', sans-serif;
}
</style>
""", unsafe_allow_html=True)


def load_model():
    import joblib
    model = joblib.load('packages/lr_car_pred_model.h5')
    return model


col1, col2 = st.columns(2)

with col1:
    present_price = st.number_input("Current Price of the Car", min_value=2000000, step=1000000)
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])

with col2:
    seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

submit_button = st.button("Predict Price")

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
    X = df[["Present_Price","Fuel_Type_encodeded","Seller_Type_encoded","Transmission_encoded"]]
    st.write(X)
    # Predicting 
    selling_price = model.predict(X)
    st.success(f" Selling Price: ₦ {selling_price[0]:,.2f} naira")
   


#  About section 
#  A toggle to show/hide the About information
show_about = st.checkbox("ℹ️ About", value=False)

if show_about:
    st.markdown("""
   **Smart Car AutoPrice**

    Uses a machine-learning regression model trained on historic
    car-sales data to estimate a fair resale price.

    * Enter car details (Current price of the car, Seller Type, fuel type, Transmission).
    * The algorithm weighs these features against market trends.
    * You get an evidence-based price estimate before you visit a dealer.
    """)













