# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Applying aggregate functions
sum_result = df.sum()
mean_result = df.mean()
min_result = df.min()
max_result = df.max()

# Printing the aggregate results
print("Sum of DataFrame:")
print(sum_result)
print("\nMean of DataFrame:")
print(mean_result)
print("\nMin of DataFrame:")
print(min_result)
print("\nMax of DataFrame:")
print(max_result)
