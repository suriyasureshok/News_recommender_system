from src.components.model_saver import save
from zenml import step
import sys
import mlflow
from src.logger import logging
from src.exception import CustomException

@step(enable_cache=False)
def save_step(model,vectorizer) -> None:
    try:
        with mlflow.start_run(nested=True):
            save(model,vectorizer)
            mlflow.log_param("Saved model",model)
        logging.info("Saved model Successfully")

    except Exception as e:
        logging.error("Error occurred while saving model.")
        raise CustomException(e,sys)