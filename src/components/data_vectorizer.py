from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
from scipy.sparse import csr_matrix
from typing import Tuple
from typing_extensions import Annotated
import sys
from src.logger import logging
from src.exception import CustomException

def vectorize(df:pd.DataFrame)->Tuple[
    Annotated[csr_matrix,"X_train"],
    Annotated[csr_matrix,"X_test"],
    Annotated[pd.Series,"y_train"],
    Annotated[pd.Series,"y_test"],
    Annotated[object,"vectorizer"]]:
    try:
        X = df['content'].fillna('')
        y = df['category_level_1']

        vectorizer = TfidfVectorizer(max_features=10000)
        X_tfidf = vectorizer.fit_transform(X)
        logging.info('Feature column vectorized successfully.')

        X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)
        logging.info('Train Test Split Done.')

        return X_train, X_test, y_train, y_test,vectorizer
    
    except Exception as e:
        logging.error("Error occurred while vectorizing the data.")
        raise CustomException(e,sys)