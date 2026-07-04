import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words("english"))

KEYWORDS = {
    "exam": "fear",
    "assignment": "fear",
    "deadline": "fear",
    "job": "fear",
    "placement": "fear",
    "happy": "joy",
    "excited": "joy",
    "love": "love",
    "angry": "anger",
    "hate": "anger",
    "cry": "sadness",
    "depressed": "sadness"
}


def clean_text(text):

    text = text.lower()

    text = re.sub(r"http\S+", "", text)

    text = re.sub(r"[^a-zA-Z ]", "", text)

    words = text.split()

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)


def keyword_boost(text):

    detected = []

    text = text.lower()

    for key, value in KEYWORDS.items():

        if key in text:

            detected.append(value)

    return detected