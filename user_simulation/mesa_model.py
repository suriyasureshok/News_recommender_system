from mesa import Model
from mesa.time import RandomActivation
import pandas as pd
from mesa_agents import NewsUserAgent

class NewsRecommendationModel(Model):
    def __init__(self, users_df, articles_df):
        self.schedule = RandomActivation(self)
        self.users_df = users_df
        self.articles = articles_df.to_dict('records')
        self.interactions = []

        for i, row in users_df.iterrows():
            agent = NewsUserAgent(i, self, row['preference'])
            self.schedule.add(agent)

    def log_interactions(self, user_id, article_id, liked):
        self.interactions.append({
            'user_id':user_id,
            'article_id': article_id,
            'liked':liked
        })

    def step(self):
        self.schedule.step()