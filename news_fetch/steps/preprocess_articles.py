import sys
import joblib
from src.exception import CustomException
from src.logger import logging
from datetime import datetime
import pandas as pd
from zenml import step
from src.components.data_preprocessing import preprocess

@step(enable_cache=False)
def preprocess_input_step(model,df:pd.DataFrame) -> list[dict]:
    try:
        labeled_articles = []
        vectorizer = joblib.load('model/tfidf_vectorizer.joblib')
        df = preprocess(df)

        X = vectorizer.transform(df['description'])
        labels = model.predict(X)

        for idx, label in enumerate(labels):
            labeled_articles.append({
                "title": df.iloc[idx]["title"],
                "description": df.iloc[idx]["description"],
                "published_At": df.iloc[idx]["published_At"],
                "category_level_1": label
            })

        logging.info('Data preprocessing and labeling completed.')
        return labeled_articles
    
    except Exception as e:
        logging.error('Data preprocesses terminated')
        raise CustomException(e,sys)