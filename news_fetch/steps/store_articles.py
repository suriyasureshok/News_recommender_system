import sys
from src.exception import CustomException
from src.logger import logging
from zenml import step
import psycopg2

@step
def postgres_step(label_articles) -> None:
    try:
        conn = psycopg2.connect("postgresql://neondb_owner:npg_XOkZ2jyGNd6a@ep-empty-flower-a8c046xv-pooler.eastus2.azure.neon.tech/User?sslmode=require")
        cursor = conn.cursor()
        for article in label_articles:
            cursor.execute("""
                INSERT INTO articles (title, description, published_at, category)
                VALUES (%s, %s, %s, %s)
            """,
            (article["title"], article["description"], article["published_at"], article["category"]))
        logging.info('Data Stored successfully')
        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        logging.error('Data Storage Terminated')
        raise CustomException(e,sys)
