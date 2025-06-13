from zenml import step
import pandas as pd
import sys
from src.components.data_ingestion import CSVIngestor
import mlflow
from src.exception import CustomException
from src.logger import logging

@step
def ingest_step(data_path:str) -> pd.DataFrame:
    try:
        mlflow.set_experiment("News_Recommendation_Pipeline")
        with mlflow.start_run(nested=True):
            ingestor = CSVIngestor()
            df = ingestor.ingest(data_path=data_path)
            logging.info('Data Ingestion Step Succesful')
            mlflow.log_param("data_shape", df.shape)
            mlflow.log_param("columns", df.columns.tolist())
            return df
        
    except Exception as e:
        raise CustomException(e,sys)