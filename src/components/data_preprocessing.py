import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from src.logger import logging
from src.exception import CustomException

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

stop_words = set(stopwords.words('english'))

custom_stopwords = stop_words.union({"said", "year", "000", "com", "https", "he", "she","would","could",'uh', 'um', 'er', 'ah', 'like', 'okay', 'ok', 'right', 'well', 'hmm', 'sorta', 'kinda', 'youknow', 'actually', 'basically', 'literally', 'just', 'really',
    'is', 'am', 'are', 'was', 'were', 'be', 'been', 'being', 
    'have', 'has', 'had', 'do', 'does', 'did', 'doing', 
    'can', 'could', 'should', 'would', 'may', 'might', 'must', 'shall', 'will',
    'the', 'a', 'an', 'this', 'that', 'these', 'those',
    'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them',
    'my', 'your', 'his', 'its', 'our', 'their',
    'mine', 'yours', 'hers', 'ours', 'theirs',
    'and', 'or', 'but', 'if', 'because', 'so', 'while', 'although', 'though',
    'not', 'no', 'nor', 'only', 'very', 'too', 'also', 'even', 'than',
    'in', 'on', 'at', 'by', 'to', 'from', 'of', 'with', 'as', 'about', 'for', 'between', 'through', 'during', 'before', 'after', 'under', 'over', 'against', 'without', 'within', 'into', 'onto', 'upon',
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
    'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
    'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
    'seventy', 'eighty', 'ninety', 'hundred', 'thousand', 'million', 'billion',
    'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
    'eighth', 'ninth', 'tenth',
    'https', 'http', 'www', 'com', 'net', 'org', 'html', 'co', 'inc',
    'said', 'he', 'she', '000', 'year', 'new', 'old',})

def preprocess(df: pd.DataFrame)->pd.DataFrame:
    try:
        def clean_text(text):
            tokens = word_tokenize(text.lower())
            features = [t for t in tokens if t.isalnum() and t not in custom_stopwords]
            return ' '.join(features)
        
        logging.info('Data Cleaning started.')
        df['content'] = df['content'].fillna('').apply(clean_text)
        logging.info('Data Cleaning successful.')
        return df
    
    except Exception as e:
        logging.error('Preprocessing failed please try again.')
        raise CustomException(e,sys)