import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend(liked_list, all_news, k=10):
    if not liked_list:
        return all_news[:k]
    text = [n.title + ' ' + n.description for n in liked_list + all_news]
    vec = TfidfVectorizer(max_features=500).fit_transform(text).toarray()
    liked_vec = vec[:len(liked_list)].mean(axis=0)
    scores = cosine_similarity([liked_vec], vec[len(liked_list):])[0]
    ranked = sorted(zip(all_news, scores), key=lambda x: x[1], reverse=True)
    return [n for n, _ in ranked[:k]]
