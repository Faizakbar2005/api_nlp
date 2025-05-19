# app/utils/preprocessor.py

import re
import string
import nltk
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

nltk.download('stopwords')
stop_words = set(stopwords.words('indonesian'))
stemmer = StemmerFactory().create_stemmer()

def preprocess(text: str) -> str:
    # Lowercase
    text = text.lower()
    
    # Remove punctuation & numbers
    text = re.sub(r'[^a-z\s]', '', text)
    
    # Tokenize
    tokens = text.split()
    
    # Remove stopwords & stemming
    cleaned_tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
    
    return ' '.join(cleaned_tokens)
