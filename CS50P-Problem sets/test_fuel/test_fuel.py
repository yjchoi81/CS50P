import pytest
from fuel import convert, gauge


def main():
    test_convert_function()
    test_gauge_function()


def test_convert_function():
    assert convert('3/4') == 75
    assert convert('1/4') == 25
    with pytest.raises(ValueError) as excinfo:
        convert('cat/dog')
    with pytest.raises(ValueError) as excinfo:
        convert('-1/4')
    with pytest.raises(ValueError) as excinfo:
        convert('1/-4')
    with pytest.raises(ZeroDivisionError) as excinfo:
        convert('1/0')


def test_gauge_function():
    assert gauge(75) == '75%'
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'


if __name__ == "__main__":
    main()

