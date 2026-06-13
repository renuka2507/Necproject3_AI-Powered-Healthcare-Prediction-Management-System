import streamlit as st

def show_medical_report():
    st.header("📑 Medical Report Analysis")

    uploaded_file = st.file_uploader(
        "Upload Medical Report (.txt)",
        type=["txt"]
    )

    if uploaded_file is not None:

        content = uploaded_file.read().decode("utf-8")

        st.subheader("Report Content")
        st.text_area(
            "Medical Report",
            content,
            height=250
        )

        st.subheader("AI Analysis")

        findings = []

        text = content.lower()

        if "diabetes" in text:
            findings.append("🩸 Diabetes-related information detected.")

        if "heart" in text:
            findings.append("❤️ Cardiac-related information detected.")

        if "blood pressure" in text:
            findings.append("🩺 Blood pressure observations found.")

        if "kidney" in text:
            findings.append("🧬 Kidney-related information detected.")

        if findings:
            for item in findings:
                st.success(item)
        else:
            st.info("No major medical keywords detected.")