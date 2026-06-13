import streamlit as st

def show_treatment():
    st.header("💊 Treatment Recommendation Engine")

    disease = st.selectbox(
        "Select Disease",
        ["diabetes", "heart", "normal"]
    )

    if st.button("Get Recommendation"):

        if disease == "diabetes":
            st.success("👨‍⚕️ Specialist: Endocrinologist")
            st.info("Recommended Tests: HbA1c, Fasting Blood Sugar")
            st.write("Advice: Healthy diet and regular exercise.")

        elif disease == "heart":
            st.success("👨‍⚕️ Specialist: Cardiologist")
            st.info("Recommended Tests: ECG, Lipid Profile")
            st.write("Advice: Monitor blood pressure and reduce salt intake.")

        else:
            st.success("✅ No major disease risk detected.")
            st.write("Advice: Maintain a healthy lifestyle.")