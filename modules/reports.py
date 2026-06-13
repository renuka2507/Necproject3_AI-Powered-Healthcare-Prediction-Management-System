import streamlit as st
from database.db import conn

def show_reports():
    st.header("📄 Hospital Reports")

    cursor = conn.cursor()

    # Patients Count
    patient_count = cursor.execute(
        "SELECT COUNT(*) FROM patients"
    ).fetchone()[0]

    # Appointments Count
    appointment_count = cursor.execute(
        "SELECT COUNT(*) FROM appointments"
    ).fetchone()[0]

    # EHR Count
    ehr_count = cursor.execute(
        "SELECT COUNT(*) FROM ehr_records"
    ).fetchone()[0]

    st.subheader("📊 Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Patients", patient_count)

    with col2:
        st.metric("Appointments", appointment_count)

    with col3:
        st.metric("EHR Records", ehr_count)

    st.subheader("🦠 Disease Statistics")

    diseases = cursor.execute("""
        SELECT disease, COUNT(*)
        FROM patients
        GROUP BY disease
    """).fetchall()

    if diseases:
        st.bar_chart(
            {disease: count for disease, count in diseases}
        )
    else:
        st.info("No disease data available.")