import streamlit as st
from auth.auth_service import login

st.set_page_config(page_title="AI Healthcare System", layout="wide")

# ---------------- LOGIN ----------------
login()

if "user" not in st.session_state:
    st.info("Please login to continue")
    st.stop()

role = st.session_state["role"]
user = st.session_state["user"]

# ---------------- HEADER ----------------
st.title("🏥 AI Healthcare System")
st.write(f"Welcome: {user} ({role})")

# ---------------- ROLE BASED MENU ----------------

if role == "Doctor":

    menu = st.sidebar.selectbox(
        "Doctor Menu",
        [
            "Dashboard",
            "Appointments",
            "Patient Records",
            "Disease Prediction",
            "Treatment Recommendation",
            "Outcome Prediction",
            "Reports",
            "Medical Report Analysis",
            "Bed Management"
        ]
    )

elif role == "Patient":

    menu = st.sidebar.selectbox(
        "Patient Menu",
        [
            "Dashboard",
            "Book Appointment",
            "My Appointments",
            "Disease Prediction",
            "My Reports",
            "AI Chatbot",
            "Medical Report Analysis",
            "Notifications"
        ]
    )

# ---------------- DASHBOARD ----------------
if menu == "Dashboard":
    st.header("📊 Dashboard")
    st.success("System running successfully")

# ---------------- DOCTOR MODULES ----------------
elif menu == "Appointments":
    from modules.appointment import show_appointments
    show_appointments()

elif menu == "Patient Records":
    from modules.ehr import show_ehr
    show_ehr()

elif menu == "Disease Prediction":
    from modules.prediction import show_prediction
    show_prediction()

elif menu == "Treatment Recommendation":
    from modules.treatment import show_treatment
    show_treatment()

elif menu == "Outcome Prediction":
    from modules.outcome import show_outcome
    show_outcome()

elif menu == "Reports":
    from modules.reports import show_reports
    show_reports()

elif menu == "Medical Report Analysis":
    from modules.medical_report import show_medical_report
    show_medical_report()

elif menu == "Bed Management":
    from modules.bed_management import show_bed_management
    show_bed_management()

# ---------------- PATIENT MODULES ----------------
elif menu == "Book Appointment":
    from modules.appointment import book_appointment
    book_appointment()

elif menu == "My Appointments":
    from modules.appointment import show_appointments
    show_appointments()

elif menu == "My Reports":
    from modules.reports import show_reports
    show_reports()

elif menu == "AI Chatbot":
    from modules.chatbot import show_chatbot
    show_chatbot()

elif menu == "Notifications":
    from modules.notifications import show_notifications
    show_notifications()