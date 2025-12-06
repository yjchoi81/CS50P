from plates import is_valid
import pytest


def main():
    test_len_function()
    test_started_alpha()
    test_alnum_function()
    test_isdigit_function()

def test_len_function():
    assert is_valid("OUTATIME") == False
    assert is_valid("H") == False

def test_started_alpha():
    assert is_valid("H1llo") == False
    assert is_valid("12345") == False

def test_alnum_function():
    assert is_valid("PI3.14") == False

def test_isdigit_function():
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True


if __name__ == "__main__":
    main()
