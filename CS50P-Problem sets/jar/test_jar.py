from jar import Jar
import pytest


def test_init():
    jar = Jar(6)
    assert jar.capacity == 6
    with pytest.raises(ValueError):
        jar = Jar(-5)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(4)
    jar.deposit(4)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.deposit(14)


def test_withdraw():
    jar = Jar(12)
    jar.deposit(5)
    jar.withdraw(5)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(10)
