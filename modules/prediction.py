import streamlit as st
from ml.predict import predict_disease
from database.db import conn

def show_prediction():

    st.header("🧠 Disease Prediction AI")

    age = st.number_input("Age")
    bp = st.number_input("Blood Pressure")
    sugar = st.number_input("Sugar Level")
    bmi = st.number_input("BMI")

    if st.button("Predict"):
        result = predict_disease(age, bp, sugar, bmi)

        st.success(f"Disease: {result['disease']}")
        st.warning(f"Risk: {result['risk']}")

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO patients(name, age, bp, sugar, bmi, disease, risk)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, ("user", age, bp, sugar, bmi, result["disease"], result["risk"]))

        conn.commit()

        st.info("Saved to database")