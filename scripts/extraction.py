import pandas as pd

#extract data from the csv file
def extract_data_from_csv(file_path):
    df = pd.read_csv(file_path)
    return df 



# confirming if the data has been extracted succefully
if __name__ == '__main__':
    file_path = './data/raw/marks_final.csv'
    data = extract_data_from_csv(file_path)
    print(f"\nView of the top 5 rows:\n{data.head()}")
    print(f"\nView of the bottom 5 rows:\n{data.tail()}")
    print(f"\nSummary statistics:\n{data.describe()}")
