import pytest
from working import convert

def test_correct_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_uncorrect_format():
    with pytest.raises(ValueError):
        convert("9AM to5pM")
    with pytest.raises(ValueError):
        convert("17AM to 5 PM")
    with pytest.raises(ValueError):
        convert("")
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM ")

def test_minutes():
    assert convert("9:30 AM to 5:00 PM") == "09:30 to 17:00"
    assert convert("4 AM to 12:33 PM") == "04:00 to 12:33"
