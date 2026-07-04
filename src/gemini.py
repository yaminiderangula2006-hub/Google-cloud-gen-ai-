import google.generativeai as genai

from src.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

# Use a currently supported model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_response(field, emotion, problem):

    prompt = f"""
You are an empathetic AI learning assistant.

Student Category:
{field}

Detected Emotion:
{emotion}

Student Problem:
{problem}

Provide:

1. Emotional support
2. Practical advice
3. Study strategy
4. Motivation
5. A short action plan

Keep the response friendly and concise.
"""

    response = model.generate_content(prompt)

    return response.text