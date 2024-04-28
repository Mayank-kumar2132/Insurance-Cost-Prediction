import streamlit as st
import joblib

def main():
    title_color = "#007acc"
    st.markdown(
    f"""
    <h1 style='color:{title_color}; text-align:center;'>Health Insurance Price Prediction using Machine Learning</h1>
    """,
    unsafe_allow_html=True)
    model = joblib.load("C:/Users/MAYANK KUMAR/OneDrive/Desktop/OneDrive - K.R. MANGALAM UNIVERSITY/PROJECT/Bank_churn/Health insurance cost prediction/model_joblib_gr")
    p1 = st.slider("Enter Your Age", 18, 100)



