from src.components.model_evaluation import evaluate
from zenml import step
import mlflow
from sklearn.metrics import accuracy_score
from src.exception import CustomException
from src.logger import logging
import sys

@step
def evaluate_step(model,X_test,y_test) -> float:
    try:
        with mlflow.start_run(nested=True):
            predictions = model.predict(X_test)
            accuracy = accuracy_score(y_test, predictions)
            mlflow.log_metric("accuracy", accuracy)
            evaluate(model,X_test,y_test)
            return accuracy
        
    except Exception as e:
        logging.error("Error in evaluate_step.")
        raise CustomException(e,sys)