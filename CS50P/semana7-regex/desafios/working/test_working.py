from working import convert
import pytest

def test_padrao1_valueError():
    with pytest.raises(ValueError):
        convert("13 AM to 10 PM")

    with pytest.raises(ValueError):
        convert("13 AM 10 PM")

def test_padrao1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_padrao2_valueError():
    with pytest.raises(ValueError):
        convert("13:00 AM to 10:00 PM")

    with pytest.raises(ValueError):
        convert("13:00 AM 10:00 PM")

def test_padrao2():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"