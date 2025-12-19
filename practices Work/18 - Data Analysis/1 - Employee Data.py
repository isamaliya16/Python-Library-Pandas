import pandas as pd

# Sample data
data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ivan', 'Jack'],
    'Department': ['HR', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR'],
    'Age': [25, 30, 45, 28, 35, 40, 26, 32, 42, 29],
    'Salary': [50000, 60000, 80000, 52000, 62000, 78000, 51000, 63000, 79000, 54000],
    'Experience': [2, 5, 20, 3, 10, 18, 1, 6, 19, 4],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'F', 'M', 'M']
}

# Creating DataFrame
df = pd.DataFrame(data)

# Query 1: Display all employees in the IT department
it_employees = df[df['Department'] == 'IT']
print("IT Employees:\n", it_employees)

# Query 2: Find the average salary of employees in the HR department
avg_hr_salary = df[df['Department'] == 'HR']['Salary'].mean()
print("\nAverage Salary in HR Department:", avg_hr_salary)

# Query 3: Count the number of employees in each department
department_count = df['Department'].value_counts()
print("\nNumber of Employees in Each Department:\n", department_count)

# Query 4: Find the employee with the highest salary
highest_salary = df[df['Salary'] == df['Salary'].max()]
print("\nEmployee with the Highest Salary:\n", highest_salary)

# Query 5: Get the names of all female employees
female_employees = df[df['Gender'] == 'F']['Name']
print("\nFemale Employees:\n", female_employees)

# Query 6: Find the average age of employees in the Finance department
avg_finance_age = df[df['Department'] == 'Finance']['Age'].mean()
print("\nAverage Age in Finance Department:", avg_finance_age)

# Query 7: List all employees with more than 10 years of experience
experienced_employees = df[df['Experience'] > 10]
print("\nEmployees with More Than 10 Years of Experience:\n", experienced_employees)

# Query 8: Sort employees by salary in descending order 
sorted_by_salary = df.sort_values(by='Salary', ascending=False)
print("\nEmployees Sorted by Salary (Descending):\n", sorted_by_salary)

# Query 9: Display the names and salaries of employees younger than 30
young_employees = df[df['Age'] < 30][['Name', 'Salary']]
print("\nEmployees Younger Than 30:\n", young_employees)

# Query 10: Find the total salary paid to employees in the IT department
total_it_salary = df[df['Department'] == 'IT']['Salary'].sum()
print("\nTotal Salary Paid in IT Department:", total_it_salary)

# Query 11: Find the average experience of male employees
avg_male_experience = df[df['Gender'] == 'M']['Experience'].mean()
print("\nAverage Experience of Male Employees:", avg_male_experience)

# Query 12: Get a list of employees with salaries between 50,000 and 70,000
salary_range = df[(df['Salary'] >= 50000) & (df['Salary'] <= 70000)]
print("\nEmployees with Salaries Between 50,000 and 70,000:\n", salary_range)

# Query 13: Find the employee with the least experience
least_experience = df[df['Experience'] == df['Experience'].min()]
print("\nEmployee with the Least Experience:\n", least_experience)

# Query 14: Count the number of employees older than 40
older_than_40 = df[df['Age'] > 40].shape[0]
print("\nNumber of Employees Older Than 40:", older_than_40)

# Query 15: List employees who are in the HR department and have more than 3 years of experience
hr_experienced = df[(df['Department'] == 'HR') & (df['Experience'] > 3)]
print("\nHR Employees with More Than 3 Years of Experience:\n", hr_experienced)

# Query 16: Find the highest salary in each department
highest_salary_per_dept = df.groupby('Department')['Salary'].max()
print("\nHighest Salary in Each Department:\n", highest_salary_per_dept)

# Query 17: Calculate the total number of years of experience for all employees
total_experience = df['Experience'].sum()
print("\nTotal Years of Experience for All Employees:", total_experience)

# Query 18: Find the average salary for female employees
avg_female_salary = df[df['Gender'] == 'F']['Salary'].mean()
print("\nAverage Salary for Female Employees:", avg_female_salary)

# Query 19: List employees with names starting with 'A'
names_with_a = df[df['Name'].str.startswith('A')]
print("\nEmployees with Names Starting with 'A':\n", names_with_a)

# Query 20: Create a new column 'Bonus' as 10% of the salary and display the updated DataFrame
df['Bonus'] = df['Salary'] * 0.10
print("\nDataFrame with Bonus Column:\n", df)
