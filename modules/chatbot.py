import streamlit as st

def show_chatbot():
    st.header("🤖 AI Healthcare Chatbot")

    user_message = st.text_input("Ask your health question:")

    if user_message:

        message = user_message.lower()

        if "fever" in message:
            response = (
                "You may have an infection. Stay hydrated and consult a physician if symptoms persist."
            )

        elif "diabetes" in message:
            response = (
                "Monitor your blood sugar regularly and follow your doctor's advice."
            )

        elif "heart" in message:
            response = (
                "Maintain a healthy lifestyle and consult a cardiologist if you have chest pain."
            )

        elif "appointment" in message:
            response = (
                "You can book appointments through the Appointment module."
            )

        else:
            response = (
                "I'm a healthcare assistant. Please consult a doctor for an accurate diagnosis."
            )

        st.success(f"Chatbot: {response}")