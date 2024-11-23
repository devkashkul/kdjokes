from main import get_random_joke

def test_joke_length():
    joke = get_random_joke()
    assert len(joke) < 1

def test_joke_word_length():
    joke = get_random_joke()
    assert len(joke.split(' ')) > 4
