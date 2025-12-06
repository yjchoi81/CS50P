import pytest
from twttr import shorten


def main():
    test_shorten_function()

def test_shorten_function():
    assert shorten("Twitter") == "Twttr" # without vowel replacement
    assert shorten("Eggs") == "ggs" # without capitalized vowel replacement
    assert shorten("what's your name?") == "wht's yr nm?" # without  lowercase vowel replacement
    assert shorten("CS50") == "CS50" # printing in uppercase
    assert shorten("12345") == "12345" # omittig numbers
    assert shorten("!@#$") == "!@#$" ## omittig punctuation

if __name__ == "__main__":
    main()
