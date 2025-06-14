import sys
import psycopg2
from datetime import datetime, timedelta
from src.logger import logging
from src.exception import CustomException
from zenml import step

@step
def deletion_step() -> None:
    try:
        ystrdy = (datetime.now() - timedelta(days=1)).date()
        conn = psycopg2.connect('postgresql://neondb_owner:npg_XOkZ2jyGNd6a@ep-empty-flower-a8c046xv-pooler.eastus2.azure.neon.tech/neondb?sslmode=require')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM articles WHERE date = %s", (ystrdy,))
        conn.commit()
        logging.info("Deletion of articles from yesterday completed")
        cursor.close()
        conn.close()

    except Exception as e:
        logging.error('Data deletion successful')
        raise CustomException(e,sys)