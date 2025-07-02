from gemini_api import generate_prompt
from youtube_api import search_youtube_videos
from database import init_db, save_query_and_results, get_search_history

def search_flow():
    user_topic = input("\nWhat topic or concept do you need help with?\n> ")

    if not user_topic.strip():
        print("Please enter a topic. You can't learn from silence!")
        return
    
    print("\nGenerating an optimized search query...")
    search_query = generate_prompt(user_topic)
    print(f"Search query: {search_query}")

    print("\nFetching top YouTube videos...")
    videos = search_youtube_videos(search_query)

    if not videos:
        print("No videos found. Even the AI is confused. Try again?")
        return


    print("\nTop 3 YouTube Results:\n")
    for i, (title, url) in enumerate(videos, 1):
        print(f"{i}. {title}\n   {url}\n")

    save_query_and_results(search_query, videos)
    print("\nSearch saved to history.")

def view_history():
    print("\nRecent Search History:\n")
    history = get_search_history(limit=5)

    if not history:
        print("No search history yet.")
        return

    for i, entry in enumerate(history, 1):
        print(f"{i}. [{entry['timestamp']}] {entry['query']}")
        print(f"   {entry['title']}\n   {entry['url']}\n")

def main():
    init_db()
    print("SmartSearch: AI-Powered Video Finder")

    while True:
        print("\nMenu:")
        print("[1] Search for a topic")
        print("[2] View recent search history")
        print("[3] Exit (because learning is hard and Netflix exists)")

        choice = input("Choose an option (no pressure): ")

        if choice == "1":
            search_flow()
        elif choice == "2":
            view_history()
        elif choice == "3":
            print("Exiting... but your curiosity lives on!")
            break
        else:
            print("I can predict search queries, not your typos. Try again!")


if __name__ == "__main__":
    main()

"""
# sample input and output

🔍 SmartSearch: AI-Powered Video Finder

Menu:
[1] Search for a topic
[2] View recent search history
[3] Exit
Choose an option: 1

What topic or concept do you need help with?
> I need help with object oriented programming. I find it hard to grasp this concept

Generating an optimized search query...
Search query: OOP explained

Fetching top YouTube videos...

Top 3 YouTube Results:

1. Object-Oriented Programming, Simplified
   https://www.youtube.com/watch?v=pTB0EiLXUC8

2. What Is Object Oriented Programming? | OOP Explained
   https://www.youtube.com/watch?v=yBs0ic7pVvk

3. Fundamental Concepts of Object Oriented Programming
   https://www.youtube.com/watch?v=m_MQYyJpIjg


Search saved to history.

Menu:
[1] Search for a topic
[2] View recent search history
[3] Exit
Choose an option: 2

Recent Search History:

1. [2025-07-01T23:02:06.895926] OOP explained
   Object-Oriented Programming, Simplified
   https://www.youtube.com/watch?v=pTB0EiLXUC8

2. [2025-07-01T23:02:06.895926] OOP explained
   What Is Object Oriented Programming? | OOP Explained
   https://www.youtube.com/watch?v=yBs0ic7pVvk

3. [2025-07-01T23:02:06.895926] OOP explained
   Fundamental Concepts of Object Oriented Programming
   https://www.youtube.com/watch?v=m_MQYyJpIjg

4. [2025-07-01T22:45:08.631443] Recursion explained
   This is a Better Way to Understand Recursion
   https://www.youtube.com/watch?v=Q83nN97LVOU

5. [2025-07-01T22:45:08.631443] Recursion explained
   Recursion in 100 Seconds
   https://www.youtube.com/watch?v=rf60MejMz3E


Menu:
[1] Search for a topic
[2] View recent search history
[3] Exit
Choose an option: 3
Goodbye!

"""