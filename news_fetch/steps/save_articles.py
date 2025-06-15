from src.exception import CustomException
from src.logger import logging
import pandas as pd
from zenml import step
import psycopg2
import sys

@step
def save_db_step(df:pd.DataFrame) -> None:
    try:
        conn = psycopg2.connect('postgresql://neondb_owner:npg_XOkZ2jyGNd6a@ep-empty-flower-a8c046xv-pooler.eastus2.azure.neon.tech/neondb?sslmode=require')
        cursor = conn.cursor()
        
        for index, row in df.iterrows():
            cursor.execute("""
                INSERT INTO storage_of_articles (title, description, published_at)
                VALUES (%s, %s, %s)
                RETURNING id
            """,
            (row["title"], row["description"], row["published_at"]))
            article_id = cursor.fetchone()[0]

            cursor.execute("""
                INSERT INTO categories (name)
                VALUES (%s)
                ON CONFLICT (name) DO NOTHING
                RETURNING id
            """, (row["categories"],))
            result = cursor.fetchone()
            if result:
                category_id = result[0]
            else:
                cursor.execute("""
                    SELECT id FROM categories WHERE name = %s
                """, (row["categories"],))
                category_id = cursor.fetchone()[0]

            cursor.execute("""
                INSERT INTO article_categories (article_id, category_id)
                VALUES (%s, %s)
                ON CONFLICT DO NOTHING
            """, (article_id, category_id))
            
        logging.info('Data Stored successfully')
        conn.commit()

    except Exception as e:
        conn.rollback()
        logging.error(f"Error in storing the data: {str(e)}")
        raise CustomException(e, sys)
    
    finally:
        cursor.close()
        conn.close()