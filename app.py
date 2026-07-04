import streamlit as st
import pandas as pd

from src.predict import predict
from src.gemini import generate_response
from src.database import (
    initialize_database,
    insert_record,
    fetch_history
)
from src.analytics import (
    emotion_distribution,
    confidence_chart,
    timeline_chart
)
from src.utils import (
    initialize_prediction_file,
    load_predictions
)

st.set_page_config(
    page_title="Emotion Detection Learning Support Engine",
    page_icon="🧠",
    layout="wide"
)

initialize_database()
initialize_prediction_file()

st.title("🧠 Emotion Detection Learning Support Engine")

st.markdown(
"""
Detect student emotions using **BiLSTM + DistilBERT**
and receive **AI-powered learning guidance** using Gemini.
"""
)

st.divider()

if "response" not in st.session_state:
    st.session_state.response = ""

if "emotion" not in st.session_state:
    st.session_state.emotion = ""

if "confidence" not in st.session_state:
    st.session_state.confidence = 0.0

if "prediction" not in st.session_state:
    st.session_state.prediction = None


left, right = st.columns([2,1])

with left:

    field = st.selectbox(

        "Select Category",

        [

            "Academics",

            "Career",

            "Mental Health",

            "Relationships",

            "Family",

            "Finance",

            "Other"

        ]

    )

    problem = st.text_area(

        "Describe your problem",

        height=180,

        placeholder="Explain how you are feeling..."

    )

with right:

    st.info(

        """
        Supported Models

        ✅ BiLSTM

        ✅ DistilBERT

        ✅ Gemini AI

        """
    )

analyze = st.button(
    "Analyze Emotion",
    use_container_width=True
)
if analyze:

    if problem.strip() == "":

        st.error("Please enter your problem.")

    else:

        with st.spinner("Analyzing Emotion..."):

            result = predict(problem)

            emotion = result["emotion"]

            confidence = result["confidence"]

            bilstm = result["bilstm"]

            bert = result["bert"]

            mixed = result["mixed"]

            keywords = result["keywords"]

            ai_response = generate_response(
                field,
                emotion,
                problem
            )

            st.session_state.prediction = result

            st.session_state.response = ai_response

            st.session_state.emotion = emotion

            st.session_state.confidence = confidence

            insert_record(
                problem,
                emotion,
                confidence,
                ai_response
            )

st.divider()

if st.session_state.prediction is not None:

    result = st.session_state.prediction

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Primary Emotion")

        st.success(st.session_state.emotion)

        st.metric(
            "Confidence",
            f"{st.session_state.confidence:.2f}%"
        )

    with col2:

        st.subheader("Model Comparison")

        comparison = pd.DataFrame({

            "Model":[

                "BiLSTM",

                "DistilBERT"

            ],

            "Prediction":[

                result["bilstm"],

                result["bert"]

            ]

        })

        st.table(comparison)

    st.divider()

    st.subheader("Mixed Emotion Detection")

    if len(result["mixed"]) > 0:

        mixed_df = pd.DataFrame(

            result["mixed"],

            columns=[

                "Emotion",

                "Probability"

            ]

        )

        st.dataframe(
            mixed_df,
            use_container_width=True
        )

    else:

        st.info("No secondary emotions detected.")

    st.divider()

    st.subheader("Keyword Enhancement")

    if len(result["keywords"]) > 0:

        st.write(result["keywords"])

    else:

        st.write("No keywords detected.")

    st.divider()

    st.subheader("Gemini AI Guidance")

    st.write(st.session_state.response)

    regenerate = st.button(
        "Regenerate Response"
    )

    if regenerate:

        with st.spinner("Generating..."):

            st.session_state.response = generate_response(

                field,

                st.session_state.emotion,

                problem

            )

        st.success("Response regenerated.")

        st.write(st.session_state.response)
        st.divider()

st.header("📜 Prediction History")

try:

    history = load_predictions()

    if len(history) > 0:

        st.dataframe(

            history,

            use_container_width=True,

            hide_index=True

        )

    else:

        st.info("No predictions available.")

except Exception as e:

    st.warning(f"Unable to load prediction history: {e}")

st.divider()

st.header("📊 Analytics Dashboard")

try:

    history = load_predictions()

    if len(history) > 0:

        col1, col2 = st.columns(2)

        with col1:

            fig = emotion_distribution(history)

            st.plotly_chart(

                fig,

                use_container_width=True

            )

        with col2:

            fig = confidence_chart(history)

            st.plotly_chart(

                fig,

                use_container_width=True

            )

        timeline = timeline_chart(history)

        if timeline is not None:

            st.plotly_chart(

                timeline,

                use_container_width=True

            )

    else:

        st.info("Analytics will appear after predictions are made.")

except Exception as e:

    st.warning(f"Analytics error: {e}")

st.divider()

st.markdown(
"""
### 📌 Project Information

**Emotion Detection Learning Support Engine**

Developed using:

- 🤖 BiLSTM
- 🧠 DistilBERT
- ✨ Google Gemini AI
- 📊 Streamlit
- 🗄️ SQLite
- 📈 Plotly

This system detects emotions from user text and provides
empathetic, AI-powered learning guidance.

---
Developed by **BADDI CHETAN**
"""
)