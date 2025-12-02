import google.generativeai as genai
import os
from dotenv import load_dotenv  # <--- Added this to read your .env file

# Load the environment variables from .env
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ Error: GOOGLE_API_KEY not found. Check your .env file.")
else:
    genai.configure(api_key=api_key)

    try:
        models = genai.list_models()
        print("Available Gemini models:")
        for model in models:
            print(f"- {model.name}")
            
            # Print supported generation methods to be sure
            if 'generateContent' in model.supported_generation_methods:
                 print(f"  (Supports generateContent - Good for your app!)")
                 
    except Exception as e:
        print(f"Error fetching models: {e}")