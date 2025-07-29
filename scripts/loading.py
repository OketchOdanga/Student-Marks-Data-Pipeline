import csv
import sqlite3
import sqlite3

def load_data(csv_path, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        with open(csv_path, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Skip the header row
            for row in csv_reader:
                cursor.execute("""
                    INSERT OR IGNORE INTO marks (ROLL_NUMBER, Q1_5, Q2_5, Q3_5, Q4_5, Q5_5, Q6_5, Q7_5, Q8_5, Q9_5, Q10_5, Q11_5, Q12_5, Top9_out_of_45, TotalMarks_x_30)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """, row)
                cursor.execute("""
                    INSERT OR IGNORE INTO totalmarks (ROLL_NUMBER, Top9_out_of_45, TotalMarks_x_30)
                    VALUES (?,?,?)
                """, (row[0], row[13], row[14]))
        conn.commit()
        print("Data has been loaded into the database successfully.")
    except (sqlite3.Error, IOError) as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        conn.close()

# Example usage:
# load_data('./data/processed/marks_transformed.csv', 'student_marks.db')
""" if __name__ == '__main__':
    csv_path = './data/processed/marks_transformed.csv'
    db_path = 'student_marks.db'
    load_data(csv_path, db_path)
    print("Data loading script executed successfully.") """