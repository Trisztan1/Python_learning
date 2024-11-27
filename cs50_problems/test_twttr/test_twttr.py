import twttr

def test_shorten_lower():
    assert twttr.shorten("twitter") == "twttr"

def test_shorten_upper():
    assert twttr.shorten("TWITTER") == "TWTTR"

def test_shorten_numbers():
    assert twttr.shorten("12345") == "12345"

def test_shorten_punctuation():
    assert twttr.shorten("hello, world!") == "hll, wrld!"
