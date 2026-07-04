from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)

from src.config import BERT_MODEL

_tokenizer = AutoTokenizer.from_pretrained(
    BERT_MODEL
)

_model = AutoModelForSequenceClassification.from_pretrained(
    BERT_MODEL
)


def get_bert():
    return _model


def get_bert_tokenizer():
    return _tokenizer