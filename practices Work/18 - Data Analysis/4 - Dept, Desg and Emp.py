import pandas as pd

# Sample Departments data
departments_data = {
    'DepartmentID': [1, 2, 3, 4, 5],
    'DepartmentName': ['HR', 'Finance', 'IT', 'Marketing', 'Operations'],
    'Location': ['New York', 'London', 'San Francisco', 'Berlin', 'Tokyo']
}

# Sample Designations data
designations_data = {
    'DesignationID': [101, 102, 103, 104, 105],
    'DesignationName': ['Manager', 'Senior Developer', 'Junior Developer', 'Analyst', 'Intern']
}

# Sample Employees data
employees_data = {
    'EmployeeID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ivan', 'Jack'],
    'DepartmentID': [1, 2, 3, 1, 2, 3, 4, 5, 4, 5],
    'DesignationID': [101, 102, 103, 104, 105, 101, 102, 103, 104, 105],
    'Age': [25, 30, 45, 28, 35, 40, 26, 32, 42, 29],
    'Salary': [50000, 60000, 80000, 52000, 62000, 78000, 51000, 63000, 79000, 54000],
    'Experience': [2, 5, 20, 3, 10, 18, 1, 6, 19, 4],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'F', 'M', 'M']
}

# Creating DataFrames
departments_df = pd.DataFrame(departments_data)
designations_df = pd.DataFrame(designations_data)
employees_df = pd.DataFrame(employees_data)

# 1. Inner join on Employees, Departments, and Designations
merged_df = pd.merge(pd.merge(employees_df, departments_df, on='DepartmentID', how='inner'), 
                     designations_df, on='DesignationID', how='inner')
print("Inner Join:\n", merged_df)

# 2. Count the number of employees in each department
employees_per_department = merged_df.groupby('DepartmentName')['EmployeeID'].count()
print("\nNumber of Employees in Each Department:\n", employees_per_department)

# 3. Find the average salary of employees in each department
avg_salary_per_department = merged_df.groupby('DepartmentName')['Salary'].mean()
print("\nAverage Salary in Each Department:\n", avg_salary_per_department)

# 4. Count the number of employees in each designation
employees_per_designation = merged_df.groupby('DesignationName')['EmployeeID'].count()
print("\nNumber of Employees in Each Designation:\n", employees_per_designation)

# 5. Find the department with the highest average salary
highest_avg_salary_dept = avg_salary_per_department.idxmax()
print("\nDepartment with the Highest Average Salary:", highest_avg_salary_dept)

# 6. Get the total number of years of experience in each department
total_experience_per_department = merged_df.groupby('DepartmentName')['Experience'].sum()
print("\nTotal Experience in Each Department:\n", total_experience_per_department)

# 7. Find the designation with the highest total salary
total_salary_per_designation = merged_df.groupby('DesignationName')['Salary'].sum()
highest_salary_designation = total_salary_per_designation.idxmax()
print("\nDesignation with the Highest Total Salary:", highest_salary_designation)

# 8. Find the department with the highest total experience
highest_experience_dept = total_experience_per_department.idxmax()
print("\nDepartment with the Highest Total Experience:", highest_experience_dept)

# 9. Get the list of employees working as 'Senior Developer'
senior_developers = merged_df[merged_df['DesignationName'] == 'Senior Developer']
print("\nSenior Developers:\n", senior_developers)

# 10. Find the average age of employees in each designation
avg_age_per_designation = merged_df.groupby('DesignationName')['Age'].mean()
print("\nAverage Age in Each Designation:\n", avg_age_per_designation)

# 11. Get the highest salary in each department
highest_salary_per_department = merged_df.groupby('DepartmentName')['Salary'].max()
print("\nHighest Salary in Each Department:\n", highest_salary_per_department)

# 12. Find the total number of female employees in each department
female_employees_per_department = merged_df[merged_df['Gender'] == 'F'].groupby('DepartmentName')['EmployeeID'].count()
print("\nTotal Female Employees in Each Department:\n", female_employees_per_department)

# 13. Find the highest salary in each designation
highest_salary_per_designation = merged_df.groupby('DesignationName')['Salary'].max()
print("\nHighest Salary in Each Designation:\n", highest_salary_per_designation)

# 14. List all departments with more than 2 employees
departments_with_more_than_2 = employees_per_department[employees_per_department > 2]
print("\nDepartments with More Than 2 Employees:\n", departments_with_more_than_2)

# 15. Find the average experience of employees in the 'IT' department
avg_experience_it = merged_df[merged_df['DepartmentName'] == 'IT']['Experience'].mean()
print("\nAverage Experience in IT Department:", avg_experience_it)

# 16. Get the names of all employees in 'Marketing' and 'Operations' departments
marketing_operations_employees = merged_df[merged_df['DepartmentName'].isin(['Marketing', 'Operations'])]['Name']
print("\nEmployees in Marketing and Operations Departments:\n", marketing_operations_employees)

# 17. Find the department with the youngest average employee age
youngest_avg_age_dept = merged_df.groupby('DepartmentName')['Age'].mean().idxmin()
print("\nDepartment with the Youngest Average Age:", youngest_avg_age_dept) 

# 18. List all employees who have more than 10 years of experience and work as 'Manager'
experienced_managers = merged_df[(merged_df['Experience'] > 10) & (merged_df['DesignationName'] == 'Manager')]
print("\nManagers with More Than 10 Years of Experience:\n", experienced_managers)

# 19. Calculate the total salary expenditure for each department
total_salary_per_department = merged_df.groupby('DepartmentName')['Salary'].sum()
print("\nTotal Salary Expenditure in Each Department:\n", total_salary_per_department)

# 20. Find the employee with the highest salary in each department
highest_salary_employee_per_dept = merged_df.loc[merged_df.groupby('DepartmentName')['Salary'].idxmax()]
print("\nEmployee with the Highest Salary in Each Department:\n", highest_salary_employee_per_dept)

# 21. Find the average salary of male employees in each department
avg_salary_male_per_department = merged_df[merged_df['Gender'] == 'M'].groupby('DepartmentName')['Salary'].mean()
print("\nAverage Salary of Male Employees in Each Department:\n", avg_salary_male_per_department)

# 22. Find the number of employees in each department location
employees_per_location = merged_df.groupby('Location')['EmployeeID'].count()
print("\nNumber of Employees in Each Location:\n", employees_per_location)

# 23. Get the department with the most employees
most_employees_dept = employees_per_department.idxmax()
print("\nDepartment with the Most Employees:", most_employees_dept)

# 24. Calculate the total salary expenditure for all employees working in New York
total_salary_ny = merged_df[merged_df['Location'] == 'New York']['Salary'].sum()
print("\nTotal Salary Expenditure for Employees in New York:", total_salary_ny)

# 25. Get the list of employees who work in departments located in 'San Francisco'
sf_employees = merged_df[merged_df['Location'] == 'San Francisco']
print("\nEmployees in Departments Located in San Francisco:\n", sf_employees)
