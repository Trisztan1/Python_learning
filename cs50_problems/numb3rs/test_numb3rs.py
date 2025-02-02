from numb3rs import validate

def test_longer():
    assert validate("1.2.3.2.1") == False
    assert validate("1.3.24.34.255") == False

def test_shorter():
    assert validate("232.23.1") == False
    assert validate("32,123.0") == False

def test_zero():
    assert validate("0.0.0.0") == True
    assert validate("0.123.231.9") == True

def test_good_format():
    assert validate("267.23.122.23") == False
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True
    assert validate("0.23.124.249") == True

def test_range():
    assert validate("552.23.332.2") == False
    assert validate("232.443.23.1") == False
