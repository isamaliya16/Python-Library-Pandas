import pandas as pd

# 1. Read the Excel file into a Pandas DataFrame
df = pd.read_excel('16 - Basic Data Analysis/data/employee_data.xlsx')

# 2. Display the first 5 records of the DataFrame
# print(df.head())

# # 3. Get the column names of the DataFrame
# print(df.columns)

# # 4. Get the summary statistics of the DataFrame
# print(df.describe())

# # 5. Filter employees with a salary greater than 60000
# high_salary = df[df['salary'] > 60000]
# print(high_salary)

# # 6. Get the list of unique departments
# unique_departments = df['department'].unique()
# print(unique_departments)

# # 7. Get the number of employees in each department
# department_counts = df['department'].value_counts()
# print(department_counts)

# # 8. Add a new column 'bonus' which is 10% of the salary
# df['bonus'] = df['salary'] * 0.10
# print(df)

# # 9. Get the average salary of employees
# average_salary = df['salary'].mean()
# print(average_salary)

# # 10. Get the employee(s) with the highest salary
# highest_salary = df[df['salary'] == df['salary'].max()]
# print(highest_salary)

# # 11. Sort the DataFrame by the 'salary' column in descending order
# sorted_df = df.sort_values(by='salary', ascending=False)
# print(sorted_df)

# # 12. Rename the 'birthdate' column to 'dob'
# df.rename(columns={'birthdate': 'dob'}, inplace=True)
# print(df)

# # 13. Calculate the age of each employee
# from datetime import datetime
# df['age'] = df['birthdate'].apply(lambda x: datetime.now().year - pd.to_datetime(x).year)
# print(df)

# # 14. Get the total salary paid to all employees
# total_salary = df['salary'].sum()
# print(total_salary)

# # 15. Find employees who joined before the year 2020
# early_joiners = df[pd.to_datetime(df['date_of_joining']) < '2020-01-01']
# print(early_joiners)

# # 16. Group employees by department and get the average salary for each department
# avg_salary_by_dept = df.groupby('department')['salary'].mean()
# print(avg_salary_by_dept)

# # 17. Check for missing values in the DataFrame
# missing_values = df.isnull().sum()
# print(missing_values)

# # 18. Fill missing values in the 'salary' column with the average salary
# df['salary'].fillna(df['salary'].mean(), inplace=True)
# print(df)

# # 19. Drop the 'age' column from the DataFrame
# df.drop(columns=['designation'], inplace=True)
# print(df)

# # 20. Merge the DataFrame with another DataFrame containing department head information
# dept_heads = pd.DataFrame({
#     'department': ['HR', 'Finance', 'IT', 'Marketing', 'Operations'],
#     'head': ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
# })
# merged_df = pd.merge(df, dept_heads, on='department', how='left')
# print(merged_df)

# # 21. Save the DataFrame to a CSV file
# df.to_csv('16 - Data Analysis/data/employee_data.csv', index=False)

# # 22. Read specific columns from the Excel file
# df_specific = pd.read_excel('16 - Data Analysis/data/employee_data.xlsx', usecols=['id', 'first_name', 'salary'])
# print(df_specific)

# # 23. Filter employees who are in the 'IT' department
# it_employees = df[df['department'] == 'IT']
# print(it_employees)

# # 24. Change the 'date_of_joining' column to datetime format
# df['date_of_joining'] = pd.to_datetime(df['date_of_joining'])
# print(df)

# # 25. Find the total number of employees
# total_employees = df['id'].count()
# print(total_employees)

# # 28. Get the median salary of employees
# median_salary = df['salary'].median()
# print(median_salary)

# # 29. Filter employees who are either in the 'HR' or 'IT' department
# hr_it_employees = df[df['department'].isin(['HR', 'IT'])]
# print(hr_it_employees)

# # 30. Create a new DataFrame with employees' names and their respective departments
# name_dept_df = df[['first_name', 'last_name', 'department']]
# print(name_dept_df)
