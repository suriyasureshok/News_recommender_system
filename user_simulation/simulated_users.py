import random
import pandas as pd

def generate_fake_users(n, categories):
    users = []
    for i in range(n):
        preference = {cat: random.random() for cat in categories}
        users.append({'id': i, 'preference': preference})
    return pd.DataFrame(users)