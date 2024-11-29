import bank

def test_hello():
    assert bank.value("hello, newman") == 0

def test_Hi():
    assert bank.value("hi, newman") == 20

def test_else():
    assert bank.value("what's up, newman") == 100

def test_case():
    assert bank.value("Hello") == 0
