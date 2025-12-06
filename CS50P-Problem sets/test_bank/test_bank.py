import pytest
from bank import value

def main():
    test_value_function()


def test_value_function():
    assert value("hello") == 0
    assert value("HeLLo") == 0
    assert value("hi") == 20
    assert value("how are you?") == 20
    assert value("What's up") == 100

if __name__ == "__main__":
    main()
