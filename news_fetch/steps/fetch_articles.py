from zenml import step
import requests
import pandas as pd
import sys
from src.logger import logging
from src.exception import CustomException

@step
def fetch_step() -> pd.DataFrame:
    try:
        API = '3a029167e178b9fdba7a4c5e749c7aff'
        response = requests.get(f'https://gnews.io/api/v4/top-headlines?lang=en&token={API}')
        data = response.json()
        df = pd.DataFrame(data['articles'])
        logging.info('Data Fetched successfully.')
        return df
    
    except Exception as e:
        logging.error("An error occurred.")
        raise CustomException(e,sys)