import fuel
import pytest

def test_convert():
    assert isinstance(fuel.convert("3/4"), int)
    assert fuel.convert("3/4") == 75

def test_convert_exception():
    with pytest.raises(ValueError):
        fuel.convert("cat")

    with pytest.raises(ValueError):
        fuel.convert("cat/cat")

    with pytest.raises(ZeroDivisionError):
        fuel.convert("3/0")

    with pytest.raises(ValueError):
        fuel.convert("3/2")

def test_gauge_ppercent_symbol():
    assert "%" in fuel.gauge(75)

def test_gauge():
    assert fuel.gauge(75) == "75%"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(1) == "E"
