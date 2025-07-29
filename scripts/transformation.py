import pandas as pd

def transform_quiz_data(file_path):
    # Load the data
    data = pd.read_csv(file_path)
    # Transform the data
    # Rename the column 'Out of 30' to 'Total Marks(x/30)'
    data.rename(columns={'Out of 30':'Total Marks(x/30)'}, inplace=True)
    data.isnull().sum()
    # Fill NaN values with 0
    data.fillna(0, inplace=True)
    # Remove SNO column
    if 'SNO.' in data.columns:
        data.drop(columns=['SNO.'], inplace=True)

    # convert AB values to 0
    data.replace({'AB': 0}, inplace=True)
    # Check if the 'ROLL NUMBER' column valus are unique
    if data['ROLL NUMBER'].is_unique:
        print("ROLL NUMBER values are unique.")
    else:
        #remove duplicates
        data.drop_duplicates(subset=['ROLL NUMBER'], inplace=True)
        data.reset_index(drop=True, inplace=True)
        print("Duplicates found and removed.")
        # Check again if the 'ROLL NUMBER' column values are unique
        if data['ROLL NUMBER'].is_unique:
            print("ROLL NUMBER values are now unique after removing duplicates.")
        else:
            print("ROLL NUMBER values are not unique. Please check the data.")
    # save transformed data to a new CSV file
    data.to_csv('./data/processed/marks_transformed.csv', index=False)
    print("Data has been transformed and saved to './data/processed/marks_transformed.csv'")
    # Return the transformed data      
    return data 
""" 
if __name__ == '__main__':
    file_path = './data/raw/marks_final.csv'
    transformed_data = transform_quiz_data(file_path)
    # Save transformed data to a new CSV file
    transformed_data.to_csv('./data/processed/marks_transformed.csv', index=False)
    print(f"\nData has been transformed and saved to './data/processed/marks_transformed.csv'")
    # Display the first and last 5 rows, and summary statistics
    print(f"\nView of the top 5 rows:\n{transformed_data.head()}")
    print(f"\nView of the bottom 5 rows:\n{transformed_data.tail()}")
    print(f"\nTransformed Data:\n{transformed_data.head()}")
    print(f"\nSummary statistics:\n{transformed_data.describe()}")  """    