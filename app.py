import streamlit as st
import pandas as pd
import pickle
from datetime import datetime, timedelta
st.set_page_config(
    page_title='Weekly Units Sold Forecast',
    page_icon='📊',
    layout='wide',
    initial_sidebar_state='collapsed')
st.markdown("""
    <style>
    /* Custom fonts */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

    /* Apply the custom font */
    html, body, [class*="css"]  {
        font-family: 'Roboto', sans-serif;
        background-color: #F8F4FF;  /* Set a soft light purple background color */  }

    /* Main title styling for containerized effect */
    .main-title-container {
        font-size: 42px;
        font-weight: 700;
        color: #4A235A;
        background: #F6F0FB;  /* Purple background for contrast */
        padding: 10px 30px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        width: auto;
        border: 2px solid #6C3483;
        margin: 20px auto;  /* Center with margin */
        text-align: center; }

    /* Adjusted header inside the input container */
    .input-header {
        font-size: 20px;
        font-weight: 500;
        color: #4A235A;
        background: #F6F0FB;  /* Purple background for contrast */
        padding: 10px 30px;
        border-radius: 15px;
        position: absolute;
        top: -50px;  /* Move the header up to overlap */
        left: 12%;   /* Center align relative to parent */
        transform: translateX(-50%);  /* Proper centering */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  /* Slight shadow */
        width: auto;  /* Adjust the width automatically */  }
    /* Customize input labels */
    .stDateInput > label, .stSelectbox > label {
        font-size: 35px;
        font-weight: bold;  /* Make labels bold */
        color: #4A235A;  /* Dark purple */
        margin-bottom: 10px;  }
    /* Styling for the input box (Date picker and select box) */
    .stDateInput > div, .stSelectbox > div {
        background-color: #F6F0FB;  /* Light purple background */
        border-radius: 10px;
        border: 3px solid #C39BD3;  /* Slightly darker purple border */  }

    /* Adjust the height of the input boxes */
    .stDateInput input, .stSelectbox div[data-baseweb="select"] {
        height: 40px;  /* Increase height for better visibility */  }

    /* Styling for the prediction result */
    .prediction-text {
        font-size: 28px;
        font-weight: 700;
        color: #E67E22;
        text-align: center;
        background-color: #F6F0FB;
        padding: 15px;
        border-radius: 15px;
        margin-top: 30px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);    }

    /* Button styling */
    .stButton>button {
        background-color: #6C3483;  /* Dark purple */
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: 600;    }
    /* Button hover effect */
    .stButton>button:hover {
        background-color: #501B70;  /* Darker purple on hover */
        transition: 0.3s;  }
    </style>
    """, unsafe_allow_html=True)
st.markdown('<div class="main-title-container">Weekly Units Forecast📊</div>', unsafe_allow_html=True)

# Center the image using Streamlit's columns
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image('Demand_Forecasting2.png', use_column_width=True, width=600)

st.markdown('<div class="input-container">', unsafe_allow_html=True)

# Create a header inside the container to make it appear inside the box
st.markdown('<div class="input-header">Enter the Forecasting Parameters</div>', unsafe_allow_html=True)

# Date picker for end date with a tooltip and bold label
end_date_input = st.date_input(
    'Select the end date of the next week: 📅',
    datetime.today() + timedelta(days=7),
    key='date_input',
    help='Choose the end date for the next week to generate the forecast.')
subcategory_mapping = {
    'ADULT CEREAL': 0,
    'FAMILY CEREAL': 1,
    'KIDS CEREAL': 2,
    'MOUTHWASH/RINSES AND SPRAYS': 3,
    'MOUTHWASHES (ANTISEPTIC)': 4,
    'PIZZA/PREMIUM': 5,
    'PRETZELS': 6}
subcategory_input = st.selectbox(
    'Select the Sub Category:📋 ',
    list(subcategory_mapping.keys()),
    key='subcategory_input',
    help='Choose the product subcategory to forecast the weekly units sold.')
predict_button = st.button('Predict Units📈 ')

st.markdown('</div>', unsafe_allow_html=True)

# Load the trained model
with open('model.pkl', 'rb') as pickle_in:
    model_xgb = pickle.load(pickle_in)
# Load data
weekly_data = pd.read_pickle('data.pkl')
# Map subcategory name to numerical code
subcategory_code = subcategory_mapping[subcategory_input]
# Perform the prediction when the "Predict" button is clicked
if predict_button:
    # Filter data for the selected subcategory code
    subcat_data = weekly_data[weekly_data['SUB_CATEGORY'] == subcategory_code]
    # Check if there is enough data
    if len(subcat_data) < 4:
        st.error('⚠️ Not enough data for this subcategory to make a prediction.')
    else:
        # Prepare features for prediction
        subcat_data = subcat_data.sort_values('WEEK_END_DATE')

        # Get the last weeks' data
        last_week_data = subcat_data.iloc[-1]
        second_last_week_data = subcat_data.iloc[-2]

        # Calculate features
        lag_1_week_units = last_week_data['UNITS']
        lag_2_week_units = second_last_week_data['UNITS']
        rolling_mean_4_weeks = subcat_data['UNITS'].rolling(window=4).mean().iloc[-1]
        week_over_week_diff = lag_1_week_units - lag_2_week_units
        percentage_change = (
            (week_over_week_diff / lag_2_week_units) if lag_2_week_units != 0 else 0    )
    
        new_data = {
            'SUB_CATEGORY': subcategory_code,
            'year': end_date_input.year,
            'month': end_date_input.month,
            'day': end_date_input.day,
            'week': end_date_input.isocalendar()[1],
            'quarter': (end_date_input.month - 1) // 3 + 1,
            'lag_1_week_units': lag_1_week_units,
            'lag_2_week_units': lag_2_week_units,
            'rolling_mean_4_weeks': rolling_mean_4_weeks,
            'week_over_week_diff': week_over_week_diff,
            'percentage_change': percentage_change   }
        # Convert to DataFrame
        input_df = pd.DataFrame([new_data])
        prediction = model_xgb.predict(input_df)
        predicted_units = int(round(prediction[0]))
        # Display the prediction with styling
        st.markdown(
            f'<div class="prediction-text"> Predicted Units for <strong>{subcategory_input}</strong>: {predicted_units} units 🔮</div>',
            unsafe_allow_html=True  )
