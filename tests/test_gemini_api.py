from project.gemini_api import generate_prompt

def test_generate_prompt_returns_string():
    topic = "binary search"
    result = generate_prompt(topic)
    assert isinstance(result, str)
    assert len(result.strip()) > 0
