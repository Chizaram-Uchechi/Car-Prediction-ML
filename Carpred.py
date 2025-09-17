import streamlit as st
import pandas as pd
import joblib

# --- Page configuration (must be first Streamlit command)
st.set_page_config(
    page_title="Smart Car AutoPrice",
    layout="wide"
)

# --- Page title & intro
st.title("Smart Car AutoPrice")
st.markdown("### Let’s estimate the best selling price for your car.")

# --- Extra custom CSS (optional)
st.markdown("""
<style>
    /* page background override (dark greenish tone) */
    .stApp { background-color: #293636; }

    /* optional: custom font via Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap');
    html, body, [class*="st-"] {
        font-family: 'Lato', sans-serif;
    }

    /* About button styling */
    .about-btn {
        background: linear-gradient(135deg, #ffafbd, #c9a0dc);
        color: white;
        padding: 0.6em 1.2em;
        border: none;
        border-radius: 30px;
        font-weight: bold;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

# --- Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("packages/lr_car_pred_model.h5")

# --- User inputs
col1, col2 = st.columns(2)

with col1:
    present_price = st.number_input(
        "Current Price of the Car",
        min_value=2_000_000,
        step=1_000_000,
        format="%d"
    )
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])

with col2:
    seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

# --- Prediction button
if st.button("Predict Price"):
    model = load_model()

    # Encode categorical variables
    df = pd.DataFrame({
        "Present_Price": [present_price],
        "Fuel_Type_encoded": [ {"Petrol":0, "Diesel":1, "CNG":2}[fuel_type] ],
        "Seller_Type_encoded": [ {"Dealer":0, "Individual":1}[seller_type] ],
        "Transmission_encoded": [ {"Manual":0, "Automatic":1}[transmission] ]
    })

    # Predict
    selling_price = model.predict(df)[0]
    st.success(f"Selling Price: ₦ {selling_price:,.2f} naira")

# --- About section
with st.expander("ℹ️ About This App"):
    st.markdown("""
    **Smart Car AutoPrice**  

    This app uses a machine-learning regression model trained on
    historic car sales data to estimate a fair resale price.

    **How it works**
    1. Enter the current market price and car details.
    2. The algorithm weighs these features against market trends.
    3. You receive an evidence-based price estimate before you visit a dealer.
    """)
