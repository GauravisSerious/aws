# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 2025

@author: Jai
"""

import streamlit as st

# Title of the app
st.title("BMI (Body Mass Index) Calculator")

# Sidebar header for input values
st.sidebar.header("Input your details")

# Function for user input
def user_input():
    # Taking height input from the user
    height = st.sidebar.number_input("Enter your height in meters", min_value=0.5, max_value=3.0, value=1.75, step=0.01)
    
    # Taking weight input from the user
    weight = st.sidebar.number_input("Enter your weight in kilograms", min_value=20, max_value=300, value=70, step=1)
    
    return height, weight

# Function to calculate BMI
def calculate_bmi(height, weight):
    # BMI formula
    bmi = weight / (height ** 2)
    return bmi

# Getting user input
height, weight = user_input()

# Calculate BMI based on user input
bmi = calculate_bmi(height, weight)

# Displaying BMI result
st.subheader(f"Your BMI is: {bmi:.2f}")

# Displaying BMI category
if bmi < 18.5:
    st.write("Category: Underweight")
elif 18.5 <= bmi < 24.9:
    st.write("Category: Normal weight")
elif 25 <= bmi < 29.9:
    st.write("Category: Overweight")
else:
    st.write("Category: Obesity")

# Optionally, display additional information about BMI ranges
st.write("""
### BMI Classification:
- Underweight: BMI < 18.5
- Normal weight: 18.5 ≤ BMI < 24.9
- Overweight: 25 ≤ BMI < 29.9
- Obesity: BMI ≥ 30
""")
