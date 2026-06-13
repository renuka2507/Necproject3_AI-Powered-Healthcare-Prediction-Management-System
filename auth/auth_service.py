import streamlit as st

USERS = {
    "admin": {"password": "admin123", "role": "Admin"},
    "doctor": {"password": "doc123", "role": "Doctor"},
    "patient": {"password": "pat123", "role": "Patient"}
}

def login():

    if "user" in st.session_state:
        return

    st.sidebar.header("🔐 Login")

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):

        if username in USERS and USERS[username]["password"] == password:

            st.session_state["user"] = username
            st.session_state["role"] = USERS[username]["role"]

            st.success("Login successful")
            st.rerun()

        else:
            st.error("Invalid credentials")