from working import convert
import pytest


def main():
    test_wrong_input()
    test_numbers_range()
    test_return_values()


def test_wrong_input():
    with pytest.raises(ValueError):
        convert("9:0 AM to 5:40 AM")
    with pytest.raises(ValueError):
        convert("9 to 5")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("5 PM - 9 PM")
    with pytest.raises(ValueError):
        convert("5 PM 9 PM")


def test_numbers_range():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("0:00 PM to 3:00 AM")


def test_return_values():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("6:30 PM to 10:59 PM") == "18:30 to 22:59"
    assert convert("2:00 PM to 2:01 AM") == "14:00 to 02:01"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"


if __name__ == "__main__":
    main()
