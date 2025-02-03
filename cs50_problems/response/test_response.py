from response import validation

def test_incorrect():
    assert validation("sdsdasd") == "Invalid"
    assert validation("malan@@@harvard.edu") == "Invalid"
    assert validation("malan@harvard.edu...") == "Invalid"

def test_correct():
    assert validation("malan@harvard.edu") == "Valid"

def test_all():
    assert validation("malan@@@harvard.edu") == "Invalid"
    assert validation("malan@harvard.edu") == "Valid"