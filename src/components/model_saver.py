import joblib
from src.logger import logging
from src.exception import CustomException
import sys

def save(model,vectorizer) -> None:
    try:
        joblib.dump(model, 'model/classifier.pkl')
        joblib.dump(vectorizer, "model/tfidf_vectorizer.joblib")
        logging.info(f'{model} model and vectorizer has been saved successfully')
        
    except Exception as e:
        logging.error(f"Error occurred while saving model and vectorizer.")
        raise CustomException(e, sys)