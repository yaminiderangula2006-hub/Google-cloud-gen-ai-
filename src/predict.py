import pandas as pd
import torch

from src.preprocessing import clean_text, keyword_boost
from src.bert_model import get_bert, get_bert_tokenizer
from src.config import PREDICTIONS_FILE

bert = get_bert()
bert.eval()

tokenizer = get_bert_tokenizer()

LABELS = [
    "anger",
    "fear",
    "joy",
    "love",
    "sadness",
    "surprise"
]


def save_prediction(data):

    try:
        old = pd.read_csv(PREDICTIONS_FILE)
        new = pd.concat([old, pd.DataFrame([data])], ignore_index=True)
    except Exception:
        new = pd.DataFrame([data])

    new.to_csv(PREDICTIONS_FILE, index=False)


def predict(text):

    cleaned = clean_text(text)

    encoded = tokenizer(
        cleaned,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        outputs = bert(**encoded)

    probs = torch.softmax(outputs.logits, dim=1)[0]

    idx = torch.argmax(probs).item()

    emotion = LABELS[idx]

    confidence = float(probs[idx])

    mixed = []

    for i, score in enumerate(probs):
        if score >= 0.15:
            mixed.append(
                (
                    LABELS[i],
                    round(float(score), 3)
                )
            )

    save_prediction({
        "text": text,
        "bert": emotion,
        "final": emotion,
        "confidence": confidence
    })

    return {
        "emotion": emotion,
        "confidence": round(confidence * 100, 2),
        "bert": emotion,
        "bilstm": "N/A",
        "mixed": mixed,
        "keywords": keyword_boost(text)
    }