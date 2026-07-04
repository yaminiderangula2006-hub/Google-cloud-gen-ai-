import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Model Paths
BILSTM_MODEL = os.path.join(
    BASE_DIR,
    "models",
    "bilstm",
    "bilstm_model.keras"
)

TOKENIZER = os.path.join(
    BASE_DIR,
    "models",
    "tokenizer.pkl"
)

LABEL_ENCODER = os.path.join(
    BASE_DIR,
    "models",
    "bilstm",
    "label_encoder.pkl"
)

BERT_MODEL = os.path.join(
    BASE_DIR,
    "models",
    "bert_emotion_model_final"
)

# Data
DATA_DIR = os.path.join(BASE_DIR, "data")

PREDICTIONS_FILE = os.path.join(
    DATA_DIR,
    "predictions.csv"
)

LOG_DIR = os.path.join(BASE_DIR, "logs")

MAX_SEQUENCE_LENGTH = 128