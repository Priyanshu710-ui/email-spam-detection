"""
preprocess.py
-------------
Text cleaning and tokenization utilities shared by train.py and app.py.
"""

import re
import string

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


def ensure_nltk_data():
    """Download required NLTK resources if they aren't already present."""
    resources = {
        "tokenizers/punkt": "punkt",
        "tokenizers/punkt_tab": "punkt_tab",
        "corpora/stopwords": "stopwords",
    }
    for path, name in resources.items():
        try:
            nltk.data.find(path)
        except LookupError:
            nltk.download(name, quiet=True)


ensure_nltk_data()

STOPWORDS = set(stopwords.words("english"))
STEMMER = PorterStemmer()


def clean_text(text: str) -> str:
    """Lowercase, strip URLs/HTML/punctuation/numbers, remove stopwords, and stem."""
    text = text.lower()
    text = re.sub(r"http\S+|www\.\S+", " ", text)          # URLs
    text = re.sub(r"<.*?>", " ", text)                       # HTML tags
    text = re.sub(r"\d+", " ", text)                         # numbers
    text = text.translate(str.maketrans("", "", string.punctuation))  # punctuation
    text = re.sub(r"\s+", " ", text).strip()

    try:
        tokens = word_tokenize(text)
    except LookupError:
        tokens = text.split()

    tokens = [STEMMER.stem(t) for t in tokens if t not in STOPWORDS and len(t) > 1]
    return " ".join(tokens)


def preprocess_series(texts):
    """Apply clean_text to an iterable of raw email texts."""
    return [clean_text(t) for t in texts]
