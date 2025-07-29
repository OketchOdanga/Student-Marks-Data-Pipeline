import sqlite3

conn = sqlite3.connect('student_marks.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS marks (
    ROLL_NUMBER INTEGER PRIMARY KEY,
    Q1_5 INTEGER,
    Q2_5 INTEGER,
    Q3_5 INTEGER,
    Q4_5 INTEGER,
    Q5_5 INTEGER,
    Q6_5 INTEGER,
    Q7_5 INTEGER,
    Q8_5 INTEGER,
    Q9_5 INTEGER,
    Q10_5 INTEGER,
    Q11_5 INTEGER,
    Q12_5 INTEGER,
    Top9_out_of_45 FLOAT,
    TotalMarks_x_30 FLOAT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS totalmarks (
    ROLL_NUMBER INTEGER PRIMARY KEY,
    Top9_out_of_45 FLOAT,
    TotalMarks_x_30 FLOAT
)
""")
conn.commit()
conn.close()    
print("Database and tables created successfully.")
