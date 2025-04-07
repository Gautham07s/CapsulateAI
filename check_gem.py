import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

try:
    models = genai.list_models()
    print("Available Gemini models:")
    for model in models:
        print(f"- {model.name}")
except Exception as e:
    print(f"Error fetching models: {e}")
