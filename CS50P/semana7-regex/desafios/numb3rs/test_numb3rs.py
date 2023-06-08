from numb3rs import validate
import pytest

def test_greather_than_255():
    assert validate("333.0.0.10") == False
    assert validate("1.1.1.1000") == False
    assert validate("1.300.300.1000") == False

def test_one_byte():
    assert validate("1.300.300.1000") == False

def test_value_error_not_dot():
    assert validate("1-1-1-1") == False

def test_value_error_not_digit():
    assert validate("1.1.abc.1") == False

def test_valid_input():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True