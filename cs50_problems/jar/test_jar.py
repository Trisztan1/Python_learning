from jar import Jar
import pytest

# test __init__

def test_init_default():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_init_custom_1():
    jar = Jar()
    jar.capacity = 20
    assert jar.capacity == 20

def test_init_custom_2():
    jar = Jar(capacity=20)
    assert jar.capacity == 20

def test_init_invalid_input():
    with pytest.raises(ValueError):
        jar = Jar(capacity=-2)
    
    with pytest.raises(ValueError):
        jar = Jar(capacity=-10)

# test __str__

def test_str():
    jar = Jar()
    assert str(jar) == "Empty jar"
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


# test deposit()

def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(10)
    assert jar.size == 12

def depost_invalid_input():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(13)
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(-2)

# test withdraw()

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(2)
    assert jar.size == 10
    jar.withdraw(8)
    assert jar.size == 2

def test_withdraw_invalid_input():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(12)
        jar.withdraw(13)
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(12)
        jar.withdraw(-2)
    with pytest.raises(ValueError): # test for empty jar
        jar = Jar()
        jar.withdraw(2)

    