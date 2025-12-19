import pandas as pd
import numpy as np

# Sample Departments data
departments_data = {
    'DepartmentID': [1, 2, 3, 4],
    'DepartmentName': ['HR', 'Finance', 'IT', 'Marketing'],
    'Location': ['New York', 'London', 'San Francisco', np.nan]
}

# Sample Employees data with missing values and null columns
employees_data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', np.nan, 'David', 'Eva', 'Frank', 'Grace', 'Hannah', np.nan, 'Jack'],
    'DepartmentID': [1, 2, 3, 4, np.nan, 3, 1, 2, 4, 1],
    'Age': [25, np.nan, 45, 28, 35, 40, 26, np.nan, 42, 29],
    'Salary': [50000, 60000, 80000, np.nan, 62000, 78000, 51000, 63000, 79000, np.nan],
    'Experience': [2, 5, 20, 3, 10, 18, 1, 6, 19, np.nan],
    'Gender': ['F', 'M', 'M', np.nan, 'F', 'M', 'F', 'F', 'M', 'M']
}

# Creating DataFrames
departments_df = pd.DataFrame(departments_data)
employees_df = pd.DataFrame(employees_data)

# Join Departments and Employees data
merged_df = pd.merge(employees_df, departments_df, on='DepartmentID', how='left')
print("Merged DataFrame:\n", merged_df)

# 1. Display the dataset with missing values
print("\nOriginal DataFrame with Missing Values:\n", merged_df)

# 2. Check for missing values in each column
missing_values = merged_df.isnull().sum()
print("\nMissing Values in Each Column:\n", missing_values)

# 3. Fill missing values in the 'Age' column with the mean value
merged_df['Age'].fillna(merged_df['Age'].mean(), inplace=True)
print("\nDataFrame after Filling Missing 'Age' Values with Mean:\n", merged_df)

# 4. Fill missing values in the 'Salary' column with the median value
merged_df['Salary'].fillna(merged_df['Salary'].median(), inplace=True)
print("\nDataFrame after Filling Missing 'Salary' Values with Median:\n", merged_df)

# 5. Drop rows with any missing values
df_dropna = merged_df.dropna()
print("\nDataFrame after Dropping Rows with Any Missing Values:\n", df_dropna)

# 6. Drop rows with all missing values
df_dropna_all = merged_df.dropna(how='all')
print("\nDataFrame after Dropping Rows with All Missing Values:\n", df_dropna_all)

# 7. Fill missing values in 'Location' column with 'Unknown'
merged_df['Location'].fillna('Unknown', inplace=True)
print("\nDataFrame after Filling Missing 'Location' Values with 'Unknown':\n", merged_df)

# 8. Replace missing 'Gender' values with 'Unknown'
merged_df['Gender'].fillna('Unknown', inplace=True)
print("\nDataFrame after Replacing Missing 'Gender' Values with 'Unknown':\n", merged_df)

# 9. Fill missing values using forward fill method
df_ffill = merged_df.fillna(method='ffill')
print("\nDataFrame after Forward Fill (ffill) Method:\n", df_ffill)

# 10. Fill missing values using backward fill method
df_bfill = merged_df.fillna(method='bfill')
print("\nDataFrame after Backward Fill (bfill) Method:\n", df_bfill)

# 11. Interpolate missing values in the 'Experience' column
merged_df['Experience'] = merged_df['Experience'].interpolate()
print("\nDataFrame after Interpolating Missing 'Experience' Values:\n", merged_df)

# 12. Drop columns with any missing values
df_drop_columns = merged_df.dropna(axis=1)
print("\nDataFrame after Dropping Columns with Any Missing Values:\n", df_drop_columns)

# 13. Check for missing values after performing data cleaning
missing_values_after_cleaning = merged_df.isnull().sum()
print("\nMissing Values in Each Column After Cleaning:\n", missing_values_after_cleaning)

# 14. Replace missing values in 'Name' column with 'No Name'
merged_df['Name'].fillna('No Name', inplace=True)
print("\nDataFrame after Replacing Missing 'Name' Values with 'No Name':\n", merged_df)

# 15. Fill missing 'DepartmentID' values with mode
merged_df['DepartmentID'].fillna(merged_df['DepartmentID'].mode()[0], inplace=True)
print("\nDataFrame after Filling Missing 'DepartmentID' Values with Mode:\n", merged_df)

# 16. Create a new column 'Tax' where missing values are calculated as 10% of 'Salary'
merged_df['Tax'] = merged_df['Salary'] * 0.10
print("\nDataFrame with New 'Tax' Column:\n", merged_df)

# 17. Check for rows where all values are missing
all_missing = merged_df[merged_df.isnull().all(axis=1)]
print("\nRows Where All Values are Missing:\n", all_missing)

# 18. Drop duplicate rows if any
df_dedup = merged_df.drop_duplicates()
print("\nDataFrame after Dropping Duplicate Rows:\n", df_dedup)

# 19. Find the total count of missing values in the entire DataFrame
total_missing_values = merged_df.isnull().sum().sum()
print("\nTotal Count of Missing Values in the Entire DataFrame:", total_missing_values)

# 20. Replace all missing values with a placeholder string 'Missing'
df_replace_all = merged_df.fillna('Missing')
print("\nDataFrame after Replacing All Missing Values with 'Missing':\n", df_replace_all)

# 21. Fill missing values in 'Salary' using linear interpolation
merged_df['Salary'] = merged_df['Salary'].interpolate()
print("\nDataFrame after Interpolating Missing 'Salary' Values:\n", merged_df)

# 22. Group data by 'Department' and calculate the average 'Salary' (handling missing values)
avg_salary_by_dept = merged_df.groupby('DepartmentName')['Salary'].mean()
print("\nAverage Salary by Department (Handling Missing Values):\n", avg_salary_by_dept)

# 23. Detect missing values in 'Location' column and flag them
merged_df['Location_Missing_Flag'] = merged_df['Location'] == 'Unknown'
print("\nDataFrame with 'Location_Missing_Flag' Column:\n", merged_df)

# 24. Fill missing 'Experience' values with the previous value in the column
merged_df['Experience'] = merged_df['Experience'].fillna(method='pad')
print("\nDataFrame after Filling Missing 'Experience' with Previous Value:\n", merged_df)

# 25. Replace missing values in multiple columns with their respective mean
df_filled_mean = merged_df.copy()
df_filled_mean[['Age', 'Salary', 'Experience']] = df_filled_mean[['Age', 'Salary', 'Experience']].apply(lambda x: x.fillna(x.mean()))
print("\nDataFrame after Replacing Missing Values in Multiple Columns with Mean:\n", df_filled_mean)
