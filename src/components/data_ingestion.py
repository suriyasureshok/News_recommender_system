from abc import ABC, abstractmethod
import pandas as pd

class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path:str):
        pass

class CSVIngestor(DataIngestor):
    def ingest(self, file_path: str)-> pd.DataFrame:
        if not file_path.endswith('.csv'):
            raise ValueError("File path must end with '.csv'")
        else:
            df = pd.read_csv(file_path)
            return df
        
class 