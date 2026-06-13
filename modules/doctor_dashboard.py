import streamlit as st
from database.db import conn
import pandas as pd

def show_doctor_dashboard():

    st.header("👨‍⚕️ Doctor Dashboard")

    cursor = conn.cursor()

    # Get patients
    patients = cursor.execute("SELECT * FROM patients").fetchall()

    if not patients:
        st.info("No patient records available")
        return

    df = pd.DataFrame(patients, columns=[
        "ID", "Name", "Age", "BP", "Sugar", "BMI", "Disease", "Risk"
    ])

    st.subheader("Patient Records")
    st.dataframe(df)

    st.subheader("High Risk Patients")

    high_risk = df[df["Risk"] == "High"]
    st.dataframe(high_risk)