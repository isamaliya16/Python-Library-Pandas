# ? Install required package
# pip3 install kaggle

import os

os.environ['KAGGLE_USERNAME'] = 'girishinindia'
os.environ['KAGGLE_KEY'] = '85ff15b66796f72136a0dba04abc4aac'
from kaggle.api.kaggle_api_extended import KaggleApi

# Authenticate the API
api = KaggleApi()
api.authenticate()

def get_kaggle_data(dataset_name, file_name):

    # Define dataset and destination path
    dataset_path = dataset_name  
    destination_path = '17 - Kaggle Analysis/data'
    file_path = os.path.join(destination_path, file_name)

    if not os.path.exists(file_path):
        # Download and unzip the dataset
        api.dataset_download_files(dataset_path, path=destination_path, unzip=True)


    file_path = os.path.join(destination_path, file_name)

    return file_path
