from training_pipeline import training_pipeline_step
from src.logger import logging

if __name__ == "__main__":
    logging.info('Pipeline has started')
    training_pipeline_step()
    logging.info('Pipeline has ended')