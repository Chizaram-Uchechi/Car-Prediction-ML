import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Smart Car AutoPrice",
    layout="wide"
)
st.title("Smart Car AutoPrice")
st.markdown("### Let’s estimate the best selling price for your car.")


st.markdown("""
<style>
    /* page background */
    .stApp { background-color: #293636; }
 </style> 
                       
<style>
html, body, [class*="st-"] {
    color: #FFFFFF !important;   /* all text to white */
}
</style>
""", unsafe_allow_html=True)  
            

st.markdown("<p class='custom-blue'></p>", unsafe_allow_html=True)

#[theme]
primaryColor="#293636"
backgroundColor="#0E0D0D"
secondaryBackgroundColor="#912065"
textColor="#ffffff"
font="sans-serif"

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

submit_button = ("Predict Price")


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
   


# ---- Top-right About button ----
about_css = """
<style>
/* container for the floating button */
#about-button-container {
    position: fixed;
    top: 1rem;          /* distance from top of page */
    right: 1rem;        /* distance from right edge */
    z-index: 9999;      /* keep it above other elements */
}
/* style the button itself */
#about-button-container button {
    background: linear-gradient(135deg, #ffafbd, #c9a0dc);
    color: white;
    padding: 0.6em 1.2em;
    border: none;
    border-radius: 30px;
    font-weight: bold;
    cursor: pointer;
}
</style>

<div id="about-button-container">
    <button onclick="window.dispatchEvent(new Event('about-click'))">
        ℹ️ About
    </button>
</div>
"""
st.markdown(about_css, unsafe_allow_html=True)

# Invisible streamlit listener for the custom click ----
clicked = st.session_state.get("about_clicked", False)

# small JS snippet to flip a Streamlit session variable when button clicked
st.markdown("""
<script>
window.addEventListener('about-click', () => {
    const streamlitEvent = new Event('streamlit:setComponentValue');
    window.dispatchEvent(streamlitEvent);
});
</script>
""", unsafe_allow_html=True)

# a simple toggle using Streamlit widgets:
show_about = st.checkbox("Show About", value=False, key="about_clicked",
                         label_visibility="hidden")

if show_about:
    with st.expander("About This App", expanded=True):
        st.markdown(
            """
            **Smart Car AutoPrice**  

            Uses a machine-learning regression model trained on historic
            car sales data to estimate a fair resale price.

            * Enter car details (Current price of the car, Seller Type, fuel type, Transmission.).
            * The algorithm weighs these features against market trends.
            * You get an evidence based price estimate before you visit a dealer.
            """
        )

st.set_page_config(
    page_title="Smart Car AutoPrice",
    layout="wide"
)
st.title("Smart Car AutoPrice")
st.markdown("### Let’s estimate the best selling price for your car.")


st.markdown("""
<style>
    /* page background */
    .stApp { background-color: #293636; }
 </style> 
                       
   <style> 
        
    h1, h2, h3, p {
        color: #ffffff;
    }
    .custom-white { color: white; important; }
</style>
""", unsafe_allow_html=True)
st.markdown("<p class='custom-blue'></p>", unsafe_allow_html=True)

#[theme]
primaryColor="#293636"
backgroundColor="#0E0D0D"
secondaryBackgroundColor="#912065"
textColor="#ffffff"
font="sans-serif"

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

submit_button = ("Predict Price")


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
   


# ---- Top-right About button ----
about_css = """
<style>
/* container for the floating button */
#about-button-container {
    position: fixed;
    top: 1rem;          /* distance from top of page */
    right: 1rem;        /* distance from right edge */
    z-index: 9999;      /* keep it above other elements */
}
/* style the button itself */
#about-button-container button {
    background: linear-gradient(135deg, #ffafbd, #c9a0dc);
    color: white;
    padding: 0.6em 1.2em;
    border: none;
    border-radius: 30px;
    font-weight: bold;
    cursor: pointer;
}
</style>

<div id="about-button-container">
    <button onclick="window.dispatchEvent(new Event('about-click'))">
        ℹ️ About
    </button>
</div>
"""
st.markdown(about_css, unsafe_allow_html=True)

# Invisible streamlit listener for the custom click ----
clicked = st.session_state.get("about_clicked", False)

# small JS snippet to flip a Streamlit session variable when button clicked
st.markdown("""
<script>
window.addEventListener('about-click', () => {
    const streamlitEvent = new Event('streamlit:setComponentValue');
    window.dispatchEvent(streamlitEvent);
});
</script>
""", unsafe_allow_html=True)

# a simple toggle using Streamlit widgets:
show_about = st.checkbox("Show About", value=False, key="about_clicked",
                         label_visibility="hidden")

if show_about:
    with st.expander("About This App", expanded=True):
        st.markdown(
            """
            **Smart Car AutoPrice**  

            Uses a machine-learning regression model trained on historic
            car sales data to estimate a fair resale price.

            * Enter car details (Current price of the car, Seller Type, fuel type, Transmission.).
            * The algorithm weighs these features against market trends.
            * You get an evidence based price estimate before you visit a dealer.
            """
        )

