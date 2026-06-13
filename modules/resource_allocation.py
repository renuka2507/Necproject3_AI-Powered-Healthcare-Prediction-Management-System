import streamlit as st
import pandas as pd

def show_resource_allocation():
    st.header("📦 Resource Allocation System")

    resource = st.selectbox(
        "Select Resource",
        [
            "Ventilator",
            "Oxygen Cylinder",
            "PPE Kit",
            "Ambulance"
        ]
    )

    quantity = st.number_input(
        "Available Quantity",
        min_value=0,
        value=10
    )

    if "resources" not in st.session_state:
        st.session_state.resources = []

    if st.button("Allocate Resource"):

        st.session_state.resources.append({
            "Resource": resource,
            "Quantity": quantity
        })

        st.success(f"{resource} allocated successfully!")

    st.subheader("Allocated Resources")

    if st.session_state.resources:
        df = pd.DataFrame(st.session_state.resources)
        st.dataframe(df, use_container_width=True)

        total = df["Quantity"].sum()
        st.metric("Total Resources Tracked", total)

    else:
        st.info("No resources allocated yet.")