import os
import pandas as pd
from datetime import datetime

from src.config import PREDICTIONS_FILE


def timestamp():

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def initialize_prediction_file():

    if not os.path.exists(PREDICTIONS_FILE):

        df = pd.DataFrame(
            columns=[
                "timestamp",
                "text",
                "bilstm",
                "bert",
                "final",
                "confidence"
            ]
        )

        df.to_csv(
            PREDICTIONS_FILE,
            index=False
        )


def load_predictions():

    initialize_prediction_file()

    return pd.read_csv(PREDICTIONS_FILE)