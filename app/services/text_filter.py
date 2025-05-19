# app/utils/text_filter.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.utils.preprocessor import preprocess

def is_relevant(query: str, text: str, threshold: float = 0.2) -> bool:
    clean_query = preprocess(query)
    clean_text = preprocess(text)

    docs = [clean_query, clean_text]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(docs)

    sim_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return sim_score >= threshold
