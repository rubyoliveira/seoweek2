from gemini_api import generate_prompt
from youtube_api import search_youtube_videos
from database import init_db, save_query_and_results

def main():
    print("SmartSearch: AI-Powered Video Finder\n")
    # intialize db
    init_db()
    
    # Step 1: Get input from user
    user_topic = input("What topic or concept do you need help with?\n> ")

    # Step 2: Generate YouTube search query using Gemini
    print("\nGenerating an optimized search query...")
    search_query = generate_prompt(user_topic)
    print(f"Search query: {search_query}")

    # Step 3: Search YouTube using that query
    print("\nFetching top YouTube videos...")
    videos = search_youtube_videos(search_query)

    # Step 4: Show results
    if not videos:
        print("No videos found. Try a different topic.")
        return

    print("\nTop 3 YouTube Results:\n")
    for i, (title, url) in enumerate(videos, 1):
        print(f"{i}. {title}\n   {url}\n")
    
    save_query_and_results(search_query, videos)
    print("\nSearch saved to history.")


if __name__ == "__main__":
    main()

"""
# sample input and output

SmartSearch: AI-Powered Video Finder

What topic or concept do you need help with?
> i need help with recursion as a programming concept. I find it hard to under
stand this concept

Generating an optimized search query...
Search query: Recursion programming explained

 Fetching top YouTube videos...

 Top 3 YouTube Results:

1. This is a Better Way to Understand Recursion
   https://www.youtube.com/watch?v=Q83nN97LVOU

2. Recursion in 100 Seconds
   https://www.youtube.com/watch?v=rf60MejMz3E

3. Recursion Simply Explained with Code Examples - Python for Beginners       
   https://www.youtube.com/watch?v=m1Fjdnj_Mds

"""