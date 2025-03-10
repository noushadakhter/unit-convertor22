import streamlit as st
import pandas as pd

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .stApp {
            background-color: #f8f9fa;
            text-align: center;
        }
        .stTextInput, .stSelectbox, .stNumberInput {
            border-radius: 8px;
            border: 1px solid #ccc;
            padding: 10px;
            width: 80%;
        }
        .convert-btn {
            background-color: #00b4d8;
            color: white;
            border-radius: 8px;
            padding: 10px;
            font-size: 18px;
            border: none;
            cursor: pointer;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Unit conversion dictionary
unit_conversion = {
    "Length": {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701,
    },
    "Weight": {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1000000,  # 1 Kilogram = 1,000,000 Milligrams
        "Tola": 85.735,  # 1 Kilogram = 85.735 Tola
        "Pound": 2.20462,
        "Ounce": 35.274,
    },
    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K",
    }
}

def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        return value
    else:
        return value * (unit_conversion[category][to_unit] / unit_conversion[category][from_unit])

# Streamlit UI
st.title("Unit Converter using Python and Streamlit")
st.write("Easily convert between different units of length, weight, and temperature.")

category = st.selectbox("Choose Conversion Type", list(unit_conversion.keys()))
from_unit = st.selectbox("From", list(unit_conversion[category].keys()))
to_unit = st.selectbox("To", list(unit_conversion[category].keys()))
value = st.number_input("Enter Value", min_value=0.0, format="%.4f")

if st.button("Convert", key="convert-btn"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

st.markdown("<br><br><sub>Created with by Noushad Akhter</sub>", unsafe_allow_html=True)
