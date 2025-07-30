# Student-Marks-Data-Pipeline

---
## Dataset
- This dataset contains anonymized quiz scores for students enrolled in the course Innovation and Entrepreneurship. The data is collected from multiple quizzes conducted throughout the academic term.For the final evaluation, the best 9 scores were considered and then scaled down to a maximum of 30.

- Features:
  * Roll Number: Unique student identifier
  * Quiz 1 to Quiz N: Individual quiz marks(evaluated out of 5)
  * Total: Sum of all quiz scores

- Link to the dataset.
[Student Quiz Marks Dataset](https://www.kaggle.com/datasets/pratsharma7/student-quiz-marks-dataset)

---
## Data Pipeline
1. **Goal**
- The purpose of this pipeline is to store the collect stendent data into a database after cleaning, transforming , and enriching the data to make it useful for analysis and visualization.
2. **Exatraction**
- This is the start of the pipeline. Raw data is extracted from the csv file and converted into a data frame using pandas. 
3. **Tranformation**
- In this section I did the following:
  * Rename the column 'Out of 30' to 'Total Marks(x/30)'
  * Dropped SNO column 
  * Convert AB values in the Quiz colums to 0. This makes all the values to be integers.
  * Check if the 'ROLL NUMBER' column valus are unique and removed duplicates to enfornce data integrity.
  * Saved the transformed data to a csv file.

4. **Loading**
- Before loading the data I first had to set up the sqlite database. Then I proceeded to load the transformed data into the data base as follows:
   * I created student marks database and two tables: marks and total marks.


---
## Use case
- **Data Analysis and Visualization** of the student perfomances