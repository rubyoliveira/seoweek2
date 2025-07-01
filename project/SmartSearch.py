import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from .env file
load_dotenv()

# Set environment variables
gemini_api_key = os.getenv('GENAI_KEY')
youtube_api_key = os.getenv('YOUTUBE_API_KEY')
youtube_url = 'https://www.googleapis.com/youtube/v3/search'

if not gemini_api_key:
    raise ValueError("GENAI_KEY not found in environment variables. Check your .env file.")

genai.api_key = gemini_api_key

# Create an genAI client using the key from our environment variable
client = genai.Client(
    api_key = gemini_api_key,
)

user_request = input("Enter your request to gemini: ")

# Specify the model to use and the messages to send
response = client.models.generate_content(
    model = "gemini-2.5-flash",
    config = types.GenerateContentConfig(
      system_instruction = "You are a master at making search queries for youtube videos, only return the search query and nothing else.",
    ),
    contents = user_request,
)

print(response.text)