import streamlit as st

def show_bed_management():
    st.header("🛏️ Bed Management System")

    total_beds = st.number_input(
        "Total Beds",
        min_value=1,
        value=100
    )

    occupied_beds = st.number_input(
        "Occupied Beds",
        min_value=0,
        max_value=total_beds,
        value=70
    )

    available_beds = total_beds - occupied_beds
    occupancy_rate = (occupied_beds / total_beds) * 100

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Beds", total_beds)

    with col2:
        st.metric("Occupied Beds", occupied_beds)

    with col3:
        st.metric("Available Beds", available_beds)

    st.progress(int(occupancy_rate / 100 * 100))

    st.info(f"Occupancy Rate: {occupancy_rate:.1f}%")

    if occupancy_rate >= 90:
        st.error("⚠️ Critical: Bed occupancy above 90%")
    elif occupancy_rate >= 75:
        st.warning("⚠️ High occupancy level")
    else:
        st.success("✅ Bed availability is healthy")