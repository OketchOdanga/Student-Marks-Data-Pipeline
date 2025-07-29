import logging
from scripts.extraction import extract_data_from_csv
from scripts.transformation import transform_quiz_data
from scripts.loading import load_data

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        # Step 1: Extract data
        raw_csv_path = './data/raw/marks_final.csv'
        data = extract_data_from_csv(raw_csv_path)
        logging.info("Data extracted successfully.")

        # Step 2: Transform data
        # The transformation function expects a file path, so we pass the raw CSV path
        transformed_data = transform_quiz_data(raw_csv_path)
        logging.info("Data transformed successfully.")

        # Step 3: Load data
        processed_csv_path = './data/processed/marks_transformed.csv'
        db_path = './db/student_marks.db'
        load_data(processed_csv_path, db_path)
        logging.info("Data loaded into the database successfully.")

    except Exception as e:
        logging.error(f"An error occurred in the pipeline: {e}")

if __name__ == '__main__':
    main()
    logging.info("Data pipeline execution completed.")