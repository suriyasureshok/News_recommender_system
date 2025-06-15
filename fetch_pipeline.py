from zenml import pipeline
from news_fetch.steps.fetch_articles import fetch_step
from news_fetch.steps.preprocess_articles import preprocess_input_step
from news_fetch.steps.load_model import load_step
from news_fetch.steps.store_articles import postgres_step
from news_fetch.steps.save_articles import save_db_step

@pipeline()
def fetch_and_store_articles():
    df = fetch_step()
    model = load_step()
    save_db_step(df)
    label_articles = preprocess_input_step(model,df)
    postgres_step(label_articles)