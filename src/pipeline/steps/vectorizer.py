from zenml import step
import pandas as pd
import sys
from typing import Tuple
from typing_extensions import Annotated
from sklearn.feature_extraction.text import TfidfVectorizer
from src.components.data_vectorizer import vectorize
from src.logger import logging
from src.exception import CustomException
from scipy.sparse import csr_matrix
import mlflow

@step
def vectorize_step(df: pd.DataFrame) -> Tuple[
    Annotated[csr_matrix,"X_train"],
    Annotated[csr_matrix,"X_test"],
    Annotated[pd.Series,"y_train"],
    Annotated[pd.Series,"y_test"],
    Annotated[object,"vectorizer"],
    ]:
    try:
        with mlflow.start_run(nested=True):
            X_train, X_test, y_train, y_test,vectorizer = vectorize(df)
            mlflow.log_param("vectorizer_max_features", 10000)
            mlflow.log_param("train_size", X_train.shape[0])
            logging.info('Vectoriztion Successful.')
    
        return X_train, X_test, y_train, y_test,vectorizer
    
    except Exception as e:
        logging.error(f"Error in vectorize step.")
        raise CustomException(e,sys)