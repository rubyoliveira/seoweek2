import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load API key from .env
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
      system_instruction = "You are a university instructor and can explain programming concepts clearly in a few words."
    ),
    contents = "What are the advantages of pair programming?",
)

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
