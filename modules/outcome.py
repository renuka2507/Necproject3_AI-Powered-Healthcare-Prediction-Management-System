import streamlit as st

def show_outcome():

    st.header("📈 Patient Outcome Prediction")

    age = st.number_input("Patient Age", 0, 120)
    bp = st.number_input("Blood Pressure")
    sugar = st.number_input("Sugar Level")
    bmi = st.number_input("BMI")

    if st.button("Predict Outcome"):

        # Simple rule-based logic
        if age > 65 or bp > 150 or sugar > 180:
            recovery = "60%"
            icu = "High"
            stay = "7–10 days"

        elif age > 45 or bp > 130 or sugar > 140:
            recovery = "80%"
            icu = "Medium"
            stay = "4–6 days"

        else:
            recovery = "95%"
            icu = "Low"
            stay = "1–3 days"

        st.success(f"Recovery Probability: {recovery}")
        st.warning(f"ICU Requirement Risk: {icu}")
        st.info(f"Expected Hospital Stay: {stay}")