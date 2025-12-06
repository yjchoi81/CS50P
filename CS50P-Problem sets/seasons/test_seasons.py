import pytest
from seasons import calculate_total_minutes
from datetime import date

def test_calculate_total_minutes():
    born = date(2020, 5, 20)
    assert calculate_total_minutes(born) != 0

    born = date(2000, 5, 20)
    assert calculate_total_minutes(born) != 0

    born = date(1985, 12, 31)
    today = date.today()
    expected = (today - born).days * 1440
    assert calculate_total_minutes(born) == expected

    born = date(2004, 2, 29)
    expected = (today - born).days * 1440
    assert calculate_total_minutes(born) == expected
