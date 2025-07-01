import os 
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from .env file
load_dotenv()

# Set environment variables
my_api_key = os.getenv('GENAI_KEY')

if not my_api_key:
    raise ValueError("GENAI_KEY not found in environment variables. Check your .env file.")

genai.api_key = my_api_key

# Create an genAI client using the key from our environment variable
client = genai.Client(
    api_key = my_api_key,
)

# Specify the model to use and the messages to send
response = client.models.generate_content(
    model = "gemini-2.5-flash",
    config = types.GenerateContentConfig(
      system_instruction = "You are a master at making search queries for youtube videos, only return the search query and nothing else.",
    ),
    contents = "I have a google SWE interview coming up and idk how to do backtracking can you help me?",
)

print(response.text)