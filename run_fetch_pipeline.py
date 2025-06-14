from fetch_pipeline import fetch_and_store_articles
from src.logger import logging

if __name__ == "__main__":
    logging.info('Pipeline has started')
    fetch_and_store_articles()
    logging.info('Pipeline has ended')