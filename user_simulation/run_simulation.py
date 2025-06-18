from mesa_agents import NewsUserAgent
from mesa_model import NewsRecommendationModel
from simulated_users import generate_fake_users
import pandas as pd

users_df = generate_fake_users(1000, ['crime, law and justice', 'arts, culture, entertainment and media',
       'economy, business and finance',
       'disaster, accident and emergency incident', 'environment',
       'education', 'health', 'human interest', 'lifestyle and leisure',
       'politics', 'labour', 'religion and belief',
       'science and technology', 'society', 'sport',
       'conflict, war and peace', 'weather'])
articles_df = pd.read_csv('analysis/data/news_dataset.csv')

model = NewsRecommendationModel(users_df, articles_df)

for _ in range(10):
    model.step()

interactions_df = pd.DataFrame(model.interactions)
interactions_df.to_csv('analysis/data/simulated_interactions.csv', index = False)