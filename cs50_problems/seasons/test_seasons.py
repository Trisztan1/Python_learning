import pytest
from datetime import date
from seasons import date_to_minutes

current_date = "2025-02-06"

def test_date_format():
    assert date_to_minutes("2024-02-06", current_date) == "Five hundred twenty-seven thousand forty minutes"
    with pytest.raises(ValueError):
        date_to_minutes("2024-44-23", current_date)
    with pytest.raises(ValueError):
        date_to_minutes("2024/44/23", current_date)
    with pytest.raises(ValueError):
        date_to_minutes("2024.44.23", current_date)

def test_dates():
    assert date_to_minutes("2024-02-06", current_date) == "Five hundred twenty-seven thousand forty minutes"
    assert date_to_minutes("2023-02-06", current_date) == "One million, fifty-two thousand, six hundred forty minutes"
