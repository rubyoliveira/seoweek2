from project.database import init_db, save_query_and_results, get_search_history

def test_database_functions():
    init_db()
    
    query = "test query"
    results = [("Video Title 1", "https://youtube.com/watch?v=abc123"),
               ("Video Title 2", "https://youtube.com/watch?v=def456")]

    save_query_and_results(query, results)

    history = get_search_history(limit=5)

    assert isinstance(history, list)
    assert len(history) >= 2

    record = history[0]
    assert isinstance(record, dict)
    assert 'query' in record and record['query'] == query
    assert 'title' in record and record['title'] in [r[0] for r in results]
    assert 'url' in record and record['url'] in [r[1] for r in results]
    assert 'timestamp' in record
