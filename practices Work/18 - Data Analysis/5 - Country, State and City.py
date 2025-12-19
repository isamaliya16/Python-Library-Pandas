import pandas as pd

# Sample Country data
country_data = {
    'CountryID': [1, 2, 3],
    'CountryName': ['USA', 'India', 'Germany'],
    'Continent': ['North America', 'Asia', 'Europe']
}

# Sample State data
state_data = {
    'StateID': [101, 102, 103, 104, 105, 106],
    'StateName': ['California', 'Texas', 'Maharashtra', 'Karnataka', 'Bavaria', 'Berlin'],
    'CountryID': [1, 1, 2, 2, 3, 3]
}

# Sample City data
city_data = {
    'CityID': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    'CityName': ['Los Angeles', 'Houston', 'Mumbai', 'Bangalore', 'Munich', 'Berlin', 'San Francisco', 'Austin'],
    'StateID': [101, 102, 103, 104, 105, 106, 101, 102],
    'Population': [4000000, 2300000, 18000000, 8400000, 1500000, 3600000, 880000, 950000]
}

# Creating DataFrames
country_df = pd.DataFrame(country_data)
state_df = pd.DataFrame(state_data)
city_df = pd.DataFrame(city_data)

# 1. Inner join on Cities and States, and then Countries
merged_df = pd.merge(pd.merge(city_df, state_df, on='StateID', how='inner'), 
                     country_df, on='CountryID', how='inner')
print("Inner Join:\n", merged_df)

# 2. Count the number of cities in each country
cities_per_country = merged_df.groupby('CountryName')['CityID'].count()
print("\nNumber of Cities in Each Country:\n", cities_per_country)

# 3. Find the average population of cities in each country
avg_population_per_country = merged_df.groupby('CountryName')['Population'].mean()
print("\nAverage Population in Each Country:\n", avg_population_per_country)

# 4. Count the number of cities in each state
cities_per_state = merged_df.groupby('StateName')['CityID'].count()
print("\nNumber of Cities in Each State:\n", cities_per_state)

# 5. Find the country with the highest average city population
highest_avg_population_country = avg_population_per_country.idxmax()
print("\nCountry with the Highest Average City Population:", highest_avg_population_country)

# 6. Get the total population in each country
total_population_per_country = merged_df.groupby('CountryName')['Population'].sum()
print("\nTotal Population in Each Country:\n", total_population_per_country)

# 7. Find the state with the highest total population
total_population_per_state = merged_df.groupby('StateName')['Population'].sum()
highest_population_state = total_population_per_state.idxmax()
print("\nState with the Highest Total Population:", highest_population_state)

# 8. Find the country with the highest total population
highest_population_country = total_population_per_country.idxmax()
print("\nCountry with the Highest Total Population:", highest_population_country)

# 9. Get the list of cities in 'California'
cities_in_california = merged_df[merged_df['StateName'] == 'California']
print("\nCities in California:\n", cities_in_california)

# 10. Find the average population of cities in each state
avg_population_per_state = merged_df.groupby('StateName')['Population'].mean()
print("\nAverage Population in Each State:\n", avg_population_per_state)

# 11. Get the highest population city in each country
highest_population_city_per_country = merged_df.loc[merged_df.groupby('CountryName')['Population'].idxmax()]
print("\nCity with the Highest Population in Each Country:\n", highest_population_city_per_country)

# 12. Find the total number of cities in each continent
cities_per_continent = merged_df.groupby('Continent')['CityID'].count()
print("\nTotal Number of Cities in Each Continent:\n", cities_per_continent)

# 13. Find the highest population city in each state
highest_population_city_per_state = merged_df.loc[merged_df.groupby('StateName')['Population'].idxmax()]
print("\nCity with the Highest Population in Each State:\n", highest_population_city_per_state)

# 14. List all countries with more than 2 cities
countries_with_more_than_2_cities = cities_per_country[cities_per_country > 2]
print("\nCountries with More Than 2 Cities:\n", countries_with_more_than_2_cities)

# 15. Find the average population of cities in the 'USA'
avg_population_usa = merged_df[merged_df['CountryName'] == 'USA']['Population'].mean()
print("\nAverage Population of Cities in USA:", avg_population_usa)

# 16. Get the names of all cities in 'Germany'
cities_in_germany = merged_df[merged_df['CountryName'] == 'Germany']['CityName']
print("\nCities in Germany:\n", cities_in_germany)

# 17. Find the country with the smallest average city population
smallest_avg_population_country = avg_population_per_country.idxmin()
print("\nCountry with the Smallest Average City Population:", smallest_avg_population_country)

# 18. List all cities with a population greater than 5 million
large_cities = merged_df[merged_df['Population'] > 5000000]
print("\nCities with Population Greater Than 5 Million:\n", large_cities)

# 19. Calculate the total population in each continent
total_population_per_continent = merged_df.groupby('Continent')['Population'].sum()
print("\nTotal Population in Each Continent:\n", total_population_per_continent)

# 20. Find the city with the highest population in each continent
highest_population_city_per_continent = merged_df.loc[merged_df.groupby('Continent')['Population'].idxmax()]
print("\nCity with the Highest Population in Each Continent:\n", highest_population_city_per_continent)

# 21. Find the average population of cities in each continent
avg_population_per_continent = merged_df.groupby('Continent')['Population'].mean()
print("\nAverage Population in Each Continent:\n", avg_population_per_continent)

# 22. Find the number of states in each country
states_per_country = state_df.groupby('CountryID')['StateID'].count().reset_index()
states_per_country = pd.merge(states_per_country, country_df, on='CountryID', how='inner')
print("\nNumber of States in Each Country:\n", states_per_country[['CountryName', 'StateID']])

# 23. Calculate the total population of cities in 'Texas'
total_population_texas = merged_df[merged_df['StateName'] == 'Texas']['Population'].sum()
print("\nTotal Population of Cities in Texas:", total_population_texas)

# 24. Get the list of cities with populations between 1 million and 5 million
cities_between_1_and_5_million = merged_df[(merged_df['Population'] >= 1000000) & (merged_df['Population'] <= 5000000)]
print("\nCities with Population Between 1 Million and 5 Million:\n", cities_between_1_and_5_million)

# 25. Find the state with the largest number of cities
most_cities_state = cities_per_state.idxmax()
print("\nState with the Largest Number of Cities:", most_cities_state)