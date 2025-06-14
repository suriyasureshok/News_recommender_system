from src.components.data_preprocessing import preprocess
from zenml import step
import pandas as pd
import mlflow
import sys
from src.logger import logging
from src.exception import CustomException

@step(enable_cache=False)
def preprocess_step(df: pd.DataFrame) -> pd.DataFrame:
    try:
        clean_df = preprocess(df)
        mlflow.log_param("rows_after_cleaning", clean_df.shape[0])
        logging.info('Data preprocessing Successful.')
        return clean_df
    
    except Exception as e:
        logging.error("Error in preprocess step.")
        raise CustomException(e,sys)