import streamlit as st
from database.db import conn

def show_alerts():

    st.header("🚨 Emergency Alert System")

    cursor = conn.cursor()

    data = cursor.execute("""
        SELECT * FROM patients WHERE risk = 'High'
    """).fetchall()

    if not data:
        st.success("No emergency cases 🚑")
        return

    st.error("⚠ High Risk Patients Detected!")

    for row in data:
        st.write(f"""
        🆔 ID: {row[0]}
        👤 Name: {row[1]}
        📊 Disease: {row[6]}
        ⚠ Risk: {row[7]}
        """)