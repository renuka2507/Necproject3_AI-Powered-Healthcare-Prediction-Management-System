import streamlit as st

def show_notifications():
    st.header("🔔 Notifications Center")

    notifications = [
        "📅 Appointment Reminder: John has an appointment at 10:00 AM.",
        "🚨 Emergency Alert: ICU Bed occupancy is above 90%.",
        "💊 Medication Reminder: Patient 102 medication due at 2:00 PM.",
        "📢 System Update: Daily reports generated successfully."
    ]

    st.subheader("Recent Notifications")

    for note in notifications:
        st.info(note)