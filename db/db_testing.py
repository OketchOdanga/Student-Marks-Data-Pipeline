#this script is used to test if the data was loaded into the database successfully
import sqlite3
conn = sqlite3.connect('student_marks.db')
cursor = conn.cursor()
def test_data_loading():
    cursor.execute("SELECT COUNT(*) FROM marks")
    marks_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM totalmarks")
    totalmarks_count = cursor.fetchone()[0]
    
    if marks_count > 0 and totalmarks_count > 0:
        print(f"Data loaded successfully: {marks_count} records in 'marks' table, {totalmarks_count} records in 'totalmarks' table.")
    else:
        print("Data loading failed or no records found.")
    cursor.execute("SELECT * FROM marks LIMIT 5")
    marks_sample = cursor.fetchall()
    cursor.execute("SELECT * FROM totalmarks LIMIT 5")
    totalmarks_sample = cursor.fetchall()
    print("\nSample data from 'marks' table:")
    for row in marks_sample:
        print(row)
    print("\nSample data from 'totalmarks' table:")
    for row in totalmarks_sample:
        print(row)
    conn.close()
if __name__ == '__main__':
    test_data_loading()
    print("Test completed.")