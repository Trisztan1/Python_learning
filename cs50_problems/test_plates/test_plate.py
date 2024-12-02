from plates import is_valid

def test_short():
    assert is_valid("c") == "Invalid"

def test_long():
    assert is_valid("OUTATIME") == "Invalid"

def test_right_length():
    assert is_valid("right6") == "Valid"

def test_starts_with_number():
    assert is_valid("50cat") == "Invalid"
    assert is_valid("0horse") == "Invalid"

def test_number_in_the_middle():
    assert is_valid("CS50P2") == "Invalid"

def test_zero_first_middle():
    assert is_valid("cs05p") == "Invalid"

def test_number_right():
    assert is_valid("ECTO88") == "Valid"
    assert is_valid("cs50") == "Valid"

def test_punctuation():
    assert is_valid("PI3.14") == "Invalid"