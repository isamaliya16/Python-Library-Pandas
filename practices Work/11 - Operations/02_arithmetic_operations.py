# Importing pandas library
import pandas as pd

# Creating two simple DataFrames
data1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
data2 = {'A': [7, 8, 9], 'B': [10, 11, 12]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Performing arithmetic operations
sum_df = df1 + df2
diff_df = df1 - df2
prod_df = df1 * df2
quot_df = df1 / df2

# Printing the results
print("Sum of DataFrames:")
print(sum_df)
print("\nDifference of DataFrames:")
print(diff_df)
print("\nProduct of DataFrames:")
print(prod_df)
print("\nQuotient of DataFrames:")
print(quot_df)
