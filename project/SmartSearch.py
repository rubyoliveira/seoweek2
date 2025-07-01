import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from googleapiclient.discovery import build

# Load environment variables from .env file
load_dotenv()

# Set environment variables
gemini_api_key = os.getenv('GENAI_KEY')
youtube_api_key = os.getenv('YOUTUBE_API_KEY')
youtube_url = 'https://www.googleapis.com/youtube/v3/search'

if not gemini_api_key:
    raise ValueError("GENAI_KEY not found in environment variables. Check your .env file.")
if not youtube_api_key:
    raise ValueError("YOUTUBE_API_KEY not found in environment variables. Check your .env file.")

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

print("\n🔍 Gemini search query:")
print(response.text)

youtube = build("youtube", "v3", developerKey=youtube_api_key)
youtube_response = youtube.search().list(
    part='snippet',
    q=response.text,
    type='video',
    maxResults=5
).execute()

print("\n📹 Top YouTube Results:")
for item in youtube_response["items"]:
    title = item["snippet"]["title"]
    video_id = item["id"]["videoId"]
    url = f"https://www.youtube.com/watch?v={video_id}"
    print(f"- {title}\n  {url}\n")
