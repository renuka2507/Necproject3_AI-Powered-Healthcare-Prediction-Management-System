import streamlit as st
from database.db import conn

def book_appointment():

    st.header("📅 Book Appointment")

    cursor = conn.cursor()
    user = st.session_state["user"]

    doctor = st.text_input("Doctor Name")
    date = st.date_input("Date")
    time = st.time_input("Time")
    reason = st.text_area("Reason")

    if st.button("Book Now"):

        cursor.execute("""
            INSERT INTO appointments (patient, doctor, appointment_date, reason)
            VALUES (?, ?, ?, ?)
        """, (user, doctor, f"{date} {time}", reason))

        conn.commit()
        st.success("Appointment booked successfully!")