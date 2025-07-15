import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK data (only once)
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('wordnet')


def preprocess_text(text):
    # Lowercase
    text = text.lower()

    # Remove numbers, punctuation, special chars
    text = re.sub(r'[^a-z\s]', ' ', text)

    # Tokenize
    #words = nltk.word_tokenize(text)
    words = text.split()

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    return words
