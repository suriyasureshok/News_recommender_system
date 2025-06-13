from sklearn.metrics import classification_report
import pandas as pd
import sys
from src.logger import logging
from src.exception import CustomException
import joblib

def evaluate(model,X_test,y_test) -> None:
    try:
        y_pred = model.predict(X_test)

        logging.info(f'{model} Model has been evaluated successfully.')
        print(f'Classification Report:\n {classification_report(y_test,y_pred)}')

    except Exception as e:
        logging.error(f'Error occurred while evaluating the model.')
        raise CustomException(e,sys)