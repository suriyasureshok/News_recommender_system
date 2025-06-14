from abc import ABC, abstractmethod
import pandas as pd
from src.logger import logging
from src.exception import CustomException
import sys

class DataIngestor(ABC):
    @abstractmethod
    def ingest(self):
        pass

class CSVIngestor(DataIngestor):
    def ingest(self,data_path:str)-> pd.DataFrame:
        try:
            if data_path.endswith('.csv'):
                df = pd.read_csv(data_path)
                logging.info("DataSet Loaded Successfully.")
                return df
            else:
                logging.info("Invalid file path")
                raise CustomException("The loaded dataset is not a csv file. Please upload a csv file.")
            
        except Exception as e:
            logging.error('Ingestion unsuccessful.')
            raise CustomException(e,sys)