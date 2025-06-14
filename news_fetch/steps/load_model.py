import sys
import joblib
from src.logger import logging
from src.exception import CustomException
from zenml import step
from sklearn.base import BaseEstimator

@step
def load_step() -> BaseEstimator:
    try:
        model = joblib.load('model/classifier.pkl')
        logging.info('Model Loaded successfully.')
        return model
    
    except Exception as e:
        logging.error('Error loading model.')
        raise CustomException(e,sys)