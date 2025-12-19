import pandas as pd

# Read the Excel file into a Pandas DataFrame
df_customer = pd.read_excel('16 - Basic Data Analysis/data/customer_data.xlsx')

# 1. Display the first 5 records of the DataFrame
# print(df_customer.head())

# # 2. Get the column names of the DataFrame
# print(df_customer.columns)

# # 3. Get the summary statistics of the DataFrame
# print(df_customer.describe())

# # 4. Filter customers from 'New York'
# ny_customers = df_customer[df_customer['city'] == 'New York']
# print(ny_customers)

# # 5. Get the list of unique cities
# unique_cities = df_customer['city'].unique()
# print(unique_cities)

# # 6. Get the number of customers in each city
# city_counts = df_customer['city'].value_counts()
# print(city_counts)

# # 7. Add a new column 'full_name' combining 'first_name' and 'last_name'
# df_customer['full_name'] = df_customer['first_name'] + ' ' + df_customer['last_name']
# print(df_customer)

# # 8. Get the average length of registration time in years
# df_customer['registration_date'] = pd.to_datetime(df_customer['registration_date'])
# df_customer['years_registered'] = (pd.Timestamp.now() - df_customer['registration_date']).dt.days / 365
# average_years_registered = df_customer['years_registered'].mean()
# print(average_years_registered)

# # 9. Get the customer(s) with the earliest registration date
# earliest_registration = df_customer[df_customer['registration_date'] == df_customer['registration_date'].min()]
# print(earliest_registration)

# # 10. Sort the DataFrame by the 'registration_date' column in ascending order
# sorted_df = df_customer.sort_values(by='registration_date')
# print(sorted_df)

# # 11. Rename the 'zip_code' column to 'postal_code'
# df_customer.rename(columns={'zip_code': 'postal_code'}, inplace=True)
# print(df_customer)

# # 12. Calculate the total number of characters in the 'address' column
# df_customer['address_length'] = df_customer['address'].apply(len)
# print(df_customer)

# # 13. Get the total number of customers
# total_customers = df_customer['id'].count()
# print(total_customers)

# # 14. Group customers by state and get the count of customers in each state
# state_customer_counts = df_customer.groupby('state')['id'].count()
# print(state_customer_counts)

# # 15. Check for missing values in the DataFrame
# missing_values = df_customer.isnull().sum()
# print(missing_values)

# # 16. Fill missing values in the 'email' column with 'unknown@example.com'
# df_customer['email'].fillna('unknown@example.com', inplace=True)
# print(df_customer)

# # 17. Drop the 'phone' column from the DataFrame
# df_customer.drop(columns=['phone'], inplace=True)
# print(df_customer)

# # 18. Merge the DataFrame with another DataFrame containing city population information
# city_population = pd.DataFrame({
#     'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
#     'population': [8419000, 3980400, 2716000, 2328000, 1690000]
# })
# merged_df = pd.merge(df_customer, city_population, on='city', how='left')
# print(merged_df)

# # 19. Save the DataFrame to a CSV file
# df_customer.to_csv('16 - Data Analysis/data/customer_data.csv', index=False)

# # 20. Read specific columns from the Excel file
# df_specific = pd.read_excel('16 - Data Analysis/data/customer_data.xlsx', usecols=['id', 'first_name', 'email'])
# print(df_specific)

# # 21. Filter customers who are in 'Chicago'
# chicago_customers = df_customer[df_customer['city'] == 'Chicago']
# print(chicago_customers)

# # 22. Change the 'registration_date' column to datetime format
# df_customer['registration_date'] = pd.to_datetime(df_customer['registration_date'])
# print(df_customer)

# # 23. Create a pivot table with the count of customers in each state and city
# pivot_table = df_customer.pivot_table(values='id', index='state', columns='city', aggfunc='count')
# print(pivot_table)
