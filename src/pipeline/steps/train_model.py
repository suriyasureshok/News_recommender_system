from src.components.model_training import train
from zenml import step
import mlflow
import sys
from src.logger import logging
from src.exception import CustomException
from sklearn.base import BaseEstimator

@step(enable_cache=False)
def train_step(X_train,y_train)-> BaseEstimator:
    try:
        with mlflow.start_run(nested=True):
            model,score,params =  train(X_train,y_train)
            mlflow.log_params(params)
            logging.info('Model training successful')
            return model
        
    except Exception as e:
        logging.error(f"Error in training step.")
        raise CustomException(e,sys)