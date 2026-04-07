import pickle 
import streamlit as st 
import pandas as pd 
import numpy as np 
from sklearn.preprocessing import OneHotEncoder 
from catboost import CatBoostRegressor 




# page config 

st.set_page_config(
    page_title='Second hand Car Price Prediction' , 
    page_icon="🚗",
    layout="centered",
)

# custom CSS 
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@300;400;500&display=swap');
 
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
 
h1, h2, h3 {
    font-family: 'Syne', sans-serif !important;
}
 
.stApp {
    background: #0d0d0d;
    color: #f0ece4;
}
 
/* Card container */
.card {
    background: #161616;
    border: 1px solid #2a2a2a;
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 1.5rem;
}
 
/* Result box */
.result-success {
    background: linear-gradient(135deg, #1a2e1a, #0d1a0d);
    border: 1px solid #2d6a2d;
    border-radius: 12px;
    padding: 1.5rem 2rem;
    text-align: center;
    margin-top: 1rem;
}
 
.result-success .price {
    font-family: 'Syne', sans-serif;
    font-size: 2.8rem;
    font-weight: 800;
    color: #5dde5d;
    letter-spacing: -1px;
}
 
.result-success .label {
    font-size: 0.85rem;
    color: #7a9a7a;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 0.5rem;
}
 
.result-error {
    background: linear-gradient(135deg, #2e1a1a, #1a0d0d);
    border: 1px solid #6a2d2d;
    border-radius: 12px;
    padding: 1.5rem 2rem;
    text-align: center;
    margin-top: 1rem;
    color: #de5d5d;
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
}
 
/* Override Streamlit widget labels */
label, .stSelectbox label, .stNumberInput label, .stSlider label {
    color: #a09a90 !important;
    font-size: 0.78rem !important;
    text-transform: uppercase !important;
    letter-spacing: 1.5px !important;
    font-weight: 500 !important;
}
 
/* Inputs */
input, select, .stSelectbox > div > div {
    background: #1e1e1e !important;
    border-color: #333 !important;
    color: #f0ece4 !important;
    border-radius: 8px !important;
}
 
/* Button */
.stButton > button {
    background: #f0ece4;
    color: #0d0d0d;
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 1rem;
    letter-spacing: 1px;
    border: none;
    border-radius: 10px;
    padding: 0.75rem 2.5rem;
    width: 100%;
    transition: all 0.2s ease;
}
.stButton > button:hover {
    background: #5dde5d;
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(93, 222, 93, 0.25);
}
 
/* Divider */
hr {
    border-color: #2a2a2a;
    margin: 1.5rem 0;
}
</style>
""", unsafe_allow_html=True) 

# load model 

@st.cache_resource  # ====>used when use ML models 
def load_model(): 
    model = pickle.load(open('models/Model.pkl' , 'rb')) 
    brand_encoder = pickle.load(open('models/Brand_Encoder.pkl' , 'rb'))
    model_encoder = pickle.load(open('models/Model_Encoder.pkl' , 'rb')) 
    brand_encoder = pickle.load(open('models/Brand_Encoder.pkl' , 'rb'))
    ohe_encoder = pickle.load(open('models/OHE_Encoder.pkl' , 'rb'))  
    return model , brand_encoder , model_encoder , ohe_encoder 



model  , brand_encoder , model_encoder , ohe_encoder = load_model()

# header 

st.markdown("""
<div style="text-align:center; padding: 2rem 0 1rem;">
    <div style="font-size:3rem; margin-bottom:0.25rem;">🚗</div>
    <h1 style="font-size:2.6rem; font-weight:800; margin:0; letter-spacing:-1px;">
        Car Price Predictor
    </h1>
    <p style="color:#7a7a7a; margin-top:0.5rem; font-size:0.95rem;">
        Enter your car details below to get an instant market estimate.
    </p>
</div>
""", unsafe_allow_html=True)

st.divider() 
# read data frame to aggregate data 
@st.cache_data 
def load_data() : 
    df = pd.read_excel('data/raw_data.xlsx')
    return df 

df = load_data() 
@st.cache_data
def get_brands_models() :
    brand_to_models = df.groupby("Brand")["Model"].unique().apply(list).to_dict() 
    return brand_to_models 

brand_to_models = get_brands_models() 
@st.cache_data
def get_brand_list(): 
    brands_list = sorted(brand_to_models.keys())
    return brands_list 
brands_list = get_brand_list()
# start Bulid Form 

col1 , col2 = st.columns(2) 

with col1: 
    Brand = st.selectbox("Brand", brands_list) 
    Fuel = st.selectbox("Fuel Type",['Hybrid', 'Electric', 'Diesel', 'Petrol'])
    Year         = st.number_input("Year", min_value=1990, max_value=2025, value=2018, step=1)
    Mileage      = st.number_input("Mileage (km)", min_value=0, value=50000, step=1000)
    Doors        = st.number_input("Number of Doors", min_value=2, max_value=5, value=4, step=1)


with col2: 
    models_list = brand_to_models.get(Brand, []) 
    CarModel = st.selectbox("Model", models_list)
    Transmission = st.selectbox("Transmission", ["Manual", "Automatic", "Semi-Automatic"])
    EngineSize   = st.number_input("Engine Size (L)", min_value=0.5, max_value=8.0, value=1.6, step=0.1, format="%.1f")
    OwnerCount   = st.number_input("Number of Previous Owners", min_value=0, max_value=20, value=1, step=1)

st.write("")
predict_btn = st.button("⚡  Estimate Price")

# Prediction Logic 
if predict_btn:
    if not Brand or not CarModel: 
        st.warning("Please fill in both **Brand** and **Model** fields.")
    else : 
        input_df = pd.DataFrame({
            'Brand':        [Brand],
            'Model':        [CarModel],
            'Year':         [Year],
            'EngineSize':   [EngineSize],
            'Fuel':         [Fuel],
            'Transmission': [Transmission],
            'Mileage':      [Mileage],
            'Doors':        [Doors],
            'OwnerCount':   [OwnerCount],
        })
         
        input_df['Encoded_Brand'] = input_df['Brand'].map(brand_encoder)
        input_df['Encoded_Model'] = input_df['Model'].map(model_encoder)
        input_df['Encoded_Brand'].fillna(input_df['Encoded_Brand'].mean(), inplace=True)
        input_df['Encoded_Model'].fillna(input_df['Encoded_Model'].mean(), inplace=True)
        input_df.drop(['Brand', 'Model'], axis=1, inplace=True)



        # One-hot encode Fuel and Transmission
        categorical_cols = ['Fuel', 'Transmission']
        encoded_array = ohe_encoder.transform(input_df[categorical_cols])
        encoded_df = pd.DataFrame(encoded_array, columns=ohe_encoder.get_feature_names_out(categorical_cols))
        
        # Merge encoded columns with input data
        input_df_encoded = input_df.drop(columns=categorical_cols).reset_index(drop=True)
        input_data = pd.concat([input_df_encoded, encoded_df], axis=1)
        
        # Make prediction
        prediction = model.predict(input_data)
        output = round(prediction[0], 2)




        if output < 0:
            st.markdown("""
            <div class="result-error">
                ⚠️ Sorry, we can't estimate a positive value for this car.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-success">
                <div class="label">Estimated Market Value</div>
                <div class="price">$ {output:,.2f}</div>
            </div>
            """, unsafe_allow_html=True)
 

