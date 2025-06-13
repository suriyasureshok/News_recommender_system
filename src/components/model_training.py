from typing import Tuple
from typing_extensions import Annotated
import pandas as pd
import sys
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV
from sklearn.base import BaseEstimator
from src.logger import logging
from src.exception import CustomException

def train(X_train,y_train) -> Tuple[
    Annotated[BaseEstimator,"best_model"],
    Annotated[float,"best_score"],
    Annotated[dict,"best_params"]
    ]:
    try:
        models = {
            'LogisticRegression':
            (LogisticRegression(max_iter=1000), 
             {"C": [0.1,1,10]}),

            'RandomForestClassifier':
            (RandomForestClassifier(),
             {"n_estimators":[100],"max_depth":[10,20]}),

            'LinearSVC': (
            LinearSVC(),
            {"C": [1, 10]}  # Simple and fast
            ),

            'MultinomialNB':
            (MultinomialNB(),
             {"alpha":[0.5,1.0]})
        }

        best_score = 0
        best_model = None
        best_params = {}

        for name, (model, param_grid) in models.items():
            logging.info(f'{name} Model Training has been started')
            grid_search = GridSearchCV(model, param_grid, cv=5, scoring='f1_weighted')
            grid_search.fit(X_train, y_train)
            score = grid_search.best_score_

            if score > best_score:
                best_score = score
                best_model = grid_search.best_estimator_
                best_params = grid_search.best_params_
                
            logging.info(f'{name} Model trained successfully')

        return best_model, best_score, best_params
    
    except Exception as e:
        logging.error(f"Error in training model")
        raise CustomException(e,sys)