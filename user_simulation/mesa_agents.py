from mesa import Agent

class NewsUserAgent(Agent):
    def __init__(self, unique_id, model, preference):
        super().__init__(unique_id, model)
        self.preference = preference

    def step(self):
        article = self.random.choice(self.model.articles)
        if self.preference.get(article['category_level_1'], 0) > 0.5:
            self.model.log_interactions(self.unique_id, article['data_id'], liked = True)
        else:
            self.model.log_interactions(self.unique_id, article['data_id'], liked = False)

