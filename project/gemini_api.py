import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")
if not my_api_key:
    raise ValueError(f"Missing GEMINI_API_KEY — got: {repr(os.environ)}")

# Create the client
client = genai.Client(api_key=my_api_key)

def generate_prompt(user_topic: str) -> str:
    """
    Uses Gemini to generate a single optimized YouTube search phrase for a given topic.
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=(
                "You are a helpful assistant that rewrites student questions "
                "into short, specific YouTube search phrases. Return ONE clean search phrase. "
                "Avoid full sentences, lists, or explanations."
            )
        ),
        contents=user_topic,
    )

    return response.text.strip()

# sample test
# print(generate_prompt("I am struggling to understand recursion"))

# output: 
# recursion explained