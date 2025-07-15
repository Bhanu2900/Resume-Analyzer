from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_match_score(resume_text, jd_text):
    corpus = [resume_text, jd_text]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return round(score[0][0] * 100, 2)  # Return as percentage
