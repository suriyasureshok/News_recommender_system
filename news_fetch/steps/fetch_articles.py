from zenml import step
import requests
import pandas as pd
import sys
from src.logger import logging
from src.exception import CustomException

@step(enable_cache=False)
def fetch_step() -> pd.DataFrame:
    try:
        API = 'a5jfEDGVHw40H8PB9xBoMlPKpg92OnGdi3OZ591I'
        response = requests.get(f'https://api.thenewsapi.com/v1/news/all?api_token={API}&language=en&locale=in')
        data = response.json()
        df = pd.DataFrame(data['data'])
        logging.info('Data Fetched successfully.')
        return df
    
    except Exception as e:
        logging.error("An error occurred.")
        raise CustomException(e,sys)