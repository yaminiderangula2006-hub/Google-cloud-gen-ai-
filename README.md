# 🧠 Emotion Detection Learning Support Engine

> An AI-powered web application that detects user emotions from textual input using **DistilBERT** and **BiLSTM** models and provides personalized guidance through **Google Gemini AI**.

---

# 📌 Project Overview

The **Emotion Detection Learning Support Engine** is an intelligent web-based application developed to identify emotions from user text and provide supportive guidance based on the detected emotional state.

The system combines **Deep Learning**, **Natural Language Processing (NLP)**, and **Generative AI** to understand users' feelings and offer personalized learning and emotional support.

The application is developed using **Python**, **Streamlit**, **TensorFlow**, **PyTorch**, **Transformers**, and **Google Gemini AI**.

---

# 🎯 Objectives

The main objectives of this project are:

- Detect emotions from user textual input.
- Improve student learning support using AI.
- Provide personalized guidance using Google Gemini.
- Maintain prediction history.
- Visualize emotion analytics.
- Demonstrate practical implementation of NLP and Deep Learning.

---

# 🚀 Features

- ✅ Emotion Detection using DistilBERT
- ✅ BiLSTM Model Prediction
- ✅ Mixed Emotion Detection
- ✅ Keyword Extraction
- ✅ AI-generated Personalized Guidance
- ✅ Student Learning Support
- ✅ SQLite Database
- ✅ Prediction History
- ✅ Analytics Dashboard
- ✅ Streamlit Web Interface
- ✅ Real-time Emotion Analysis

---

# 🏗 Project Architecture

```
User Input
      │
      ▼
Text Preprocessing
      │
      ▼
Emotion Detection
 ┌───────────────┐
 │   DistilBERT  │
 └───────────────┘
        │
        ▼
Emotion Prediction
        │
        ▼
Keyword Detection
        │
        ▼
Google Gemini AI
        │
        ▼
Personalized Guidance
        │
        ▼
Store Prediction
        │
        ▼
Analytics Dashboard
```

---

# 🧠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application |
| TensorFlow | BiLSTM Model |
| PyTorch | DistilBERT Model |
| Hugging Face Transformers | NLP Model |
| Google Gemini API | AI Guidance |
| SQLite | Database |
| Plotly | Analytics Dashboard |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Scikit-learn | Label Encoding |

---

# 📂 Project Structure

```
Emotion-Detection-Learning-Support-Engine/

│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── emotion_dataset.csv
│   ├── GoEmotions/
│   └── empatheticdialogues/
│
├── models/
│   ├── bilstm/
│   ├── tokenizer.pkl
│   └── bert_emotion_model_final/
│
├── notebooks/
│   └── Emotion_Training.ipynb
│
├── src/
│   ├── analytics.py
│   ├── bert_model.py
│   ├── config.py
│   ├── database.py
│   ├── gemini.py
│   ├── model.py
│   ├── predict.py
│   ├── preprocessing.py
│   ├── train.py
│   └── utils.py
│
└── test.py
```

---

# ⚙️ Project Workflow

## Phase 1 – Dataset Collection

Emotion datasets were collected from publicly available sources including:

- Emotion Dataset
- GoEmotions Dataset
- Empathetic Dialogues Dataset

---

## Phase 2 – Data Preprocessing

The collected data undergoes:

- Text Cleaning
- Lowercase Conversion
- Removing URLs
- Removing Special Characters
- Tokenization
- Sequence Padding

---

## Phase 3 – Model Training

Two Deep Learning models are used:

### 🔹 BiLSTM

- Word Embedding
- Bidirectional LSTM
- Dense Layers
- Softmax Classification

### 🔹 DistilBERT

- Fine-tuned Transformer Model
- Context-aware Emotion Detection
- Higher Prediction Accuracy

---

## Phase 4 – Emotion Prediction

The system predicts emotions such as:

- 😀 Joy
- 😢 Sadness
- 😡 Anger
- 😨 Fear
- ❤️ Love
- 😲 Surprise

The final prediction is generated using the best confidence score.

---

## Phase 5 – Keyword Enhancement

Important emotional keywords are extracted from user input to improve understanding.

Example:

Input:

```
I feel nervous about my exams.
```

Detected Keyword:

```
fear
```

---

## Phase 6 – AI Guidance

Google Gemini AI generates personalized guidance based on:

- Selected Category
- User Problem
- Detected Emotion

Example:

```
Category:
Academics

Emotion:
Fear

Response:
Break your study schedule into small goals, practice regularly, and maintain confidence. Consistent preparation reduces exam anxiety.
```

---

## Phase 7 – Database Storage

Each prediction is stored in SQLite with:

- User Text
- Emotion
- Confidence
- AI Response
- Timestamp

---

## Phase 8 – Analytics Dashboard

The dashboard visualizes:

- Emotion Distribution
- Confidence Scores
- Prediction Timeline

using Plotly charts.

---

# 🌍 Real World Example

### User Input

Category:

```
Academics
```

Problem:

```
I am feeling nervous about my final exams.
```

### Emotion Prediction

```
Fear
```

Confidence

```
99.89%
```

Keyword

```
fear
```

Gemini Response

```
Create a study plan,
take regular breaks,
practice mock tests,
and remember that consistent effort is more important than perfection.
```

---

# 📸 Screenshots

Include screenshots such as:

- Home Page
- User Input
- Emotion Prediction
- Mixed Emotion Detection
- AI Guidance
- Prediction History
- Analytics Dashboard

*(Add images to an `assets/` folder and reference them here.)*

Example:

```markdown
## Home Page

![Home](assets/home.png)

## Emotion Prediction

![Prediction](assets/prediction.png)
```

---

# 📊 Supported Emotions

| Emotion | Description |
|----------|-------------|
| Joy | Happiness |
| Sadness | Feeling Low |
| Anger | Frustration |
| Fear | Anxiety |
| Love | Affection |
| Surprise | Unexpected Feeling |

---

# 💻 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Emotion-Detection-Learning-Support-Engine.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# 📦 Required Libraries

```
streamlit
tensorflow
torch
transformers
google-generativeai
pandas
numpy
plotly
scikit-learn
joblib
python-dotenv
```

---

# 🔮 Future Enhancements

- Voice Emotion Detection
- Facial Emotion Recognition
- Multilingual Emotion Analysis
- Speech-to-Text Integration
- Mobile Application
- Cloud Deployment
- Student Performance Prediction

---

# 🎓 Academic Applications

This project can be used in:

- Smart Learning Systems
- E-learning Platforms
- Student Counseling
- Mental Health Monitoring
- AI Education Platforms
- Emotion-aware Learning Systems

---

# 👨‍💻 Developed By

Baddi chetan
Derangula Yamini
Bala Navya Sree
Arveti Arun Kumar
Anand Kumar

Annamacharya institute of technology and sciences,kadapa
---

# 📜 License

This project is developed for academic and educational purposes.

---

# ⭐ Acknowledgement

This project was developed as part of academic learning to demonstrate the integration of **Artificial Intelligence**, **Natural Language Processing**, **Deep Learning**, and **Generative AI** for emotion-aware learning support.

Special thanks to:

- Hugging Face
- TensorFlow
- PyTorch
- Google Gemini
- Streamlit
- Plotly
