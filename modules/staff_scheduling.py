import streamlit as st
import pandas as pd

def show_staff_scheduling():
    st.header("👩‍⚕️ Staff Scheduling System")

    st.subheader("Assign Hospital Staff")

    staff_name = st.text_input("Staff Name")
    role = st.selectbox(
        "Role",
        ["Doctor", "Nurse", "Technician", "Receptionist"]
    )

    shift = st.selectbox(
        "Shift",
        ["Morning", "Afternoon", "Night"]
    )

    if "staff_schedule" not in st.session_state:
        st.session_state.staff_schedule = []

    if st.button("Assign Shift"):
        st.session_state.staff_schedule.append({
            "Staff Name": staff_name,
            "Role": role,
            "Shift": shift
        })

        st.success("Shift assigned successfully!")

    st.subheader("Current Schedule")

    if st.session_state.staff_schedule:
        df = pd.DataFrame(st.session_state.staff_schedule)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No staff schedules available.")