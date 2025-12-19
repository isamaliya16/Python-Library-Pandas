
from kaggle_auth import get_kaggle_data
import pandas as pd


datasets = ['girishinindia/master', 'syedanwarafridi/vehicle-sales-data']
files = ['MVR.csv', 'car_prices.csv']

file_path = get_kaggle_data(datasets[1], files[1])

df = pd.read_csv(file_path)

print(df)
# print(df.info())      # get infor of dataset
