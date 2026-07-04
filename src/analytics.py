import pandas as pd
import plotly.express as px


def emotion_distribution(df):

    fig = px.pie(
        df,
        names="final",
        title="Emotion Distribution"
    )

    return fig


def confidence_chart(df):

    fig = px.bar(
        df,
        x="final",
        y="confidence",
        color="final",
        title="Confidence Score"
    )

    return fig


def timeline_chart(df):

    if "timestamp" not in df.columns:
        return None

    fig = px.line(
        df,
        x="timestamp",
        y="confidence",
        color="final",
        markers=True,
        title="Prediction Timeline"
    )

    return fig