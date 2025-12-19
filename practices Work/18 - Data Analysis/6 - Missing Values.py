import pandas as pd
import numpy as np

# Sample data with missing values and null columns
data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', np.nan, 'Hannah', 'Ivan', 'Jack'],
    'Department': ['HR', 'Finance', 'IT', 'HR', np.nan, 'IT', 'HR', 'Finance', 'IT', 'HR'],
    'Age': [25, 30, np.nan, 28, 35, 40, 26, np.nan, 42, 29],
    'Salary': [50000, 60000, 80000, np.nan, 62000, 78000, 51000, 63000, 79000, np.nan],
    'Experience': [2, 5, 20, 3, 10, 18, 1, 6, 19, np.nan],
    'Gender': ['F', 'M', 'M', np.nan, 'F', 'M', 'F', 'F', 'M', 'M'],
    'Bonus': [5000, 6000, np.nan, 5200, 6200, 7800, 5100, np.nan, 7900, 5400]
}

# Creating DataFrame
df = pd.DataFrame(data)

# 1. Display the dataset with missing values
print("Original DataFrame with Missing Values:\n", df)

# 2. Check for missing values in each column
missing_values = df.isnull().sum()
print("\nMissing Values in Each Column:\n", missing_values)

# 3. Fill missing values in the 'Age' column with the mean value
df['Age'].fillna(df['Age'].mean(), inplace=True)
print("\nDataFrame after Filling Missing 'Age' Values with Mean:\n", df)

# 4. Fill missing values in the 'Salary' column with the median value
df['Salary'].fillna(df['Salary'].median(), inplace=True)
print("\nDataFrame after Filling Missing 'Salary' Values with Median:\n", df)

# 5. Drop rows with any missing values
df_dropna = df.dropna()
print("\nDataFrame after Dropping Rows with Any Missing Values:\n", df_dropna)

# 6. Drop rows with all missing values
df_dropna_all = df.dropna(how='all')
print("\nDataFrame after Dropping Rows with All Missing Values:\n", df_dropna_all)

# 7. Fill missing values in 'Bonus' column with zero
df['Bonus'].fillna(0, inplace=True)
print("\nDataFrame after Filling Missing 'Bonus' Values with Zero:\n", df)

# 8. Replace missing 'Gender' values with a specific value (e.g., 'Unknown')
df['Gender'].fillna('Unknown', inplace=True)
print("\nDataFrame after Replacing Missing 'Gender' Values with 'Unknown':\n", df)

# 9. Fill missing values using forward fill method
df_ffill = df.fillna(method='ffill')
print("\nDataFrame after Forward Fill (ffill) Method:\n", df_ffill)

# 10. Fill missing values using backward fill method
df_bfill = df.fillna(method='bfill')
print("\nDataFrame after Backward Fill (bfill) Method:\n", df_bfill)

# 11. Interpolate missing values in the 'Experience' column
df['Experience'] = df['Experience'].interpolate()
print("\nDataFrame after Interpolating Missing 'Experience' Values:\n", df)

# 12. Drop columns with any missing values
df_drop_columns = df.dropna(axis=1)
print("\nDataFrame after Dropping Columns with Any Missing Values:\n", df_drop_columns)

# 13. Check for missing values after performing data cleaning
missing_values_after_cleaning = df.isnull().sum()
print("\nMissing Values in Each Column After Cleaning:\n", missing_values_after_cleaning)

# 14. Replace missing values in 'Name' column with 'No Name'
df['Name'].fillna('No Name', inplace=True)
print("\nDataFrame after Replacing Missing 'Name' Values with 'No Name':\n", df)

# 15. Fill missing 'Department' values with mode
df['Department'].fillna(df['Department'].mode()[0], inplace=True)
print("\nDataFrame after Filling Missing 'Department' Values with Mode:\n", df)

# 16. Create a new column 'Tax' where missing values are calculated as 10% of 'Salary'
df['Tax'] = df['Salary'] * 0.10
print("\nDataFrame with New 'Tax' Column:\n", df)

# 17. Check for rows where all values are missing
all_missing = df[df.isnull().all(axis=1)]
print("\nRows Where All Values are Missing:\n", all_missing)

# 18. Drop duplicate rows if any
df_dedup = df.drop_duplicates()
print("\nDataFrame after Dropping Duplicate Rows:\n", df_dedup)

# 19. Find the total count of missing values in the entire DataFrame
total_missing_values = df.isnull().sum().sum()
print("\nTotal Count of Missing Values in the Entire DataFrame:", total_missing_values)

# 20. Replace all missing values with a placeholder string 'Missing'
df_replace_all = df.fillna('Missing')
print("\nDataFrame after Replacing All Missing Values with 'Missing':\n", df_replace_all)

# 21. Fill missing values in 'Bonus' using linear interpolation
df['Bonus'] = df['Bonus'].replace(0, np.nan)  # Replace zeros with NaN for interpolation
df['Bonus'] = df['Bonus'].interpolate()
print("\nDataFrame after Interpolating Missing 'Bonus' Values:\n", df)

# 22. Group data by 'Department' and calculate the average 'Salary' (handling missing values)
avg_salary_by_dept = df.groupby('Department')['Salary'].mean()
print("\nAverage Salary by Department (Handling Missing Values):\n", avg_salary_by_dept)

# 23. Detect missing values in 'Name' column and flag them
df['Name_Missing_Flag'] = df['Name'].isnull()
print("\nDataFrame with 'Name_Missing_Flag' Column:\n", df)

# 24. Fill missing 'Experience' values with the previous value in the column
df['Experience'] = df['Experience'].fillna(method='pad')
print("\nDataFrame after Filling Missing 'Experience' with Previous Value:\n", df)

# 25. Replace missing values in multiple columns with their respective mean
df_filled_mean = df.copy()
df_filled_mean[['Age', 'Salary', 'Experience']] = df_filled_mean[['Age', 'Salary', 'Experience']].apply(lambda x: x.fillna(x.mean()))
print("\nDataFrame after Replacing Missing Values in Multiple Columns with Mean:\n", df_filled_mean)
