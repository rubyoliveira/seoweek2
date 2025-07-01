from project.youtube_api import search_youtube_videos

def test_youtube_search_returns_results():
    query = "binary search tutorial"
    results = search_youtube_videos(query)
    
    assert isinstance(results, list)
    assert len(results) <= 3
    for item in results:
        assert isinstance(item, tuple)
        assert len(item) == 2  # (title, url)
        assert item[1].startswith("https://www.youtube.com/watch?v=")
