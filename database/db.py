
import sqlite3

# Connect to database
conn = sqlite3.connect("healthcare.db", check_same_thread=False)
cursor = conn.cursor()

# ---------------- PATIENTS TABLE ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    bp REAL,
    sugar REAL,
    bmi REAL,
    disease TEXT,
    risk TEXT
)
""")

# ---------------- APPOINTMENTS TABLE ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient TEXT,
    doctor TEXT,
    appointment_date TEXT,
    reason TEXT
)
""")

# ---------------- EHR TABLE ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS ehr_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient TEXT,
    age INTEGER,
    blood_group TEXT,
    allergies TEXT,
    medical_history TEXT,
    previous_treatments TEXT
)
""")

conn.commit()