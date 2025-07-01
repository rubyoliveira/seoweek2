import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Configure Gemini client
genai.configure(api_key=api_key)

# Use the Gemini 1.5 Flash model
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate a search prompt
response = model.generate_content("What are the advantages of pair programming?")

# Display result
print("\nGenerated Response:")
print(response.text)