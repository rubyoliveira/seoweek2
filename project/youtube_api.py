import os
import requests
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
if not YOUTUBE_API_KEY:
    raise ValueError("Missing YOUTUBE_API_KEY in .env")

def search_youtube_videos(query: str, max_results: int = 3):
    """
    Searches YouTube for videos matching the query.
    Returns a list of (title, url) tuples.
    """
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "key": YOUTUBE_API_KEY,
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("YouTube API error:", response.status_code, response.text)
        return []

    data = response.json().get("items", [])
    results = []
    for item in data:
        title = item["snippet"]["title"]
        video_id = item["id"]["videoId"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        results.append((title, video_url))

    return results

# sample test case
if __name__ == "__main__":
    test_query = "recursion explained"
    videos = search_youtube_videos(test_query)
    for i, (title, url) in enumerate(videos, 1):
        print(f"{i}. {title}\n   {url}")

# output:
# 1. This is a Better Way to Understand Recursion
#    https://www.youtube.com/watch?v=Q83nN97LVOU
# 2. Recursion in 100 Seconds
#    https://www.youtube.com/watch?v=rf60MejMz3E
# 3. Recursion Simply Explained with Code Examples - Python for Beginners       
#    https://www.youtube.com/watch?v=m1Fjdnj_Mds