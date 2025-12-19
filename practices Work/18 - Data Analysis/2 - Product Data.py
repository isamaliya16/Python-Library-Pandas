import pandas as pd

# Sample products data
data = {
    'ProductID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'ProductName': ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse', 'Printer', 'Camera', 'Speaker', 'Headphones'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Accessories', 'Accessories', 'Accessories', 'Electronics', 'Accessories', 'Accessories'],
    'Price': [1200, 800, 300, 150, 30, 20, 100, 500, 50, 80],
    'Stock': [50, 200, 150, 75, 300, 250, 80, 40, 100, 150],
    'Brand': ['BrandA', 'BrandB', 'BrandC', 'BrandA', 'BrandD', 'BrandD', 'BrandE', 'BrandC', 'BrandF', 'BrandG'],
    'Rating': [4.5, 4.8, 4.3, 4.1, 4.0, 3.9, 4.2, 4.6, 3.8, 4.4]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Query 1: Display all products in the 'Electronics' category
electronics_products = df[df['Category'] == 'Electronics']
print("Electronics Products:\n", electronics_products)

# Query 2: Find the average price of products in the 'Accessories' category
avg_accessories_price = df[df['Category'] == 'Accessories']['Price'].mean()
print("\nAverage Price in Accessories Category:", avg_accessories_price)

# Query 3: Count the number of products in each category
category_count = df['Category'].value_counts()
print("\nNumber of Products in Each Category:\n", category_count)

# Query 4: Find the product with the highest price 
highest_price_product = df[df['Price'] == df['Price'].max()]
print("\nProduct with the Highest Price:\n", highest_price_product)

# Query 5: Get the names of all products with a rating higher than 4.5
high_rated_products = df[df['Rating'] > 4.5]['ProductName']
print("\nProducts with Rating Higher Than 4.5:\n", high_rated_products)

# Query 6: Find the average stock available for 'Electronics' products
avg_electronics_stock = df[df['Category'] == 'Electronics']['Stock'].mean()
print("\nAverage Stock in Electronics Category:", avg_electronics_stock)

# Query 7: List all products with a price greater than 500
expensive_products = df[df['Price'] > 500]
print("\nProducts with Price Greater Than 500:\n", expensive_products)

# Query 8: Sort products by rating in descending order
sorted_by_rating = df.sort_values(by='Rating', ascending=False)
print("\nProducts Sorted by Rating (Descending):\n", sorted_by_rating)

# Query 9: Display the names and prices of products that are in stock more than 100 units
in_stock_products = df[df['Stock'] > 100][['ProductName', 'Price']]
print("\nProducts in Stock More Than 100 Units:\n", in_stock_products)

# Query 10: Find the total stock of all products in the 'Accessories' category
total_accessories_stock = df[df['Category'] == 'Accessories']['Stock'].sum()
print("\nTotal Stock in Accessories Category:", total_accessories_stock)

# Query 11: Find the average price of products by 'BrandA'
avg_brand_a_price = df[df['Brand'] == 'BrandA']['Price'].mean()
print("\nAverage Price of BrandA Products:", avg_brand_a_price)

# Query 12: Get a list of products with a price between 50 and 150
mid_range_products = df[(df['Price'] >= 50) & (df['Price'] <= 150)]
print("\nProducts with Price Between 50 and 150:\n", mid_range_products)

# Query 13: Find the product with the lowest stock
least_stock_product = df[df['Stock'] == df['Stock'].min()]
print("\nProduct with the Lowest Stock:\n", least_stock_product)

# Query 14: Count the number of products priced over 100
products_over_100 = df[df['Price'] > 100].shape[0]
print("\nNumber of Products Priced Over 100:", products_over_100)

# Query 15: List products that belong to 'Accessories' category and have a rating higher than 4.0
high_rated_accessories = df[(df['Category'] == 'Accessories') & (df['Rating'] > 4.0)]
print("\nHigh Rated Accessories Products:\n", high_rated_accessories)

# Query 16: Find the highest rated product in each category
highest_rated_per_category = df.groupby('Category')['Rating'].max()
print("\nHighest Rated Product in Each Category:\n", highest_rated_per_category)

# Query 17: Calculate the total value of stock for all products (Price * Stock)
df['TotalValue'] = df['Price'] * df['Stock']
print("\nDataFrame with Total Value of Stock:\n", df)

# Query 18: Find the average rating of products by 'BrandC'
avg_brand_c_rating = df[df['Brand'] == 'BrandC']['Rating'].mean()
print("\nAverage Rating of BrandC Products:", avg_brand_c_rating)

# Query 19: List products with names starting with 'S'
products_with_s = df[df['ProductName'].str.startswith('S')]
print("\nProducts with Names Starting with 'S':\n", products_with_s)

# Query 20: Create a new column 'DiscountedPrice' as 90% of the price and display the updated DataFrame
df['DiscountedPrice'] = df['Price'] * 0.90
print("\nDataFrame with Discounted Price Column:\n", df)
