import streamlit as st
from database.db import conn

def show_ehr():

    st.header("🧾 Electronic Health Records (EHR)")

    role = st.session_state["role"]
    user = st.session_state["user"]

    cursor = conn.cursor()
    data = []

    # ---------------- DOCTOR VIEW ----------------
    if role == "Doctor":

        st.subheader("➕ Add Patient Record")

        # Get patient list
        cursor.execute("SELECT name FROM patients")
        patients_data = cursor.fetchall()
        patients = [row[0] for row in patients_data]

        if patients:
            patient = st.selectbox("Select Patient", patients)
        else:
            st.warning("No patients available")
            patient = None

        age = st.number_input("Age", min_value=0)
        blood_group = st.text_input("Blood Group")
        allergies = st.text_input("Allergies")
        medical_history = st.text_area("Medical History")
        treatments = st.text_area("Previous Treatments")

        if st.button("Save Record") and patient:

            cursor.execute("""
                INSERT INTO ehr_records 
                (patient, age, blood_group, allergies, medical_history, previous_treatments)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (patient, age, blood_group, allergies, medical_history, treatments))

            conn.commit()
            st.success("Record saved successfully!")

        st.divider()

        st.subheader("📋 All Patient Records")

        data = cursor.execute("SELECT * FROM ehr_records").fetchall()

    # ---------------- PATIENT VIEW ----------------
    elif role == "Patient":

        st.subheader("📋 My Medical Records")

        data = cursor.execute(
            "SELECT * FROM ehr_records WHERE patient=?",
            (user,)
        ).fetchall()

    else:
        st.info("No access")
        data = []

    # ---------------- DISPLAY ----------------
    if data:
        for row in data:
            st.write(f"🆔 ID: {row[0]}")
            st.write(f"👤 Patient: {row[1]}")
            st.write(f"🎂 Age: {row[2]}")
            st.write(f"🩸 Blood Group: {row[3]}")
            st.write(f"⚠️ Allergies: {row[4]}")
            st.write(f"📜 Medical History: {row[5]}")
            st.write(f"💊 Treatments: {row[6]}")
            st.divider()
    else:
        st.info("No records found.")