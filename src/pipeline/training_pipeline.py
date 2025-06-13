from zenml import pipeline
from src.pipeline.steps.ingest_data import ingest_step
from src.pipeline.steps.preprocess import preprocess_step
from src.pipeline.steps.vectorizer import vectorize_step
from src.pipeline.steps.train_model import train_step
from src.pipeline.steps.model_evaluate import evaluate_step
from src.pipeline.steps.save_model import save_step

@pipeline
def training_pipeline_step():
    df = ingest_step('analysis/data/news_dataset.csv')
    clean_df = preprocess_step(df=df)
    X_train, X_test, y_train, y_test,vectorizer = vectorize_step(df=clean_df)
    model = train_step(X_train,y_train)
    evaluate_step(model,X_test,y_test)
    save_step(model,vectorizer)