import streamlit as st
import sqlite3
import pandas as pd

def show_analytics():

    st.header("📊 Analytics Dashboard")

    conn = sqlite3.connect("healthcare.db")
    df = pd.read_sql_query("SELECT * FROM patients", conn)

    if df.empty:
        st.warning("No data available")
        return

    st.write(df)

    st.subheader("Disease Distribution")
    st.bar_chart(df["disease"].value_counts())

    st.subheader("Risk Levels")
    st.bar_chart(df["risk"].value_counts())

    conn.close()